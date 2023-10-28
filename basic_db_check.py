# Script to check insertion into database on example of sample advertisment data.

from AB_Testing.data_preperation import SqlHandler
from AB_Testing.logger import CustomFormatter
import pandas as pd


Inst=SqlHandler('CallTracking', 'DimAdvertisement')


data=pd.read_csv('ad_sample.csv')

# Inst.truncate_table()
Inst.insert_many(data)


Inst.close_cnxn()

