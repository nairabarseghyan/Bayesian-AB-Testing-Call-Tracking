
# from ..logger import CustomFormatter

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


from sqlalchemy import create_engine,Column,Integer,String,Float, DATE, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

engine=create_engine('sqlite:///temp.db')

Base= declarative_base()

class DimDate(Base):
    __tablename__ = "DimDate"

    DateID = Column(Integer, primary_key=True)
    CalendarDate = Column(DateTime)
    Month = Column(Integer)
    Quarter = Column(Integer)
    Year = Column(Integer)

class DimAdvertisement(Base):
    __tablename__ = "DimAdvertisement"

    AdvertisementID = Column(Integer, primary_key=True)
    AdvertisementType = Column(String)
    Budget = Column(float)

class DimSource(Base):
    __tablename__ = "DimSource"

    SourceID = Column(Integer, primary_key=True)
    SourceName = Column(String)
    SourceType = Column(String)


class DimCustomer(Base):
    __tablename__ = "DimCustomer"

    CustomerID = Column(Integer, primary_key=True)
    CustomerName = Column(String)
    Location = Column(Float)
    ContactInfo = Column(String)


class CallTrackingResults(Base):
    __tablename__ = "CallTrackingResults"

    ResultID = Column(Integer, primary_key=True)
    DateID = Column(Integer, ForeignKey('DimDate.DateID'))
    AdvertisementID = Column(Integer, ForeignKey('DimAdvertisement.AdvertisementID'))
    SourceID = Column(Integer, ForeignKey('DimSource.SourceID'))
    CustomerID = Column(Integer, ForeignKey('DimCustomer.CustomerID'))
    CallDuration = Column(Integer)
    ConversionStatus = Column(String)

    DimDate = relationship("DimDate")
    DimAdvertisement = relationship("DimAdvertisement")
    DimSource = relationship("DimSource")
    DimCustomer = relationship("DimCustomer")


Base.metadata.create_all(engine)
