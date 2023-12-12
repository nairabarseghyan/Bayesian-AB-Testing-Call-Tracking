"""Fake data generators"""

from faker import Faker
import pandas as pd
import random
import numpy as np
import logging
from ..logger import CustomFormatter
import os
import json
from datetime import datetime

logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)

fake=Faker()

    
def generate_arm(arm_id) -> dict:
    """Generates an arm

    Args:
        arm_id (int): arm_id

    Returns:
        dict: arm
    """    

    return {
        "arm_id": arm_id,
        "type": fake.word(),
        "reward": np.random.randint(1, 15),
        "active": np.random.uniform() > 0.85
    }


def generate_customer(customer_id) -> dict:
    """Generates a customer with random info

    Args:
        customer_id (int): customer_id

    Returns:
        dict: customer
    """    

    return {
        "customer_id": customer_id,
        "name": fake.name(),
        "location": fake.street_address(),
        "contact": fake.phone_number()
    }


def generate_date(date_id) -> dict:
    """Generates a random date in 2023

    Args:
        date_id (int): date_id

    Returns:
        dict: date 
    """    

    # Generate a random date between a specific date range
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    random_date = fake.date_time_between_dates(start_date, end_date)

    # Extract year, quarter, and month from the random date
    year = random_date.year
    quarter = (random_date.month - 1) // 3 + 1
    month = random_date.strftime('%m')
    day = random_date.strftime('%d')

    return {
        "date_id": date_id,
        "date": random_date.strftime("%Y-%m-%d"),
        "day": day,
        "month": month,
        "quarter": quarter,
        "year": year
    }


def generate_serve(serve_id, date_id, customer_id, arm_id, p) -> dict:
    """Generates a serve with random info

    Args:
        serve_id (int): serve_id
        date_id (int): date_id
        customer_id (int): customer_id
        arm_id (int): arm_id
        p (float): probability of success

    Returns:
        dict: serve
    """    

    return {
        "serve_id": serve_id,
        "date_id": date_id,
        "customer_id": customer_id,
        "arm_id": arm_id,
        "information": json.dumps(fake.profile()),
        "result": np.random.uniform() >= p
    }



