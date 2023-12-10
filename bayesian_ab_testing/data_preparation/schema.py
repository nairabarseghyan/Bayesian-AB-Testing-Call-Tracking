"""Contains any DDL for the database"""

import logging
import os

import logging
from ..logger import CustomFormatter

logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)


from sqlalchemy import create_engine, Column, Integer, String, Float, DATE, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

def create_ORM(path):
    """Creates the sql tables by mapping objects to it

    Args:
        path (_type_): path to sqlite db
    """    

    engine = create_engine(f'sqlite:///{path}')

    Base = declarative_base()

    class DimDate(Base):
        __tablename__ = "DimDate"

        date_id = Column(Integer, primary_key=True)
        date = Column(DateTime)
        day = Column(Integer)
        month = Column(Integer)
        quarter = Column(Integer)
        year = Column(Integer)


    class DimArm(Base):
        __tablename__ = "DimArm"

        arm_id = Column(Integer, primary_key=True)
        type = Column(String)
        reward = Column(Float)
        active = Column(Boolean)


    class DimCustomer(Base):
        __tablename__ = "DimCustomer"

        customer_id = Column(Integer, primary_key=True)
        name = Column(String)
        location = Column(String)
        contact = Column(String)


    class Serve(Base):
        __tablename__ = "Serve"

        serve_id = Column(Integer, primary_key=True)
        date_id = Column(Integer, ForeignKey('DimDate.date_id'))
        customer_id = Column(Integer, ForeignKey('DimCustomer.customer_id'))
        arm_id = Column(Integer, ForeignKey('DimArm.arm_id'))
        information = Column(String)
        result = Column(Boolean, nullable = True)


    class AggregateResult(Base):
        __tablename__ = "AggregateResult"

        arm_id = Column(Integer, primary_key=True)
        customer_id = Column(Integer)
        n_triggered = Column(Integer)
        n_served = Column(Integer)
        a = Column(Float)
        b = Column(Float)
        average_reward = Column(Float)




    Base.metadata.create_all(engine)
    del Base
    del engine