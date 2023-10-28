-- Create Database
CREATE DATABASE CallTracking;
GO

-- Use the Created DB
USE CallTracking;
GO

-- Create DimDate Table
CREATE TABLE DimDate (
    DateID INT PRIMARY KEY,
    CalendarDate DATE,
    Day INT,
    Month INT,
    Quarter INT,
    Year INT
);

-- Create DimAdvertisement Table
CREATE TABLE DimAdvertisement (
    AdvertisementID INT PRIMARY KEY,
    AdvertisementType VARCHAR(255),
    Budget DECIMAL(18, 2)
);

-- Create DimSource Table
CREATE TABLE DimSource (
    SourceID INT PRIMARY KEY,
    SourceName VARCHAR(255),
    SourceType VARCHAR(255)
);

-- Create DimAlgorithm Table
CREATE TABLE DimAlgorithm (
    AlgorithmID INT PRIMARY KEY,
    AlgorithmName VARCHAR(255),
    Description VARCHAR(MAX)
);

-- Create DimCustomer Table
CREATE TABLE DimCustomer (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(255),
    Location VARCHAR(255),
    ContactInfo VARCHAR(255)
);

-- Create CallTrackingResults Table (Fact Table)
CREATE TABLE CallTrackingResults (
    ResultID INT PRIMARY KEY,
    DateID INT FOREIGN KEY REFERENCES DimDate(DateID),
    AdvertisementID INT FOREIGN KEY REFERENCES DimAdvertisement(AdvertisementID),
    SourceID INT FOREIGN KEY REFERENCES DimSource(SourceID),
    AlgorithmID INT FOREIGN KEY REFERENCES DimAlgorithm(AlgorithmID),
    CustomerID INT FOREIGN KEY REFERENCES DimCustomer(CustomerID),
    CallDuration INT,
    ConversionStatus VARCHAR(50)
);

SELECT * FROM DimCustomer
SELECT * FROM CallTrackingResults