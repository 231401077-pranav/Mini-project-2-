-- ============================================================================
-- Project 2: India Tourist Attractions & Tourism Analytics System
-- Script: 01_TourismDB_Create.sql
-- Database: IndiaTourismAnalyticsDB
-- Purpose: Creates the primary SQL Server database for tourism analytics
-- ============================================================================

USE master;
GO

IF EXISTS (SELECT name FROM sys.databases WHERE name = N'IndiaTourismAnalyticsDB')
BEGIN
    ALTER DATABASE IndiaTourismAnalyticsDB SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE IndiaTourismAnalyticsDB;
END;
GO

CREATE DATABASE IndiaTourismAnalyticsDB
COLLATE Latin1_General_100_CI_AS_SC_UTF8;
GO

ALTER DATABASE IndiaTourismAnalyticsDB SET RECOVERY SIMPLE;
GO

USE IndiaTourismAnalyticsDB;
GO

PRINT 'Database IndiaTourismAnalyticsDB successfully created.';
GO
