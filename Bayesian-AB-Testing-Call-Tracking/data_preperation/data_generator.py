from faker import Faker
import pandas as pd
import random
import logging
from ..logger import CustomFormatter
import os
from datetime import datetime
logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)

fake=Faker()

# Data Models

# advetisment generator 
def generate_advertisment(advertisment_id):
    ads = ["Facebook", "Instagram", "Billboard", "Flyer", "TV", "Magazine"]
    return {
        "AdvertisementID": advertisment_id,
        "AdvertisementType": random.choice(ads)
    }

#Source generator 
def generate_source(employee_id):
    return {
        "SourceID": employee_id,
        "SourceName": fake.first_name(),
        "SourceType": fake.last_name(),
    }

def generate_customer(customer_id):
    return {
        "CustomerID": customer_id,
        "customer_name": fake.name(),
        "Location": fake.street_address(),
        "ContactInfo": fake.phoneNumber().cellPhone()
    }

def generate_date(date_id):
    # Generate a random date between a specific date range
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    random_date = fake.date_time_between_dates(start_date, end_date)

    # Extract year, quarter, and month from the random date
    year = random_date.year
    quarter = (random_date.month - 1) // 3 + 1
    month = random_date.strftime('%B')

    return {
        "dateId": date_id,
        "callDate": random_date,
        "callDuration": year
    }

### NOT YET IMPLEMETED IN DB ###
def generate_CALLS(transaction_id, order_id, product_id, customer_id, employee_id):
    total_sales = round(random.uniform(10.0, 500.0), 2)
    quantity = random.randint(1, 10)
    discount = round(random.uniform(0.0, 0.5), 2)

    return {
        "transaction_id": transaction_id,
        "order_id": order_id,
        "product_id": product_id,
        "customer_id": customer_id,
        "employee_id": employee_id,
        "total_sales": total_sales,
        "quantity": quantity,
        "discount": discount
    }



