-- ============================================================================
-- Project 2: India Tourist Attractions & Tourism Analytics System
-- Script: 04_TourismDB_Views.sql
-- Database: IndiaTourismAnalyticsDB
-- Purpose: Creates 7 comprehensive analytical T-SQL views for reporting & BI
-- ============================================================================

USE IndiaTourismAnalyticsDB;
GO

-- ----------------------------------------------------------------------------
-- 1. vw_StateTourismPerformance
-- Summarizes overall visitor volume, revenue, ratings, and visitor splits by State
-- ----------------------------------------------------------------------------
CREATE OR ALTER VIEW dbo.vw_StateTourismPerformance AS
SELECT 
    s.StateID,
    s.StateName,
    s.StateType,
    s.Region,
    s.Capital,
    COUNT(f.TourismVisitID) AS TotalVisitRecords,
    SUM(f.VisitorCount) AS TotalVisitors,
    SUM(f.DomesticVisitors) AS TotalDomesticVisitors,
    SUM(f.InternationalVisitors) AS TotalInternationalVisitors,
    ROUND(CAST(SUM(f.InternationalVisitors) AS FLOAT) / NULLIF(SUM(f.VisitorCount), 0) * 100, 2) AS InternationalVisitorPct,
    ROUND(AVG(f.AverageRating), 2) AS AvgStateRating,
    SUM(f.EstimatedRevenue) AS TotalEstimatedRevenue,
    ROUND(AVG(f.PopularityScore), 2) AS AvgPopularityScore
FROM dbo.DimStates s
JOIN dbo.FactTourismVisits f ON s.StateID = f.StateID
GROUP BY s.StateID, s.StateName, s.StateType, s.Region, s.Capital;
GO

-- ----------------------------------------------------------------------------
-- 2. vw_AttractionPerformance
-- Summarizes performance metrics per tourist attraction
-- ----------------------------------------------------------------------------
CREATE OR ALTER VIEW dbo.vw_AttractionPerformance AS
SELECT 
    a.AttractionID,
    a.AttractionName,
    c.CityName,
    s.StateName,
    s.Region,
    t.AttractionTypeName,
    t.CategoryGroup,
    a.UNESCOStatus,
    a.HistoricalImportance,
    a.BestSeason,
    a.EntryFee AS PublishedEntryFee,
    SUM(f.VisitorCount) AS TotalVisitors,
    SUM(f.DomesticVisitors) AS TotalDomesticVisitors,
    SUM(f.InternationalVisitors) AS TotalInternationalVisitors,
    ROUND(AVG(f.AverageRating), 2) AS AvgRating,
    ROUND(AVG(f.PopularityScore), 2) AS AvgPopularityScore,
    ROUND(AVG(f.AverageStayDuration), 2) AS AvgStayDurationDays,
    SUM(f.EstimatedRevenue) AS TotalEstimatedRevenue
FROM dbo.DimAttractions a
JOIN dbo.DimCities c ON a.CityID = c.CityID
JOIN dbo.DimStates s ON c.StateID = s.StateID
JOIN dbo.DimAttractionTypes t ON a.AttractionTypeID = t.AttractionTypeID
JOIN dbo.FactTourismVisits f ON a.AttractionID = f.AttractionID
GROUP BY a.AttractionID, a.AttractionName, c.CityName, s.StateName, s.Region, 
         t.AttractionTypeName, t.CategoryGroup, a.UNESCOStatus, a.HistoricalImportance, 
         a.BestSeason, a.EntryFee;
GO

-- ----------------------------------------------------------------------------
-- 3. vw_CategoryPerformance
-- Analyzes tourism performance grouped by attraction category and category group
-- ----------------------------------------------------------------------------
CREATE OR ALTER VIEW dbo.vw_CategoryPerformance AS
SELECT 
    t.AttractionTypeID,
    t.AttractionTypeName,
    t.CategoryGroup,
    COUNT(DISTINCT a.AttractionID) AS TotalAttractionsCount,
    SUM(f.VisitorCount) AS TotalVisitors,
    SUM(f.DomesticVisitors) AS TotalDomesticVisitors,
    SUM(f.InternationalVisitors) AS TotalInternationalVisitors,
    ROUND(AVG(f.AverageRating), 2) AS AvgCategoryRating,
    ROUND(AVG(f.EntryFee), 2) AS AvgEntryFee,
    SUM(f.EstimatedRevenue) AS TotalCategoryRevenue,
    ROUND(SUM(f.EstimatedRevenue) / NULLIF(SUM(f.VisitorCount), 0), 2) AS RevenuePerVisitor
FROM dbo.DimAttractionTypes t
JOIN dbo.DimAttractions a ON t.AttractionTypeID = a.AttractionTypeID
JOIN dbo.FactTourismVisits f ON a.AttractionID = f.AttractionID
GROUP BY t.AttractionTypeID, t.AttractionTypeName, t.CategoryGroup;
GO

-- ----------------------------------------------------------------------------
-- 4. vw_VisitorAnalytics
-- Evaluates demographic patterns across Visitor Segments
-- ----------------------------------------------------------------------------
CREATE OR ALTER VIEW dbo.vw_VisitorAnalytics AS
SELECT 
    seg.VisitorSegmentID,
    seg.SegmentName,
    COUNT(f.TourismVisitID) AS ObservationCount,
    SUM(f.VisitorCount) AS TotalVisitors,
    SUM(f.DomesticVisitors) AS TotalDomesticVisitors,
    SUM(f.InternationalVisitors) AS TotalInternationalVisitors,
    ROUND(AVG(f.AverageStayDuration), 2) AS AvgStayDurationDays,
    ROUND(AVG(f.AverageRating), 2) AS AvgSegmentRating,
    SUM(f.EstimatedRevenue) AS TotalSegmentRevenue
FROM dbo.DimVisitorSegments seg
JOIN dbo.FactTourismVisits f ON seg.VisitorSegmentID = f.VisitorSegmentID
GROUP BY seg.VisitorSegmentID, seg.SegmentName;
GO

-- ----------------------------------------------------------------------------
-- 5. vw_SeasonalTourism
-- Aggregates monthly and seasonal tourism dynamics
-- ----------------------------------------------------------------------------
CREATE OR ALTER VIEW dbo.vw_SeasonalTourism AS
SELECT 
    d.Year,
    d.Quarter,
    d.Month,
    d.MonthName,
    d.Season,
    SUM(f.VisitorCount) AS TotalVisitors,
    SUM(f.DomesticVisitors) AS TotalDomesticVisitors,
    SUM(f.InternationalVisitors) AS TotalInternationalVisitors,
    SUM(CASE WHEN f.IsPeakSeason = 1 THEN f.VisitorCount ELSE 0 END) AS PeakSeasonVisitors,
    SUM(f.EstimatedRevenue) AS MonthlyRevenue,
    ROUND(AVG(f.PopularityScore), 2) AS AvgMonthlyPopularity
FROM dbo.DimDates d
JOIN dbo.FactTourismVisits f ON d.DateKey = f.DateKey
GROUP BY d.Year, d.Quarter, d.Month, d.MonthName, d.Season;
GO

-- ----------------------------------------------------------------------------
-- 6. vw_RevenueAnalysis
-- Financial breakdown by UNESCO status and high-value destinations
-- ----------------------------------------------------------------------------
CREATE OR ALTER VIEW dbo.vw_RevenueAnalysis AS
SELECT 
    a.UNESCOStatus,
    COUNT(DISTINCT a.AttractionID) AS TotalAttractions,
    SUM(f.VisitorCount) AS TotalVisitors,
    SUM(f.EstimatedRevenue) AS TotalEstimatedRevenue,
    ROUND(AVG(f.EntryFee), 2) AS AvgEntryFee,
    ROUND(SUM(f.EstimatedRevenue) / NULLIF(SUM(f.VisitorCount), 0), 2) AS RevenueYieldPerVisitor,
    ROUND(AVG(f.PopularityScore), 2) AS AvgPopularityScore
FROM dbo.DimAttractions a
JOIN dbo.FactTourismVisits f ON a.AttractionID = f.AttractionID
GROUP BY a.UNESCOStatus;
GO

-- ----------------------------------------------------------------------------
-- 7. vw_GeographicTourism
-- Zonal breakdown across Indian macro-regions
-- ----------------------------------------------------------------------------
CREATE OR ALTER VIEW dbo.vw_GeographicTourism AS
SELECT 
    s.Region,
    COUNT(DISTINCT s.StateID) AS StatesCount,
    COUNT(DISTINCT a.AttractionID) AS TotalAttractions,
    SUM(f.VisitorCount) AS TotalVisitors,
    SUM(f.DomesticVisitors) AS TotalDomesticVisitors,
    SUM(f.InternationalVisitors) AS TotalInternationalVisitors,
    SUM(f.EstimatedRevenue) AS TotalRegionRevenue,
    ROUND(AVG(f.AverageRating), 2) AS AvgRegionRating
FROM dbo.DimStates s
JOIN dbo.FactTourismVisits f ON s.StateID = f.StateID
JOIN dbo.DimAttractions a ON f.AttractionID = a.AttractionID
GROUP BY s.Region;
GO

PRINT '7 Analytical T-SQL Views created successfully.';
GO
