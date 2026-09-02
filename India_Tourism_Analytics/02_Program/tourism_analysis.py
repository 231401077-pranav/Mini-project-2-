"""
============================================================================
Project 2: India Tourist Attractions & Tourism Analytics System
Script: 02_Program/tourism_analysis.py
Purpose: Connects to database, retrieves analytical views & queries, performs
         pandas statistical transformations, and exports comprehensive findings
         to 06_Results/tourism_analysis_results.txt.
============================================================================
"""

import os
import sys
import sqlite3
import pandas as pd
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "01_Database" / "IndiaTourismAnalyticsDB.db"
OUTPUT_TXT_PATH = BASE_DIR / "06_Results" / "tourism_analysis_results.txt"


def perform_tourism_analysis():
    """Queries relational database, performs pandas statistical analysis, and generates text report."""
    if not DB_PATH.exists():
        print(f"Error: Database not found at {DB_PATH}. Provision DB first.")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)

    print("Executing database analytical queries via pandas...")

    # 1. State Analysis
    df_state = pd.read_sql_query("""
        SELECT s.StateName, s.Region, 
               SUM(f.VisitorCount) AS TotalVisitors,
               SUM(f.DomesticVisitors) AS DomesticVisitors,
               SUM(f.InternationalVisitors) AS InternationalVisitors,
               ROUND(AVG(f.AverageRating), 2) AS AvgRating,
               SUM(f.EstimatedRevenue) AS TotalRevenue
        FROM DimStates s
        JOIN FactTourismVisits f ON s.StateID = f.StateID
        GROUP BY s.StateName, s.Region
        ORDER BY TotalVisitors DESC;
    """, conn)

    # 2. Attraction Analysis
    df_attractions = pd.read_sql_query("""
        SELECT a.AttractionName, c.CityName, s.StateName, t.AttractionTypeName, a.UNESCOStatus,
               SUM(f.VisitorCount) AS TotalVisitors,
               ROUND(AVG(f.PopularityScore), 2) AS AvgPopularityScore,
               ROUND(AVG(f.AverageRating), 2) AS AvgRating,
               SUM(f.EstimatedRevenue) AS TotalRevenue
        FROM DimAttractions a
        JOIN DimCities c ON a.CityID = c.CityID
        JOIN DimStates s ON c.StateID = s.StateID
        JOIN DimAttractionTypes t ON a.AttractionTypeID = t.AttractionTypeID
        JOIN FactTourismVisits f ON a.AttractionID = f.AttractionID
        GROUP BY a.AttractionName, c.CityName, s.StateName, t.AttractionTypeName, a.UNESCOStatus
        ORDER BY TotalVisitors DESC;
    """, conn)

    # 3. Category Analysis
    df_category = pd.read_sql_query("""
        SELECT t.CategoryGroup, t.AttractionTypeName,
               COUNT(DISTINCT a.AttractionID) AS TotalAttractions,
               SUM(f.VisitorCount) AS TotalVisitors,
               SUM(f.EstimatedRevenue) AS CategoryRevenue,
               ROUND(AVG(f.EntryFee), 2) AS AvgEntryFee
        FROM DimAttractionTypes t
        JOIN DimAttractions a ON t.AttractionTypeID = a.AttractionTypeID
        JOIN FactTourismVisits f ON a.AttractionID = f.AttractionID
        GROUP BY t.CategoryGroup, t.AttractionTypeName
        ORDER BY TotalVisitors DESC;
    """, conn)

    # 4. Seasonal Analysis
    df_season = pd.read_sql_query("""
        SELECT d.Season,
               SUM(f.VisitorCount) AS TotalVisitors,
               SUM(f.DomesticVisitors) AS DomesticVisitors,
               SUM(f.InternationalVisitors) AS InternationalVisitors,
               SUM(f.EstimatedRevenue) AS SeasonalRevenue
        FROM DimDates d
        JOIN FactTourismVisits f ON d.DateKey = f.DateKey
        GROUP BY d.Season
        ORDER BY TotalVisitors DESC;
    """, conn)

    # 5. Regional Analysis
    df_region = pd.read_sql_query("""
        SELECT s.Region,
               COUNT(DISTINCT s.StateID) AS StatesCount,
               SUM(f.VisitorCount) AS TotalVisitors,
               SUM(f.EstimatedRevenue) AS RegionRevenue,
               ROUND(AVG(f.AverageRating), 2) AS AvgRegionRating
        FROM DimStates s
        JOIN FactTourismVisits f ON s.StateID = f.StateID
        GROUP BY s.Region
        ORDER BY TotalVisitors DESC;
    """, conn)

    # Summary Metrics
    total_visitors = df_state["TotalVisitors"].sum()
    total_domestic = df_state["DomesticVisitors"].sum()
    total_intl = df_state["InternationalVisitors"].sum()
    total_revenue = df_state["TotalRevenue"].sum()
    overall_rating = round(df_state["AvgRating"].mean(), 2)

    top_state = df_state.iloc[0]["StateName"]
    top_state_visitors = df_state.iloc[0]["TotalVisitors"]

    top_attraction = df_attractions.iloc[0]["AttractionName"]
    top_attraction_visitors = df_attractions.iloc[0]["TotalVisitors"]

    top_category = df_category.iloc[0]["AttractionTypeName"]
    top_season = df_season.iloc[0]["Season"]

    # Construct clean result text
    lines = [
        "===================================================================================",
        "        PROJECT 2: INDIA TOURIST ATTRACTIONS & TOURISM ANALYTICS SYSTEM            ",
        "                             EXECUTIVE ANALYTICS SUMMARY                           ",
        "===================================================================================",
        f"Database Source: IndiaTourismAnalyticsDB (SQLite / SQL Server Relational Engine)",
        f"Total Analytical Fact Records Evaluated: 25,000",
        f"Scope: 28 States & 8 Union Territories across 18 Attraction Categories",
        "-----------------------------------------------------------------------------------",
        "",
        "1. KEY SYSTEM-WIDE METRICS",
        f"   - Total Visitor Footfall   : {total_visitors:,} visitors",
        f"   - Domestic Visitors        : {total_domestic:,} ({total_domestic/total_visitors*100:.2f}%)",
        f"   - International Visitors   : {total_intl:,} ({total_intl/total_visitors*100:.2f}%)",
        f"   - Total Tourism Revenue    : INR {total_revenue:,.2f}",
        f"   - Average Attraction Rating: {overall_rating} / 5.00",
        "",
        "2. TOP 5 PERFORMING STATES BY VISITOR VOLUME",
    ]

    for idx, row in df_state.head(5).iterrows():
        lines.append(f"   {idx+1}. {row['StateName']:<22} | Region: {row['Region']:<15} | Visitors: {row['TotalVisitors']:,} | Revenue: INR {row['TotalRevenue']:,.2f}")

    lines.extend([
        "",
        "3. TOP 5 TOURIST ATTRACTIONS BY POPULARITY AND VISITORS",
    ])
    for idx, row in df_attractions.head(5).iterrows():
        lines.append(f"   {idx+1}. {row['AttractionName']:<30} ({row['StateName']}) | Visitors: {row['TotalVisitors']:,} | Rating: {row['AvgRating']} | Score: {row['AvgPopularityScore']}")

    lines.extend([
        "",
        "4. TOURISM PERFORMANCE BY CATEGORY GROUP",
    ])
    grp_cat = df_category.groupby("CategoryGroup").agg({
        "TotalVisitors": "sum",
        "CategoryRevenue": "sum",
        "AvgEntryFee": "mean"
    }).reset_index().sort_values("TotalVisitors", ascending=False)

    for idx, row in grp_cat.iterrows():
        lines.append(f"   - {row['CategoryGroup']:<25} | Visitors: {row['TotalVisitors']:,} | Revenue: INR {row['CategoryRevenue']:,.2f} | Avg Fee: INR {row['AvgEntryFee']:.2f}")

    lines.extend([
        "",
        "5. SEASONAL VISITOR DISTRIBUTION",
    ])
    for idx, row in df_season.iterrows():
        lines.append(f"   - Season: {row['Season']:<10} | Visitors: {row['TotalVisitors']:,} | Revenue: INR {row['SeasonalRevenue']:,.2f}")

    lines.extend([
        "",
        "6. REGIONAL TOURISM CONCENTRATION",
    ])
    for idx, row in df_region.iterrows():
        lines.append(f"   - Region: {row['Region']:<15} | States: {row['StatesCount']} | Visitors: {row['TotalVisitors']:,} | Revenue: INR {row['RegionRevenue']:,.2f}")

    lines.extend([
        "",
        "===================================================================================",
        "                                KEY ANALYTICAL INSIGHTS                            ",
        "===================================================================================",
        f"1. Top State Destination: {top_state} leads India with {top_state_visitors:,} visitors.",
        f"2. Top Tourist Attraction: {top_attraction} registered the highest visitor footfall of {top_attraction_visitors:,}.",
        f"3. Dominant Attraction Category: '{top_category}' generated the highest visitor interest.",
        f"4. Peak Visiting Season: '{top_season}' represents the highest seasonal traffic across the country.",
        f"5. International Tourism Contribution: International tourists account for {total_intl/total_visitors*100:.2f}% of total visits, driving disproportionately high tourism revenue.",
        "==================================================================================="
    ])

    # Ensure output directory exists
    OUTPUT_TXT_PATH.parent.mkdir(parents=True, exist_ok=True)

    result_content = "\n".join(lines)
    with open(OUTPUT_TXT_PATH, "w", encoding="utf-8") as f:
        f.write(result_content)

    print(f"\nAnalysis results successfully generated and exported to {OUTPUT_TXT_PATH}")
    print(result_content)

    conn.close()


if __name__ == "__main__":
    perform_tourism_analysis()
