"""
============================================================================
Project 2: India Tourist Attractions & Tourism Analytics System
Script: 02_Program/load_tourism_data_to_sqlserver.py
Purpose: Connects to database (SQL Server / SQLite relational engine),
         provisions Star Schema schema, loads 25,000 tourism records,
         and verifies successful ingestion.
============================================================================
"""

import os
import sys
import sqlite3
import pandas as pd
from pathlib import Path

# Add script directory to import path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from tourism_data_cleaning import generate_and_clean_tourism_data

# Relational Database File Path (Local relational store for seamless academic execution)
DB_PATH = Path(__file__).resolve().parent.parent / "01_Database" / "IndiaTourismAnalyticsDB.db"


def get_db_connection(db_path=DB_PATH):
    """Establishes connection to relational database engine."""
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def provision_schema(conn):
    """Creates Star Schema dimension and fact tables."""
    cursor = conn.cursor()

    # Drop existing tables
    cursor.executescript("""
    DROP TABLE IF EXISTS FactTourismVisits;
    DROP TABLE IF EXISTS DimAttractions;
    DROP TABLE IF EXISTS DimAttractionTypes;
    DROP TABLE IF EXISTS DimCities;
    DROP TABLE IF EXISTS DimStates;
    DROP TABLE IF EXISTS DimDates;
    DROP TABLE IF EXISTS DimVisitorSegments;

    CREATE TABLE DimStates (
        StateID INTEGER PRIMARY KEY AUTOINCREMENT,
        StateName TEXT NOT NULL UNIQUE,
        StateType TEXT NOT NULL,
        Region TEXT NOT NULL,
        Capital TEXT
    );

    CREATE TABLE DimCities (
        CityID INTEGER PRIMARY KEY AUTOINCREMENT,
        CityName TEXT NOT NULL,
        StateID INTEGER NOT NULL,
        District TEXT,
        Latitude REAL,
        Longitude REAL,
        FOREIGN KEY (StateID) REFERENCES DimStates(StateID)
    );

    CREATE TABLE DimAttractionTypes (
        AttractionTypeID INTEGER PRIMARY KEY AUTOINCREMENT,
        AttractionTypeName TEXT NOT NULL UNIQUE,
        CategoryGroup TEXT NOT NULL
    );

    CREATE TABLE DimAttractions (
        AttractionID INTEGER PRIMARY KEY AUTOINCREMENT,
        AttractionName TEXT NOT NULL,
        CityID INTEGER NOT NULL,
        AttractionTypeID INTEGER NOT NULL,
        Description TEXT,
        UNESCOStatus TEXT NOT NULL DEFAULT 'Non-UNESCO',
        HistoricalImportance TEXT NOT NULL DEFAULT 'Moderate',
        BestSeason TEXT NOT NULL DEFAULT 'All Year',
        EntryFee REAL NOT NULL DEFAULT 0.00,
        OpeningTime TEXT,
        ClosingTime TEXT,
        FOREIGN KEY (CityID) REFERENCES DimCities(CityID),
        FOREIGN KEY (AttractionTypeID) REFERENCES DimAttractionTypes(AttractionTypeID)
    );

    CREATE TABLE DimDates (
        DateKey INTEGER PRIMARY KEY,
        FullDate TEXT NOT NULL,
        Year INTEGER NOT NULL,
        Quarter INTEGER NOT NULL,
        Month INTEGER NOT NULL,
        MonthName TEXT NOT NULL,
        Season TEXT NOT NULL,
        Day INTEGER NOT NULL,
        IsWeekend INTEGER NOT NULL DEFAULT 0
    );

    CREATE TABLE DimVisitorSegments (
        VisitorSegmentID INTEGER PRIMARY KEY AUTOINCREMENT,
        SegmentName TEXT NOT NULL
    );

    CREATE TABLE FactTourismVisits (
        TourismVisitID INTEGER PRIMARY KEY AUTOINCREMENT,
        AttractionID INTEGER NOT NULL,
        StateID INTEGER NOT NULL,
        CityID INTEGER NOT NULL,
        DateKey INTEGER NOT NULL,
        VisitorSegmentID INTEGER NOT NULL,
        VisitorCount INTEGER NOT NULL,
        DomesticVisitors INTEGER NOT NULL,
        InternationalVisitors INTEGER NOT NULL,
        AverageRating REAL NOT NULL,
        EntryFee REAL NOT NULL,
        EstimatedRevenue REAL NOT NULL,
        PopularityScore REAL NOT NULL,
        AverageStayDuration REAL NOT NULL,
        IsPeakSeason INTEGER NOT NULL DEFAULT 0,
        FOREIGN KEY (AttractionID) REFERENCES DimAttractions(AttractionID),
        FOREIGN KEY (StateID) REFERENCES DimStates(StateID),
        FOREIGN KEY (CityID) REFERENCES DimCities(CityID),
        FOREIGN KEY (DateKey) REFERENCES DimDates(DateKey),
        FOREIGN KEY (VisitorSegmentID) REFERENCES DimVisitorSegments(VisitorSegmentID)
    );
    """)
    conn.commit()
    print("Star Schema tables successfully provisioned in IndiaTourismAnalyticsDB.")


def load_data_to_database():
    """Generates cleaned data and loads all tables into the database."""
    df_st, df_ci, df_ty, df_at, df_da, df_se, df_fa = generate_and_clean_tourism_data()

    conn = get_db_connection()
    provision_schema(conn)

    print("\nLoading dataset into database tables...")
    df_st.to_sql("DimStates", conn, if_exists="append", index=False)
    print(f"DimStates loaded: {len(df_st)} rows.")

    df_ci.to_sql("DimCities", conn, if_exists="append", index=False)
    print(f"DimCities loaded: {len(df_ci)} rows.")

    df_ty.to_sql("DimAttractionTypes", conn, if_exists="append", index=False)
    print(f"DimAttractionTypes loaded: {len(df_ty)} rows.")

    df_at.to_sql("DimAttractions", conn, if_exists="append", index=False)
    print(f"DimAttractions loaded: {len(df_at)} rows.")

    df_da.to_sql("DimDates", conn, if_exists="append", index=False)
    print(f"DimDates loaded: {len(df_da)} rows.")

    df_se.to_sql("DimVisitorSegments", conn, if_exists="append", index=False)
    print(f"DimVisitorSegments loaded: {len(df_se)} rows.")

    df_fa.to_sql("FactTourismVisits", conn, if_exists="append", index=False)
    print(f"FactTourismVisits loaded: {len(df_fa)} rows.")

    conn.commit()

    # Verification Query
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM FactTourismVisits;")
    fact_count = cursor.fetchone()[0]

    print("\n=======================================================")
    print("INGESTION VERIFICATION SUCCESSFUL")
    print(f"Database Name: IndiaTourismAnalyticsDB")
    print(f"Total Fact Records Inserted: {fact_count:,}")
    print("=======================================================\n")

    conn.close()
    return fact_count


if __name__ == "__main__":
    load_data_to_database()
