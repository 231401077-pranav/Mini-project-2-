"""
============================================================================
Project 2: India Tourist Attractions & Tourism Analytics System
Script: audit_project2.py
Purpose: Comprehensive Faculty Compliance Audit verifying all prompt checklist
         requirements and reporting PASS / FAIL for each rule.
============================================================================
"""

import os
import sys
import sqlite3
from pathlib import Path
from docx import Document

BASE_DIR = Path(__file__).resolve().parent / "India_Tourism_Analytics"
DB_PATH = BASE_DIR / "01_Database" / "IndiaTourismAnalyticsDB.db"
DOCX_PATH = BASE_DIR / "05_Documentation" / "India_Tourism_Analytics_Project_Report.docx"
HTML_PATH = BASE_DIR / "03_PowerBI" / "India_Tourism_Analytics_Dashboard.html"
README_PATH = BASE_DIR / "README.md"


def run_compliance_audit():
    print("======================================================================")
    print("       PROJECT 2: INDIA TOURISM ANALYTICS - FACULTY AUDIT SUITE       ")
    print("======================================================================")
    print(f"Target Directory: {BASE_DIR}\n")

    audit_checks = []

    # 1. Project 2 Folder Existence
    c1 = BASE_DIR.exists() and BASE_DIR.is_dir()
    audit_checks.append(("1. Independent Project 2 Directory Exists", "PASS" if c1 else "FAIL", str(BASE_DIR)))

    # 2. Check Absence of Project 1 / Financial Analytics / Hotel References
    forbidden_terms = ["Financial_Analytics", "Project 1", "Hotel Booking", "hotel_booking"]
    found_forbidden = False
    for root, dirs, files in os.walk(BASE_DIR):
        for f in files:
            if f.endswith(('.py', '.sql', '.md', '.dax', '.txt', '.html')):
                filepath = Path(root) / f
                content = filepath.read_text(encoding='utf-8', errors='ignore')
                for term in forbidden_terms:
                    if term in content:
                        found_forbidden = True
                        print(f"   [!] Forbidden reference '{term}' found in {filepath.name}")

    audit_checks.append(("2. Strict Isolation (No Project 1 / Hotel References)", "PASS" if not found_forbidden else "FAIL", "Zero legacy references detected"))

    # 3. Fact Record Count >= 20,000
    fact_count = 0
    if DB_PATH.exists():
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM FactTourismVisits;")
        fact_count = cursor.fetchone()[0]
        conn.close()
    
    c3 = fact_count >= 20000
    audit_checks.append(("3. Target Data Volume (20,000+ Fact Records)", "PASS" if c3 else "FAIL", f"Actual records: {fact_count:,}"))

    # 4. SQL Server Scripts Existence
    sql_files = [
        "01_TourismDB_Create.sql",
        "02_TourismDB_Tables.sql",
        "03_TourismDB_Insert.sql",
        "04_TourismDB_Views.sql",
        "05_TourismDB_Queries.sql"
    ]
    all_sql = all((BASE_DIR / "01_Database" / sf).exists() for sf in sql_files)
    audit_checks.append(("4. 5 SQL Database Scripts Exist (01_Database/)", "PASS" if all_sql else "FAIL", f"Verified files: {len(sql_files)}/5"))

    # 5. Python Pipeline Programs Existence
    py_files = [
        "tourism_data_cleaning.py",
        "load_tourism_data_to_sqlserver.py",
        "validate_tourism_data.py",
        "tourism_analysis.py"
    ]
    all_py = all((BASE_DIR / "02_Program" / pf).exists() for pf in py_files)
    audit_checks.append(("5. Python Data Pipeline Programs Exist (02_Program/)", "PASS" if all_py else "FAIL", f"Verified files: {len(py_files)}/4"))

    # 6. Jupyter Notebook Existence
    nb_exists = (BASE_DIR / "02_Program" / "tourism_analysis.ipynb").exists()
    audit_checks.append(("6. Jupyter Analytics Notebook Exists", "PASS" if nb_exists else "FAIL", "tourism_analysis.ipynb"))

    # 7. Power BI Files Existence
    pbi_files = ["India_Tourism_Analytics.pbix", "dax_measures.dax", "India_Tourism_Analytics_Dashboard.html"]
    all_pbi = all((BASE_DIR / "03_PowerBI" / pbf).exists() for pbf in pbi_files)
    audit_checks.append(("7. Power BI Workbook & Visual Assets Exist", "PASS" if all_pbi else "FAIL", f"PBIX, DAX, HTML verified"))

    # 8. Tableau Files Existence
    tab_files = ["India_Tourism_Analytics.twbx", "tableau_calculations.md"]
    all_tab = all((BASE_DIR / "04_Tableau" / tf).exists() for tf in tab_files)
    audit_checks.append(("8. Tableau Package & Documentation Exist", "PASS" if all_tab else "FAIL", "TWBX & MD verified"))

    # 9. Word Report Existence & 12 Headings Check
    required_headings = [
        "1. Aim", "2. Algorithm", "3. Methodology", "4. Dataset Details",
        "5. Database Design", "6. SQL Server Implementation", "7. Python Implementation",
        "8. Power BI Implementation", "9. Tableau Implementation", "10. Results",
        "11. Observations", "12. Conclusion"
    ]

    docx_ok = False
    missing_hd = []
    has_sql_explanation = False

    if DOCX_PATH.exists():
        doc = Document(DOCX_PATH)
        full_text = "\n".join([p.text for p in doc.paragraphs])
        
        for rh in required_headings:
            if rh not in full_text:
                missing_hd.append(rh)
        
        if "The original tourism dataset was used only as the source for Python ingestion" in full_text:
            has_sql_explanation = True
            
        docx_ok = (len(missing_hd) == 0) and has_sql_explanation

    audit_checks.append(("9. Word Report Exists with 12 Headings & SQL Explanation", "PASS" if docx_ok else "FAIL", f"Missing headings: {missing_hd if missing_hd else 'None'}"))

    # 10. QR Code Image & Generator
    qr_ok = (BASE_DIR / "07_QR" / "India_Tourism_Analytics_QR.png").exists() and (BASE_DIR / "07_QR" / "generate_qr.py").exists()
    audit_checks.append(("10. Project 2 QR Code & Generator Script Exist", "PASS" if qr_ok else "FAIL", "07_QR/ verified"))

    # 11. HTML Faculty QR Verification Button Check
    html_qr_btn = False
    if HTML_PATH.exists():
        html_txt = HTML_PATH.read_text(encoding='utf-8')
        if "Faculty QR Verification" in html_txt:
            html_qr_btn = True

    audit_checks.append(("11. HTML Interactive View Has Faculty QR Verification Modal", "PASS" if html_qr_btn else "FAIL", "Navbar modal button verified"))

    # 12. No CSV File in Submission Directory Rule
    csv_files = list(BASE_DIR.glob("**/*.csv"))
    no_csv = len(csv_files) == 0
    audit_checks.append(("12. CSV Restriction Enforced (No Working CSV in Final Folder)", "PASS" if no_csv else "FAIL", f"CSV files found: {len(csv_files)}"))

    # 13. README.md Completeness
    readme_ok = False
    if README_PATH.exists():
        rm_txt = README_PATH.read_text(encoding='utf-8')
        if "India Tourism Analytics" in rm_txt and "IndiaTourismAnalyticsDB" in rm_txt:
            readme_ok = True
    audit_checks.append(("13. Faculty-Friendly README.md Complete", "PASS" if readme_ok else "FAIL", "README.md verified"))

    # Print Summary Table
    all_passed = True
    print(f"{'CHECK ITEM':<62} | {'STATUS':<8} | {'DETAILS'}")
    print("-" * 100)
    for name, status, detail in audit_checks:
        if status != "PASS":
            all_passed = False
        flag = f"[{status}]"
        print(f"{name:<62} | {flag:<8} | {detail}")

    print("=" * 100)
    final_status = "100% COMPLIANT — READY FOR FACULTY SUBMISSION" if all_passed else "NON-COMPLIANT AUDIT DISCREPANCIES FOUND"
    print(f"FINAL AUDIT RESULT: {final_status}")
    print("=" * 100 + "\n")

    return all_passed


if __name__ == "__main__":
    run_compliance_audit()
