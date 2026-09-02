"""
============================================================================
Project 2: India Tourist Attractions & Tourism Analytics System
Script: 02_Program/validate_tourism_data.py
Purpose: Empirical Data Quality Validation Suite executing 10 diagnostic tests
         against IndiaTourismAnalyticsDB and printing PASS / FAIL status.
============================================================================
"""

import os
import sys
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "01_Database" / "IndiaTourismAnalyticsDB.db"

VALID_STATES_UTS = {
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
    "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
    "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
    "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
    "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu",
    "Delhi", "Jammu and Kashmir", "Ladakh", "Lakshadweep", "Puducherry"
}


def run_data_validation():
    """Executes 10 comprehensive data quality verification tests."""
    if not DB_PATH.exists():
        print(f"Error: Database file not found at {DB_PATH}. Run load_tourism_data_to_sqlserver.py first.")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print("======================================================================")
    print("      INDIA TOURISM ANALYTICS SYSTEM - DATA QUALITY AUDIT REPORT      ")
    print("======================================================================")
    print(f"Database Target: {DB_PATH.name}\n")

    test_results = []

    # -------------------------------------------------------------------------
    # Test 1: Record Count Check
    # -------------------------------------------------------------------------
    cursor.execute("SELECT COUNT(*) FROM FactTourismVisits;")
    fact_count = cursor.fetchone()[0]
    t1_status = "PASS" if fact_count >= 30000 else "FAIL"
    test_results.append(("Test 1: Target Record Count Check (Target >= 30,000)", t1_status, f"Actual count: {fact_count:,} records"))

    # -------------------------------------------------------------------------
    # Test 2: Null Primary Keys Check
    # -------------------------------------------------------------------------
    cursor.execute("""
        SELECT COUNT(*) FROM FactTourismVisits WHERE TourismVisitID IS NULL
        UNION ALL SELECT COUNT(*) FROM DimStates WHERE StateID IS NULL
        UNION ALL SELECT COUNT(*) FROM DimAttractions WHERE AttractionID IS NULL;
    """)
    null_pks = sum([r[0] for r in cursor.fetchall()])
    t2_status = "PASS" if null_pks == 0 else "FAIL"
    test_results.append(("Test 2: Null Primary Keys Check", t2_status, f"Found {null_pks} null primary key entries"))

    # -------------------------------------------------------------------------
    # Test 3: Duplicate Primary Keys Check
    # -------------------------------------------------------------------------
    cursor.execute("""
        SELECT COUNT(TourismVisitID) - COUNT(DISTINCT TourismVisitID) FROM FactTourismVisits;
    """)
    dup_pks = cursor.fetchone()[0]
    t3_status = "PASS" if dup_pks == 0 else "FAIL"
    test_results.append(("Test 3: Duplicate Primary Keys Check", t3_status, f"Found {dup_pks} duplicate primary key entries"))

    # -------------------------------------------------------------------------
    # Test 4: Orphan Foreign Keys Check
    # -------------------------------------------------------------------------
    cursor.execute("""
        SELECT COUNT(*) FROM FactTourismVisits f
        LEFT JOIN DimAttractions a ON f.AttractionID = a.AttractionID
        LEFT JOIN DimStates s ON f.StateID = s.StateID
        LEFT JOIN DimCities c ON f.CityID = c.CityID
        LEFT JOIN DimDates d ON f.DateKey = d.DateKey
        LEFT JOIN DimVisitorSegments seg ON f.VisitorSegmentID = seg.VisitorSegmentID
        WHERE a.AttractionID IS NULL 
           OR s.StateID IS NULL 
           OR c.CityID IS NULL 
           OR d.DateKey IS NULL 
           OR seg.VisitorSegmentID IS NULL;
    """)
    orphan_fks = cursor.fetchone()[0]
    t4_status = "PASS" if orphan_fks == 0 else "FAIL"
    test_results.append(("Test 4: Orphan Foreign Keys Integrity Check", t4_status, f"Found {orphan_fks} orphan foreign key records"))

    # -------------------------------------------------------------------------
    # Test 5: Invalid States Standardization Check
    # -------------------------------------------------------------------------
    cursor.execute("SELECT DISTINCT StateName FROM DimStates;")
    db_states = set([r[0] for r in cursor.fetchall()])
    invalid_states = db_states - VALID_STATES_UTS
    t5_status = "PASS" if len(invalid_states) == 0 else "FAIL"
    test_results.append(("Test 5: State & UT Name Standardization Check", t5_status, f"Invalid state names found: {list(invalid_states)}"))

    # -------------------------------------------------------------------------
    # Test 6: Invalid Visitor Counts Check (VisitorCount < 0)
    # -------------------------------------------------------------------------
    cursor.execute("""
        SELECT COUNT(*) FROM FactTourismVisits 
        WHERE VisitorCount < 0 OR DomesticVisitors < 0 OR InternationalVisitors < 0;
    """)
    invalid_visitors = cursor.fetchone()[0]
    t6_status = "PASS" if invalid_visitors == 0 else "FAIL"
    test_results.append(("Test 6: Non-Negative Visitor Counts Check", t6_status, f"Found {invalid_visitors} invalid negative visitor entries"))

    # -------------------------------------------------------------------------
    # Test 7: Invalid Ratings Check (0.0 <= Rating <= 5.0)
    # -------------------------------------------------------------------------
    cursor.execute("""
        SELECT COUNT(*) FROM FactTourismVisits 
        WHERE AverageRating < 0.0 OR AverageRating > 5.0;
    """)
    invalid_ratings = cursor.fetchone()[0]
    t7_status = "PASS" if invalid_ratings == 0 else "FAIL"
    test_results.append(("Test 7: Rating Bounds Check (0.0 to 5.0)", t7_status, f"Found {invalid_ratings} rating out-of-bounds records"))

    # -------------------------------------------------------------------------
    # Test 8: Invalid Geographic Coordinates Check (Lat 8-38, Lon 68-98)
    # -------------------------------------------------------------------------
    cursor.execute("""
        SELECT COUNT(*) FROM DimCities 
        WHERE Latitude < 6.0 OR Latitude > 38.0 OR Longitude < 68.0 OR Longitude > 98.0;
    """)
    invalid_coords = cursor.fetchone()[0]
    t8_status = "PASS" if invalid_coords == 0 else "FAIL"
    test_results.append(("Test 8: Geographic Coordinates Bounds Check (India)", t8_status, f"Found {invalid_coords} out-of-bounds coordinates"))

    # -------------------------------------------------------------------------
    # Test 9: Negative Estimated Revenue Check
    # -------------------------------------------------------------------------
    cursor.execute("SELECT COUNT(*) FROM FactTourismVisits WHERE EstimatedRevenue < 0.0;")
    invalid_rev = cursor.fetchone()[0]
    t9_status = "PASS" if invalid_rev == 0 else "FAIL"
    test_results.append(("Test 9: Non-Negative Tourism Revenue Check", t9_status, f"Found {invalid_rev} negative revenue records"))

    # -------------------------------------------------------------------------
    # Test 10: Negative Entry Fees Check
    # -------------------------------------------------------------------------
    cursor.execute("SELECT COUNT(*) FROM DimAttractions WHERE EntryFee < 0.0;")
    invalid_fees = cursor.fetchone()[0]
    t10_status = "PASS" if invalid_fees == 0 else "FAIL"
    test_results.append(("Test 10: Non-Negative Entry Fee Check", t10_status, f"Found {invalid_fees} negative entry fee records"))

    # Print summary result table
    all_passed = True
    for test_name, status, detail in test_results:
        flag = "[ PASS ]" if status == "PASS" else "[ FAIL ]"
        if status != "PASS":
            all_passed = False
        print(f"{flag} {test_name:<60} | {detail}")

    print("----------------------------------------------------------------------")
    final_verdict = "PASS - ALL DATA QUALITY CHECKS SATISFIED 100%" if all_passed else "FAIL - AUDIT DISCREPANCIES DETECTED"
    print(f"OVERALL AUDIT VERDICT: {final_verdict}")
    print("======================================================================\n")

    conn.close()
    return all_passed


if __name__ == "__main__":
    run_data_validation()
