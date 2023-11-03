-- Create Database CallTracking
-- CREATE DATABASE CallTracking;
-- GO

-- USE CallTracking;
-- GO

-- drop table if exists DimDate, DimAdvertisement, DimSource, DimAlgorithm, DimCustomer, CallTrackingResults

-- Create tables
CREATE TABLE DimDate (
    DateID INT PRIMARY KEY,
    CalendarDate DATETIME,
    Month INT,
    Quarter INT,
    Year INT
);

CREATE TABLE DimAdvertisement (
    AdvertisementID INT PRIMARY KEY,
    AdvertisementType VARCHAR(255),
    Budget DECIMAL(18, 2)
);

CREATE TABLE DimSource (
    SourceID INT PRIMARY KEY,
    SourceName VARCHAR(255),
    SourceType VARCHAR(255)
);

-- CREATE TABLE DimAlgorithm (
--     AlgorithmID INT PRIMARY KEY,
--     AlgorithmName VARCHAR(255),
--     Description VARCHAR(2048)
-- );

CREATE TABLE DimCustomer (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(255),
    Location VARCHAR(255),
    ContactInfo VARCHAR(255)
);

CREATE TABLE CallTrackingResults (
    ResultID INT PRIMARY KEY,
    DateID INT,
    AdvertisementID INT,
    SourceID INT,
    AlgorithmID INT,
    CustomerID INT,
    CallDuration INT,
    ConversionStatus VARCHAR(50),
    FOREIGN KEY(CustomerID) REFERENCES DimCustomer(CustomerID),
    FOREIGN KEY(AlgorithmID) REFERENCES DimAlgorithm(AlgorithmID),
    FOREIGN KEY(SourceID) REFERENCES DimSource(SourceID),
    FOREIGN KEY(AdvertisementID) REFERENCES DimAdvertisement(AdvertisementID),
    FOREIGN KEY(DateID) REFERENCES DimDate(DateID)
);

