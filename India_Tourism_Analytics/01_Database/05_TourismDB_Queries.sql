-- ============================================================================
-- Project 2: India Tourist Attractions & Tourism Analytics System
-- Script: 05_TourismDB_Queries.sql
-- Database: IndiaTourismAnalyticsDB
-- Purpose: 15 Advanced T-SQL Analytical Queries answering practical business & faculty evaluation questions
-- ============================================================================

USE IndiaTourismAnalyticsDB;
GO

-- ----------------------------------------------------------------------------
-- Query 1: Top 10 States by Total Visitor Count
-- ----------------------------------------------------------------------------
SELECT TOP 10 
    s.StateName,
    s.Region,
    SUM(f.VisitorCount) AS TotalVisitors,
    SUM(f.DomesticVisitors) AS DomesticVisitors,
    SUM(f.InternationalVisitors) AS InternationalVisitors
FROM dbo.DimStates s
JOIN dbo.FactTourismVisits f ON s.StateID = f.StateID
GROUP BY s.StateName, s.Region
ORDER BY TotalVisitors DESC;
GO

-- ----------------------------------------------------------------------------
-- Query 2: Top 10 States by Estimated Tourism Revenue
-- ----------------------------------------------------------------------------
SELECT TOP 10 
    s.StateName,
    s.Region,
    SUM(f.EstimatedRevenue) AS TotalEstimatedRevenue,
    ROUND(SUM(f.EstimatedRevenue) / NULLIF(SUM(f.VisitorCount), 0), 2) AS RevenuePerVisitor
FROM dbo.DimStates s
JOIN dbo.FactTourismVisits f ON s.StateID = f.StateID
GROUP BY s.StateName, s.Region
ORDER BY TotalEstimatedRevenue DESC;
GO

-- ----------------------------------------------------------------------------
-- Query 3: Top 20 Most Popular Tourist Attractions in India
-- ----------------------------------------------------------------------------
SELECT TOP 20 
    a.AttractionName,
    c.CityName,
    s.StateName,
    t.AttractionTypeName,
    a.UNESCOStatus,
    ROUND(AVG(f.PopularityScore), 2) AS AvgPopularityScore,
    SUM(f.VisitorCount) AS TotalVisitors,
    ROUND(AVG(f.AverageRating), 2) AS AvgRating
FROM dbo.DimAttractions a
JOIN dbo.DimCities c ON a.CityID = c.CityID
JOIN dbo.DimStates s ON c.StateID = s.StateID
JOIN dbo.DimAttractionTypes t ON a.AttractionTypeID = t.AttractionTypeID
JOIN dbo.FactTourismVisits f ON a.AttractionID = f.AttractionID
GROUP BY a.AttractionName, c.CityName, s.StateName, t.AttractionTypeName, a.UNESCOStatus
ORDER BY AvgPopularityScore DESC, TotalVisitors DESC;
GO

-- ----------------------------------------------------------------------------
-- Query 4: Most Popular Attraction Categories by Visitor Footfall
-- ----------------------------------------------------------------------------
SELECT 
    t.AttractionTypeName,
    t.CategoryGroup,
    COUNT(DISTINCT a.AttractionID) AS AttractionCount,
    SUM(f.VisitorCount) AS TotalVisitors,
    SUM(f.EstimatedRevenue) AS CategoryRevenue
FROM dbo.DimAttractionTypes t
JOIN dbo.DimAttractions a ON t.AttractionTypeID = a.AttractionTypeID
JOIN dbo.FactTourismVisits f ON a.AttractionID = f.AttractionID
GROUP BY t.AttractionTypeName, t.CategoryGroup
ORDER BY TotalVisitors DESC;
GO

-- ----------------------------------------------------------------------------
-- Query 5: Average Tourism Rating by State (Ranked Highest to Lowest)
-- ----------------------------------------------------------------------------
SELECT 
    s.StateName,
    s.Region,
    ROUND(AVG(f.AverageRating), 2) AS AvgStateRating,
    SUM(f.VisitorCount) AS TotalVisitors
FROM dbo.DimStates s
JOIN dbo.FactTourismVisits f ON s.StateID = f.StateID
GROUP BY s.StateName, s.Region
ORDER BY AvgStateRating DESC;
GO

-- ----------------------------------------------------------------------------
-- Query 6: Highest-Rated Tourist Attractions (Rating >= 4.5)
-- ----------------------------------------------------------------------------
SELECT 
    a.AttractionName,
    s.StateName,
    t.AttractionTypeName,
    a.UNESCOStatus,
    ROUND(AVG(f.AverageRating), 2) AS AvgRating,
    SUM(f.VisitorCount) AS TotalVisitors
FROM dbo.DimAttractions a
JOIN dbo.DimCities c ON a.CityID = c.CityID
JOIN dbo.DimStates s ON c.StateID = s.StateID
JOIN dbo.DimAttractionTypes t ON a.AttractionTypeID = t.AttractionTypeID
JOIN dbo.FactTourismVisits f ON a.AttractionID = f.AttractionID
GROUP BY a.AttractionName, s.StateName, t.AttractionTypeName, a.UNESCOStatus
HAVING AVG(f.AverageRating) >= 4.50
ORDER BY AvgRating DESC, TotalVisitors DESC;
GO

-- ----------------------------------------------------------------------------
-- Query 7: State-Wise Domestic Visitor Volume Analysis
-- ----------------------------------------------------------------------------
SELECT 
    s.StateName,
    s.Region,
    SUM(f.DomesticVisitors) AS TotalDomesticVisitors,
    ROUND(CAST(SUM(f.DomesticVisitors) AS FLOAT) / NULLIF(SUM(f.VisitorCount), 0) * 100, 2) AS DomesticSharePct
FROM dbo.DimStates s
JOIN dbo.FactTourismVisits f ON s.StateID = f.StateID
GROUP BY s.StateName, s.Region
ORDER BY TotalDomesticVisitors DESC;
GO

-- ----------------------------------------------------------------------------
-- Query 8: State-Wise International Visitor Volume & Percentage Share
-- ----------------------------------------------------------------------------
SELECT 
    s.StateName,
    s.Region,
    SUM(f.InternationalVisitors) AS TotalInternationalVisitors,
    ROUND(CAST(SUM(f.InternationalVisitors) AS FLOAT) / NULLIF(SUM(f.VisitorCount), 0) * 100, 2) AS InternationalSharePct
FROM dbo.DimStates s
JOIN dbo.FactTourismVisits f ON s.StateID = f.StateID
GROUP BY s.StateName, s.Region
ORDER BY TotalInternationalVisitors DESC;
GO

-- ----------------------------------------------------------------------------
-- Query 9: Peak vs Off-Peak Season Tourism Performance
-- ----------------------------------------------------------------------------
SELECT 
    CASE WHEN f.IsPeakSeason = 1 THEN 'Peak Season' ELSE 'Off-Peak Season' END AS SeasonCategory,
    COUNT(f.TourismVisitID) AS ObservationCount,
    SUM(f.VisitorCount) AS TotalVisitors,
    SUM(f.EstimatedRevenue) AS TotalRevenue,
    ROUND(AVG(f.AverageStayDuration), 2) AS AvgStayDurationDays
FROM dbo.FactTourismVisits f
GROUP BY f.IsPeakSeason;
GO

-- ----------------------------------------------------------------------------
-- Query 10: Total Tourism Revenue by Category Group
-- ----------------------------------------------------------------------------
SELECT 
    t.CategoryGroup,
    COUNT(DISTINCT a.AttractionID) AS TotalAttractions,
    SUM(f.VisitorCount) AS TotalVisitors,
    SUM(f.EstimatedRevenue) AS TotalCategoryGroupRevenue,
    ROUND(AVG(f.EntryFee), 2) AS AvgEntryFee
FROM dbo.DimAttractionTypes t
JOIN dbo.DimAttractions a ON t.AttractionTypeID = a.AttractionTypeID
JOIN dbo.FactTourismVisits f ON a.AttractionID = f.AttractionID
GROUP BY t.CategoryGroup
ORDER BY TotalCategoryGroupRevenue DESC;
GO

-- ----------------------------------------------------------------------------
-- Query 11: Average Entry Fee by Attraction Category
-- ----------------------------------------------------------------------------
SELECT 
    t.AttractionTypeName,
    t.CategoryGroup,
    ROUND(AVG(f.EntryFee), 2) AS AvgEntryFee,
    MIN(f.EntryFee) AS MinEntryFee,
    MAX(f.EntryFee) AS MaxEntryFee
FROM dbo.DimAttractionTypes t
JOIN dbo.DimAttractions a ON t.AttractionTypeID = a.AttractionTypeID
JOIN dbo.FactTourismVisits f ON a.AttractionID = f.AttractionID
GROUP BY t.AttractionTypeName, t.CategoryGroup
ORDER BY AvgEntryFee DESC;
GO

-- ----------------------------------------------------------------------------
-- Query 12: UNESCO World Heritage Attractions Breakdown by State
-- ----------------------------------------------------------------------------
SELECT 
    s.StateName,
    COUNT(DISTINCT a.AttractionID) AS UNESCOAttractionsCount,
    SUM(f.VisitorCount) AS UNESCOVisitors,
    SUM(f.InternationalVisitors) AS UNESCOIntlVisitors,
    SUM(f.EstimatedRevenue) AS UNESCORevenue
FROM dbo.DimStates s
JOIN dbo.DimCities c ON s.StateID = c.StateID
JOIN dbo.DimAttractions a ON c.CityID = a.CityID
JOIN dbo.FactTourismVisits f ON a.AttractionID = f.AttractionID
WHERE a.UNESCOStatus = 'UNESCO World Heritage'
GROUP BY s.StateName
ORDER BY UNESCOVisitors DESC;
GO

-- ----------------------------------------------------------------------------
-- Query 13: Attractions with Highest Popularity Scores (> 75.0)
-- ----------------------------------------------------------------------------
SELECT 
    a.AttractionName,
    s.StateName,
    t.AttractionTypeName,
    ROUND(AVG(f.PopularityScore), 2) AS AvgPopularityScore,
    SUM(f.VisitorCount) AS TotalVisitors,
    ROUND(AVG(f.AverageRating), 2) AS AvgRating
FROM dbo.DimAttractions a
JOIN dbo.DimCities c ON a.CityID = c.CityID
JOIN dbo.DimStates s ON c.StateID = s.StateID
JOIN dbo.DimAttractionTypes t ON a.AttractionTypeID = t.AttractionTypeID
JOIN dbo.FactTourismVisits f ON a.AttractionID = f.AttractionID
GROUP BY a.AttractionName, s.StateName, t.AttractionTypeName
HAVING AVG(f.PopularityScore) >= 75.0
ORDER BY AvgPopularityScore DESC;
GO

-- ----------------------------------------------------------------------------
-- Query 14: Visitor Distribution by Indian Region
-- ----------------------------------------------------------------------------
SELECT 
    s.Region,
    COUNT(DISTINCT s.StateID) AS StatesInRegion,
    SUM(f.VisitorCount) AS TotalVisitors,
    SUM(f.DomesticVisitors) AS TotalDomestic,
    SUM(f.InternationalVisitors) AS TotalInternational,
    SUM(f.EstimatedRevenue) AS RegionRevenue
FROM dbo.DimStates s
JOIN dbo.FactTourismVisits f ON s.StateID = f.StateID
GROUP BY s.Region
ORDER BY TotalVisitors DESC;
GO

-- ----------------------------------------------------------------------------
-- Query 15: Top 10 Attractions Generating Highest Estimated Revenue
-- ----------------------------------------------------------------------------
SELECT TOP 10 
    a.AttractionName,
    s.StateName,
    t.AttractionTypeName,
    a.UNESCOStatus,
    SUM(f.EstimatedRevenue) AS TotalRevenue,
    SUM(f.VisitorCount) AS TotalVisitors,
    ROUND(SUM(f.EstimatedRevenue) / NULLIF(SUM(f.VisitorCount), 0), 2) AS RevenueYieldPerVisitor
FROM dbo.DimAttractions a
JOIN dbo.DimCities c ON a.CityID = c.CityID
JOIN dbo.DimStates s ON c.StateID = s.StateID
JOIN dbo.DimAttractionTypes t ON a.AttractionTypeID = t.AttractionTypeID
JOIN dbo.FactTourismVisits f ON a.AttractionID = f.AttractionID
GROUP BY a.AttractionName, s.StateName, t.AttractionTypeName, a.UNESCOStatus
ORDER BY TotalRevenue DESC;
GO

PRINT '15 T-SQL Analytical Queries successfully defined.';
GO
