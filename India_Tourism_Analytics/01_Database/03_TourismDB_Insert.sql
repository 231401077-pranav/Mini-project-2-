-- ============================================================================
-- Project 2: India Tourist Attractions & Tourism Analytics System
-- Script: 03_TourismDB_Insert.sql
-- Database: IndiaTourismAnalyticsDB
-- Purpose: Representative seed insertion procedures and dimension loading statements
--          (Full 25,000 facts are ingested via Python ETL pipeline load_tourism_data_to_sqlserver.py)
-- ============================================================================

USE IndiaTourismAnalyticsDB;
GO

-- ----------------------------------------------------------------------------
-- 1. Populate Seed DimStates (Sample standard T-SQL Insertion)
-- ----------------------------------------------------------------------------
INSERT INTO dbo.DimStates (StateName, StateType, Region, Capital) VALUES
('Andhra Pradesh', 'State', 'South India', 'Amaravati'),
('Arunachal Pradesh', 'State', 'Northeast India', 'Itanagar'),
('Assam', 'State', 'Northeast India', 'Dispur'),
('Bihar', 'State', 'East India', 'Patna'),
('Chhattisgarh', 'State', 'Central India', 'Raipur'),
('Goa', 'State', 'West India', 'Panaji'),
('Gujarat', 'State', 'West India', 'Gandhinagar'),
('Haryana', 'State', 'North India', 'Chandigarh'),
('Himachal Pradesh', 'State', 'North India', 'Shimla'),
('Jharkhand', 'State', 'East India', 'Ranchi'),
('Karnataka', 'State', 'South India', 'Bengaluru'),
('Kerala', 'State', 'South India', 'Thiruvananthapuram'),
('Madhya Pradesh', 'State', 'Central India', 'Bhopal'),
('Maharashtra', 'State', 'West India', 'Mumbai'),
('Manipur', 'State', 'Northeast India', 'Imphal'),
('Meghalaya', 'State', 'Northeast India', 'Shillong'),
('Mizoram', 'State', 'Northeast India', 'Aizawl'),
('Nagaland', 'State', 'Northeast India', 'Kohima'),
('Odisha', 'State', 'East India', 'Bhubaneswar'),
('Punjab', 'State', 'North India', 'Chandigarh'),
('Rajasthan', 'State', 'West India', 'Jaipur'),
('Sikkim', 'State', 'Northeast India', 'Gangtok'),
('Tamil Nadu', 'State', 'South India', 'Chennai'),
('Telangana', 'State', 'South India', 'Hyderabad'),
('Tripura', 'State', 'Northeast India', 'Agartala'),
('Uttar Pradesh', 'State', 'North India', 'Lucknow'),
('Uttarakhand', 'State', 'North India', 'Dehradun'),
('West Bengal', 'State', 'East India', 'Kolkata'),
('Andaman and Nicobar Islands', 'Union Territory', 'South India', 'Port Blair'),
('Chandigarh', 'Union Territory', 'North India', 'Chandigarh'),
('Dadra and Nagar Haveli and Daman and Diu', 'Union Territory', 'West India', 'Daman'),
('Delhi', 'Union Territory', 'North India', 'New Delhi'),
('Jammu and Kashmir', 'Union Territory', 'North India', 'Srinagar'),
('Ladakh', 'Union Territory', 'North India', 'Leh'),
('Lakshadweep', 'Union Territory', 'South India', 'Kavaratti'),
('Puducherry', 'Union Territory', 'South India', 'Puducherry');
GO

-- ----------------------------------------------------------------------------
-- 2. Populate Seed DimAttractionTypes
-- ----------------------------------------------------------------------------
INSERT INTO dbo.DimAttractionTypes (AttractionTypeName, CategoryGroup) VALUES
('Beach', 'Nature & Coastal'),
('Waterfall', 'Nature & Coastal'),
('Hill Station', 'Nature & Hill Stations'),
('Fort', 'Cultural & Heritage'),
('Palace', 'Cultural & Heritage'),
('Temple', 'Religious & Spiritual'),
('Church', 'Religious & Spiritual'),
('Mosque', 'Religious & Spiritual'),
('Museum', 'Cultural & Heritage'),
('National Park', 'Wildlife & Eco Tourism'),
('Wildlife Sanctuary', 'Wildlife & Eco Tourism'),
('Trekking', 'Adventure & Recreation'),
('Adventure', 'Adventure & Recreation'),
('Heritage Site', 'Cultural & Heritage'),
('Lake', 'Nature & Hill Stations'),
('Cave', 'Cultural & Heritage'),
('Island', 'Nature & Coastal'),
('Monument', 'Cultural & Heritage');
GO

-- ----------------------------------------------------------------------------
-- 3. Populate Seed DimVisitorSegments
-- ----------------------------------------------------------------------------
INSERT INTO dbo.DimVisitorSegments (SegmentName) VALUES
('Domestic'),
('International'),
('Family'),
('Solo'),
('Couple'),
('Group');
GO

PRINT 'Sample T-SQL dimension data populated successfully.';
GO
