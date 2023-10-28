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


def source_type_identifier(source):
    online_source =["Facebook", "Instagram"]
    offline_sources = ["Billboard", "Flyer", "TV", "Magazine"]
    if source in online_source:
        return "Online"
    elif source in offline_sources:
        return "Offline"
    else:
        return "Unknown"
    
# Data Models

# advetisment generator 
def generate_advertisment(advertisment_id):
    return {
        "AdvertisementID": advertisment_id,
        "AdvertisementType": fake.word()
    }

#Source generator 
def generate_source(employee_id):
    sources = ["Facebook", "Instagram", "Billboard", "Flyer", "TV", "Magazine"]
    source_choice = random.choice(sources)
    return {
        "SourceID": employee_id,
        "SourceName": source_choice,
        "SourceType": source_type_identifier(source_choice)
    }

def generate_customer(customer_id):
    return {
        "CustomerID": customer_id,
        "customer_name": fake.name(),
        "Location": fake.street_address(),
        "ContactInfo": fake.phone_number()
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
def generate_calls(call_id, customer_id, product_id, phone_number_id, source_id):

    return {
        "call_id": call_id,
        "customer_id": customer_id,
        "phone_number_id": phone_number_id,
        "source_id": source_id,
        "call_duration": random.randint(0,1000)
    }



