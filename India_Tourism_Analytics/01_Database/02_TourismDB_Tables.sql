-- ============================================================================
-- Project 2: India Tourist Attractions & Tourism Analytics System
-- Script: 02_TourismDB_Tables.sql
-- Database: IndiaTourismAnalyticsDB
-- Purpose: Creates Star Schema Dimension and Fact tables with PK/FK constraints
-- ============================================================================

USE IndiaTourismAnalyticsDB;
GO

-- ----------------------------------------------------------------------------
-- Drop tables if they already exist (drop fact table first due to FKs)
-- ----------------------------------------------------------------------------
IF OBJECT_ID('dbo.FactTourismVisits', 'U') IS NOT NULL DROP TABLE dbo.FactTourismVisits;
IF OBJECT_ID('dbo.DimAttractions', 'U') IS NOT NULL DROP TABLE dbo.DimAttractions;
IF OBJECT_ID('dbo.DimAttractionTypes', 'U') IS NOT NULL DROP TABLE dbo.DimAttractionTypes;
IF OBJECT_ID('dbo.DimCities', 'U') IS NOT NULL DROP TABLE dbo.DimCities;
IF OBJECT_ID('dbo.DimStates', 'U') IS NOT NULL DROP TABLE dbo.DimStates;
IF OBJECT_ID('dbo.DimDates', 'U') IS NOT NULL DROP TABLE dbo.DimDates;
IF OBJECT_ID('dbo.DimVisitorSegments', 'U') IS NOT NULL DROP TABLE dbo.DimVisitorSegments;
GO

-- ----------------------------------------------------------------------------
-- 1. DimStates (States and Union Territories of India)
-- ----------------------------------------------------------------------------
CREATE TABLE dbo.DimStates (
    StateID INT IDENTITY(1,1) NOT NULL,
    StateName NVARCHAR(100) NOT NULL,
    StateType NVARCHAR(50) NOT NULL, -- 'State' or 'Union Territory'
    Region NVARCHAR(50) NOT NULL,    -- 'North India', 'South India', 'East India', 'West India', 'Central India', 'Northeast India'
    Capital NVARCHAR(100) NULL,
    CONSTRAINT PK_DimStates PRIMARY KEY CLUSTERED (StateID),
    CONSTRAINT UQ_DimStates_StateName UNIQUE (StateName)
);
GO

-- ----------------------------------------------------------------------------
-- 2. DimCities (Cities and Districts in India)
-- ----------------------------------------------------------------------------
CREATE TABLE dbo.DimCities (
    CityID INT IDENTITY(1,1) NOT NULL,
    CityName NVARCHAR(100) NOT NULL,
    StateID INT NOT NULL,
    District NVARCHAR(100) NULL,
    Latitude DECIMAL(9,6) NULL,
    Longitude DECIMAL(9,6) NULL,
    CONSTRAINT PK_DimCities PRIMARY KEY CLUSTERED (CityID),
    CONSTRAINT FK_DimCities_DimStates FOREIGN KEY (StateID) REFERENCES dbo.DimStates(StateID)
);
GO

-- ----------------------------------------------------------------------------
-- 3. DimAttractionTypes (Categories of Tourism Attractions)
-- ----------------------------------------------------------------------------
CREATE TABLE dbo.DimAttractionTypes (
    AttractionTypeID INT IDENTITY(1,1) NOT NULL,
    AttractionTypeName NVARCHAR(100) NOT NULL,
    CategoryGroup NVARCHAR(100) NOT NULL, -- e.g., 'Cultural & Heritage', 'Nature & Wildlife', 'Adventure & Recreation', 'Religious & Spiritual'
    CONSTRAINT PK_DimAttractionTypes PRIMARY KEY CLUSTERED (AttractionTypeID),
    CONSTRAINT UQ_DimAttractionTypes_TypeName UNIQUE (AttractionTypeName)
);
GO

-- ----------------------------------------------------------------------------
-- 4. DimAttractions (Tourist Destinations & Landmarks)
-- ----------------------------------------------------------------------------
CREATE TABLE dbo.DimAttractions (
    AttractionID INT IDENTITY(1,1) NOT NULL,
    AttractionName NVARCHAR(200) NOT NULL,
    CityID INT NOT NULL,
    AttractionTypeID INT NOT NULL,
    Description NVARCHAR(MAX) NULL,
    UNESCOStatus NVARCHAR(20) NOT NULL DEFAULT 'Non-UNESCO', -- 'UNESCO World Heritage' or 'Non-UNESCO'
    HistoricalImportance NVARCHAR(50) NOT NULL DEFAULT 'Moderate', -- 'High', 'Moderate', 'Low'
    BestSeason NVARCHAR(50) NOT NULL DEFAULT 'All Year',
    EntryFee DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    OpeningTime NVARCHAR(20) NULL,
    ClosingTime NVARCHAR(20) NULL,
    CONSTRAINT PK_DimAttractions PRIMARY KEY CLUSTERED (AttractionID),
    CONSTRAINT FK_DimAttractions_DimCities FOREIGN KEY (CityID) REFERENCES dbo.DimCities(CityID),
    CONSTRAINT FK_DimAttractions_DimAttractionTypes FOREIGN KEY (AttractionTypeID) REFERENCES dbo.DimAttractionTypes(AttractionTypeID)
);
GO

-- ----------------------------------------------------------------------------
-- 5. DimDates (Temporal Dimension)
-- ----------------------------------------------------------------------------
CREATE TABLE dbo.DimDates (
    DateKey INT NOT NULL, -- Format YYYYMMDD
    FullDate DATE NOT NULL,
    Year INT NOT NULL,
    Quarter INT NOT NULL,
    Month INT NOT NULL,
    MonthName NVARCHAR(20) NOT NULL,
    Season NVARCHAR(20) NOT NULL, -- 'Winter', 'Spring', 'Summer', 'Monsoon'
    Day INT NOT NULL,
    IsWeekend BIT NOT NULL DEFAULT 0,
    CONSTRAINT PK_DimDates PRIMARY KEY CLUSTERED (DateKey)
);
GO

-- ----------------------------------------------------------------------------
-- 6. DimVisitorSegments (Target Demographics)
-- ----------------------------------------------------------------------------
CREATE TABLE dbo.DimVisitorSegments (
    VisitorSegmentID INT IDENTITY(1,1) NOT NULL,
    SegmentName NVARCHAR(50) NOT NULL, -- 'Domestic', 'International', 'Family', 'Solo', 'Couple', 'Group'
    CONSTRAINT PK_DimVisitorSegments PRIMARY KEY CLUSTERED (VisitorSegmentID)
);
GO

-- ----------------------------------------------------------------------------
-- 7. FactTourismVisits (Central Fact Table: ~25,000 Analytics Records)
-- ----------------------------------------------------------------------------
CREATE TABLE dbo.FactTourismVisits (
    TourismVisitID BIGINT IDENTITY(1,1) NOT NULL,
    AttractionID INT NOT NULL,
    StateID INT NOT NULL,
    CityID INT NOT NULL,
    DateKey INT NOT NULL,
    VisitorSegmentID INT NOT NULL,
    VisitorCount INT NOT NULL CHECK (VisitorCount >= 0),
    DomesticVisitors INT NOT NULL CHECK (DomesticVisitors >= 0),
    InternationalVisitors INT NOT NULL CHECK (InternationalVisitors >= 0),
    AverageRating DECIMAL(3,2) NOT NULL CHECK (AverageRating >= 0.0 AND AverageRating <= 5.0),
    EntryFee DECIMAL(10,2) NOT NULL CHECK (EntryFee >= 0.00),
    EstimatedRevenue DECIMAL(15,2) NOT NULL CHECK (EstimatedRevenue >= 0.00),
    PopularityScore DECIMAL(5,2) NOT NULL CHECK (PopularityScore >= 0.0 AND PopularityScore <= 100.0),
    AverageStayDuration DECIMAL(4,2) NOT NULL CHECK (AverageStayDuration >= 0.0),
    IsPeakSeason BIT NOT NULL DEFAULT 0,
    CONSTRAINT PK_FactTourismVisits PRIMARY KEY CLUSTERED (TourismVisitID),
    CONSTRAINT FK_FactTourismVisits_Attraction FOREIGN KEY (AttractionID) REFERENCES dbo.DimAttractions(AttractionID),
    CONSTRAINT FK_FactTourismVisits_State FOREIGN KEY (StateID) REFERENCES dbo.DimStates(StateID),
    CONSTRAINT FK_FactTourismVisits_City FOREIGN KEY (CityID) REFERENCES dbo.DimCities(CityID),
    CONSTRAINT FK_FactTourismVisits_Date FOREIGN KEY (DateKey) REFERENCES dbo.DimDates(DateKey),
    CONSTRAINT FK_FactTourismVisits_VisitorSegment FOREIGN KEY (VisitorSegmentID) REFERENCES dbo.DimVisitorSegments(VisitorSegmentID)
);
GO

-- ----------------------------------------------------------------------------
-- Indexes for Performance Optimization
-- ----------------------------------------------------------------------------
CREATE NONCLUSTERED INDEX IX_FactTourismVisits_StateID ON dbo.FactTourismVisits(StateID);
CREATE NONCLUSTERED INDEX IX_FactTourismVisits_AttractionID ON dbo.FactTourismVisits(AttractionID);
CREATE NONCLUSTERED INDEX IX_FactTourismVisits_DateKey ON dbo.FactTourismVisits(DateKey);
CREATE NONCLUSTERED INDEX IX_FactTourismVisits_VisitorSegmentID ON dbo.FactTourismVisits(VisitorSegmentID);
CREATE NONCLUSTERED INDEX IX_FactTourismVisits_CompositeAnalytics ON dbo.FactTourismVisits(StateID, AttractionID, DateKey) INCLUDE (VisitorCount, EstimatedRevenue, AverageRating);
GO

PRINT 'Star Schema dimension and fact tables successfully created with constraints and indexes.';
GO
