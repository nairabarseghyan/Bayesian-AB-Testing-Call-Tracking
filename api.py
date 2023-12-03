"""API for Bayesian A/B testing"""

# region imports

from functools import wraps
from fastapi import FastAPI
from typing import Union
import pandas as pd
import sqlite3
import logging

from AB_Testing.data_preperation import SqlHandler
from AB_Testing.data_preperation.schema import create_ORM
from AB_Testing.models.TS_Bernoulli import ThompsonAlgo, ThompsonArm
import AB_Testing

# endregion imports

# region initialization

app = FastAPI()

create_ORM(AB_Testing.db_path)
cnxn = sqlite3.connect(AB_Testing.db_path)

#
# Authentication skipped since this is purely educational, 
# make sure to add it if you choose to use this in production
#

# endregion initialization

@app.get("/arm")
async def get_arm(id: int = -1):
    """Gets arm information, or multiple if id = -1

    Args:
        id (int, optional): id of arm. Defaults to -1.

    Returns:
        dict: arm info
    """    
    with SqlHandler("DimArm") as dim_arm:
        if id < 0:
            res = dim_arm.from_sql_to_pandas().to_dict()
            
            return {k:{id:v[id]} if id < len(v) and id >= 0 else v for k, v in res.items()} if id is not None else res
        else:
            res = dim_arm.select_one(id)

    return res


@app.post("/arm")
async def add_arm(customer_id: int, type: str, reward: float):
    """Adds an arm

    Args:
        customer_id (int): identifier
        type (str): type
        reward (float): Amount of reward per trigger

    Returns:
        dict: Arm as a dict
    """    
    id = SqlHandler("DimArm").get_next_id()
    ThompsonArm(id, cnxn, type=type, customer_id=customer_id, reward=reward)

    return {"arm_id": id, "type": type, "reward": reward, "active": 1}

    
@app.put("/arm/type")
async def mod_arm(id: int, type: Union[str, None]):
    """Modifies the type of the arm

    Args:
        id (int): arm identifier
        type (Union[str, None]): type

    Returns:
        str: "ok" if ok
    """    
    try:
        ThompsonArm(id).change_type(type)
    except ValueError as e:
        return "ValueError: " + str(e)
    return "ok"


@app.put("/arm")
async def toggle_arm(id: int):
    """Turns an arm on/off"""
    try:
        ThompsonArm(id, cnxn).toggle_active()
    except ValueError as e:
        logging.error(e)
        return "ValueError: " + str(e)
    
    return "ok"



@app.get("/sample")
async def sample_arm(customer_id: int, information: Union[str, None]) -> dict:
    """Samples from all arms and choses the best one

    Args:
        customer_id (int): Customer id
        information (Union[str, None]): Additional client data

    Returns:
        dict: a serve object as a dict
    """    
    algo = ThompsonAlgo(cnxn, customer_id)
    serve = algo.get_best_arm(information)

    return serve


@app.put("/sample")
async def log_result(customer_id, arm_id, serve_id) -> str:
    """Logs a trigger

    Args:
        customer_id (int): Customer identifier
        arm_id (int): Arm identifier
        serve_id (int): Serve identifier

    Returns:
        str: "ok" of ok
    """    
    algo = ThompsonAlgo(cnxn, customer_id)
    [arm for arm in algo.arms if arm.id == int(arm_id)][0].log_trigger(serve_id)
    return "ok"



@app.get("/stats")
async def stats(arm_id: int):
    """Summary statistics and state of an arm

    Args:
        arm_id (int): arm identifier

    Returns:
        dict: Dict with aggregated values and state
    """    
    agr = SqlHandler("AggregateResult")
    res = agr.select_one(arm_id)
    return res



@app.post("/client")
async def add_client(name:str, location: str, contact: str):
    """Adds a client to the db

    Args:
        name (str): Name
        location (str): location
        contact (str): contact info

    Returns:
        dict: customer as a dict
    """    
    cust = SqlHandler("DimCustomer")
    id = cust.get_next_id()
    cust_dict = dict(customer_id=id, name=name, location=location, contact=contact)
    cust.insert_one(**cust_dict)

    return cust_dict