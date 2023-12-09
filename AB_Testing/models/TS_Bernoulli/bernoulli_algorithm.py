"""Bernoulli reward AB testing algorithm"""

import logging
from ...logger import CustomFormatter
from ...utils import ISQL_Etiquette
from ...data_preperation import SqlHandler
import sqlite3
import os
import numpy as np
from datetime import datetime

logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)


class ThompsonArm(ISQL_Etiquette):
    """
    An implementation of the Thompson Sampling algorithm arm.
    """
    
    def __init__(self, id: int, cnxn: sqlite3.Connection, **kwargs):
        """Constructor for the arm.

        Args:
            id (int): arm_id
            cnxn (sqlite3.Connection): sqlite3.connection

        Raises:
            ValueError: provide `type` and `reward` to create entry in DimArm if none exists
            ValueError: provide `customer_id` to create entry in AggregateResult if none exists
        """        

        super().__init__()

        self.cnxn = cnxn
        self.id = id

        # region checking DimArm

        em = f"No arm in db with id {id}"

        cur = list(self.exec("select type, reward, active from DimArm where arm_id = ?", (id, )))

        if len(cur) == 0:
            if all([k in list(kwargs.keys()) for k in ["type", "reward"]]):
                logging.warning(em + ", attempting to create one")
                
                sh = SqlHandler("DimArm")
                sh.insert_one(arm_id = id, type = kwargs["type"], reward = kwargs["reward"], active = 1)
                self.type_, self.reward, self.active = kwargs["type"], kwargs["reward"], 1
            else:
                logging.error(em)
                raise ValueError(em + "provide `type` and `reward` to create one")
        else:
            logging.info("Found arm in DimArm")
            self.type_, self.reward, self.active = cur[0]

        # endregion checking DimArm

        # region checking AggregateResult

        self.sh = SqlHandler("AggregateResult")

        cur = list(self.exec("select customer_id, n_triggered, n_served, a, b, average_reward from AggregateResult where arm_id = ?", (id,)))
        if len(cur) == 0:
            if "customer_id" in list(kwargs.keys()):
                logging.warning(em + ", attempting to create one")
                
                self.sh.insert_one(arm_id = id, n_triggered = 0, n_served = 0, a = 1, b = 1, average_reward = 0, customer_id = kwargs["customer_id"])
                self.n_triggered, self.n_served, self.a, self.b, self.average_reward, self.customer_id = 0, 0, 1, 1, 0, kwargs["customer_id"]
            else:
                logging.error(em)
                raise ValueError(em + "provide `customer_id` to create one")
        else:
            logging.info("Found arm in AggregateResult")
            self.customer_id, self.n_triggered, self.n_served, self.a, self.b, self.average_reward = cur[0]

        # endregion checking AggregateResult
        

    def __repr__(self):
        """
        String representation of the arm.
        """
        return f"Bandit {self.id} with {self.n_triggered / self.n_served} Win Rate"


    def pull(self):
        """
        Pulls a random number from the beta distribution (used to determine winner while allowing for exploration)
        """
        sample = np.random.beta(self.a, self.b) if self.active else 0
        return sample


    def log_sampled(self, information: str = None):
        """Acknowledge the fact that this arm has been chosen by the algorithm

        Args:
            information (str, optional): Information provided by the customer to store without structure. Defaults to None.

        Returns:
            dict: serve
        """        
        """"""
        self.n_served += 1
        self.b = self.n_served - self.n_triggered + 1
        self.sh.update_one(self.id, n_served = self.n_served, b = self.b)

        
        dim_date = SqlHandler("DimDate")
        date_id = dim_date.get_next_id()
        curr_date = datetime.now()
        dim_date.insert_one(
            date_id=date_id, 
            date=curr_date.strftime("%Y/%m/%d %H:%M:%S"),
            day=curr_date.day,
            month=curr_date.month,
            quarter=((curr_date.month-1) // 3) + 1,
            year=curr_date.year
        )
        

        serve_tbl = SqlHandler("Serve")
        serve_id = serve_tbl.get_next_id()
        serve_dict = dict(serve_id=serve_id, date_id=date_id, customer_id=self.customer_id, arm_id=self.id, information=information, result=None)
        serve_tbl.insert_one(**serve_dict)

        return serve_dict


    def log_trigger(self, serve_id: int):
        """Acknowledge the fact that this arm triggered a reward

        Args:
            serve_id (int): serve_id
        """       

        self.n_triggered += 1
        self.average_reward = self.n_triggered * self.reward / self.n_served
        self.a += 1
        self.sh.update_one(self.id, n_triggered = self.n_triggered, average_reward = self.average_reward, a = self.a)

        serve_tbl = SqlHandler("Serve")
        serve_tbl.update_one(serve_id, result=1)


    def change_type(self, type = None):
        """Change the type of the arm

        Args:
            type (str, optional): Arm type. Defaults to None.

        Returns:
            self: self
        """        
        with SqlHandler("DimArm") as dim_arm:
            arm = dim_arm.select_one(self.id)
            dim_arm.update_one(id, type=type)

        self.type_ = type
        return self
    

    def toggle_active(self):
        with SqlHandler("DimArm") as dim_arm:
            dim_arm.update_one(self.id, active = not self.active)

        self.active = not self.active
        return self



class ThompsonAlgo(ISQL_Etiquette):
    """The sampling algorithm used for live A/B testing"""
        
    def __init__(self, cnxn: sqlite3.Connection, customer_id: int):
        """Constructor that initializes the thompson algorithm

        Args:
            cnxn (sqlite3.Connection): Connection to db
            customer_id (int): customer_id

        Raises:
            ValueError: The customer has no active arms
        """        

        self.cnxn = cnxn
        self.customer_id = customer_id

        arms = list(self.exec(
            "select arm_id, type, reward, active from DimArm where arm_id in (select arm_id from AggregateResult where customer_id = ?)", 
            (customer_id,)
        ))

        if len([i for i in arms if i[-1]]) == 0:
            logging.error((em := "The customer has no active arms"))
            raise ValueError(em)

        self.arms = [ThompsonArm(arm_id, cnxn, type=type_, reward=reward, active=active, customer_id=customer_id) for arm_id, type_, reward, active in arms]
      
    
    def get_best_arm(self, information: str = None) -> dict:
        """Samples the best arm

        Args:
            information (str, optional): Information provided by the customer to be stored without structure. Defaults to None.

        Returns:
            dict: serve 
        """        
        j = np.argmax([arm.pull() for arm in self.arms])
        best_arm = self.arms[j]
        serve = best_arm.log_sampled(information)

        return serve
        