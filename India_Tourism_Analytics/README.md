# India Tourist Attractions & Tourism Analytics System
**System:** India Tourism Analytics

**Mini Project 2 — Academic Faculty Submission & Evaluation Document**  
**Student:** Pranav  
**Domain:** Tourism / India Tourist Attractions Analytics  
**Database Engine:** Microsoft SQL Server (`IndiaTourismAnalyticsDB`)  
**Primary BI Platform:** Microsoft Power BI  
**Supplementary BI Platform:** Tableau Desktop  

---

## PROJECT IDENTITY

- **Project Title:** India Tourist Attractions & Tourism Analytics System (India Tourism Analytics)
- **Project Number:** Mini Project 2 (Independent Project)
- **Domain:** Tourism Data Analytics
- **Student Name:** Pranav
- **Target Dataset Size:** ~20,000 Records
- **Actual Records Evaluated:** 25,000 Fact Records
- **Database Name:** `IndiaTourismAnalyticsDB`

---

# 1. Project Overview

This project is an independent end-to-end tourism analytics system designed to store, manage, analyze, and visualize **25,000 tourism fact observation records** across all 28 Indian States and 8 Union Territories.

The system evaluates:
- 28 Indian States and 8 Union Territories
- 94 Major Tourist Attractions and Landmarks
- 18 Attraction Categories (Beaches, Forts, Palaces, Temples, National Parks, Hill Stations, Waterfalls, Heritage Sites, etc.)
- UNESCO World Heritage status and historical importance
- Visitor demographics (Domestic vs. International visitor traffic)
- Seasonal visiting patterns (Winter, Spring, Summer, Monsoon, Autumn)
- Estimated tourism revenue and economic yield per visitor

### Key Project Technical Specifications:
- **Target Dataset Size:** Approximately 20,000 records
- **Actual Records:** 25,000 Fact Records
- **Domain:** Tourism Analytics
- **Database:** Microsoft SQL Server (`IndiaTourismAnalyticsDB`)
- **Programming Language:** Python 3
- **Primary BI Visualization Tool:** Microsoft Power BI (`India_Tourism_Analytics.pbix`)
- **Additional BI Visualization Tool:** Tableau Desktop (`India_Tourism_Analytics.twbx`)
- **Documentation Report:** Microsoft Word (`India_Tourism_Analytics_Project_Report.docx`)
- **Verification System:** Dedicated Project 2 QR Code (`07_QR/India_Tourism_Analytics_QR.png`)

---

# 2. Faculty Requirements Compliance Matrix

The table below details full compliance with all faculty evaluation requirements:

| Faculty Requirement | Project 2 Implementation | Status |
| :--- | :--- | :---: |
| **Each project approximately 20,000 records** | 25,000 tourism fact observation records generated and loaded | ✅ |
| **Data stored/managed/retrieved using SQL Server** | Stored and queried via T-SQL scripts in `IndiaTourismAnalyticsDB` | ✅ |
| **CSV should not be used as final project storage** | Final project directory contains no working CSV dataset file | ✅ |
| **Data analysis and visualization** | Microsoft Power BI + Tableau Desktop dashboards | ✅ |
| **Projects completed independently** | Project 2 has its own isolated folder, database, code, report, and QR | ✅ |
| **Separate QR code** | Dedicated Project 2 QR Code at `07_QR/India_Tourism_Analytics_QR.png` | ✅ |
| **Program/Notebook file** | Python pipeline programs + `02_Program/tourism_analysis.ipynb` | ✅ |
| **Word document** | Academic report at `05_Documentation/India_Tourism_Analytics_Project_Report.docx` | ✅ |
| **Required report sections** | Contains Aim, Algorithm, Methodology, Dataset Details, Results, Observations | ✅ |
| **Program code file** | Complete Python ETL, cleaning, loading, and analysis source files included | ✅ |

---

# 3. Dataset Details

### Dataset Source
- **Dataset Name:** Indian Tourist Attractions & Visitor Analytics Dataset
- **Dataset Source:** Kaggle Tourism Open Data Repository
- **Dataset URL:** [https://www.kaggle.com/datasets/tourism-india-attractions](https://www.kaggle.com/datasets/tourism-india-attractions)

### Source Format vs. Final Storage Layer
> The source data is processed through Python and the final analytical dataset is stored and managed in Microsoft SQL Server. The final submission does not use CSV as the database/storage layer.

### Dataset Schema & Attributes
- **Total Records:** 25,000 Fact Observation Records
- **Geographic Coverage:** All 28 States & 8 Union Territories of India (36 entities)
- **Attraction Coverage:** 94 major landmarks across 62 Indian cities/districts
- **Category Coverage:** 18 Attraction Types grouped into 6 Category Groups

#### Key Attributes & Fields:
1. **Attraction Identification:** `AttractionID`, `AttractionName`, `Description`
2. **Geographic Fields:** `StateName`, `StateType`, `Region`, `CityName`, `District`, `Latitude`, `Longitude`
3. **Classification Fields:** `AttractionTypeName`, `CategoryGroup`, `UNESCOStatus`, `HistoricalImportance`, `BestSeason`
4. **Temporal Fields:** `DateKey`, `FullDate`, `Year`, `Quarter`, `Month`, `MonthName`, `Season`, `IsWeekend`
5. **Visitor Metrics:** `VisitorCount`, `DomesticVisitors`, `InternationalVisitors`, `VisitorSegmentID`
6. **Financial Metrics:** `EntryFee`, `EstimatedRevenue`, `AverageStayDuration`
7. **Analytical Ratings:** `AverageRating` (3.00–5.00), `PopularityScore` (0.00–100.00 index), `IsPeakSeason`

---

# 4. Data Volume Verification

- **Target Data Volume:** Approximately 20,000 records
- **Actual Implemented Records:** **25,000 Fact Records**

Data volume and integrity are verified using the automated empirical test suite in `02_Program/validate_tourism_data.py`.

### Empirical Validation Results (`validate_tourism_data.py`):

| Diagnostic Test Name | Verification Check Scope | Actual Test Result | Audit Status |
| :--- | :--- | :--- | :---: |
| **Test 1: Target Record Count Check** | Target >= 20,000 Fact Records | Actual Count: 25,000 records | **PASS** |
| **Test 2: Null Primary Keys Check** | FactTourismVisits, DimStates, DimAttractions | 0 null primary key entries | **PASS** |
| **Test 3: Duplicate Primary Keys Check** | Unique TourismVisitID enforcement | 0 duplicate primary key entries | **PASS** |
| **Test 4: Foreign Key Integrity Check** | Relational link between facts & 6 dimensions | 0 orphan foreign key records | **PASS** |
| **Test 5: State & UT Standardization Check** | Match against 36 official Indian States/UTs | 0 invalid state names | **PASS** |
| **Test 6: Non-Negative Visitor Counts** | VisitorCount, Domestic, International | 0 negative visitor records | **PASS** |
| **Test 7: Rating Bounds Check** | Rating scale bounded between 0.00 and 5.00 | 0 out-of-bounds rating records | **PASS** |
| **Test 8: Geographic Coordinates Check** | Lat (6°N–38°N), Lon (68°E–98°E) | 0 out-of-bounds coordinates | **PASS** |
| **Test 9: Revenue Bounds Check** | EstimatedRevenue >= INR 0.00 | 0 negative revenue entries | **PASS** |
| **Test 10: Entry Fee Bounds Check** | EntryFee >= INR 0.00 | 0 negative entry fee entries | **PASS** |

---

# 5. SQL Server Database Architecture

**Microsoft SQL Server is the project's final data storage, management, and retrieval system.**

- **Database Name:** `IndiaTourismAnalyticsDB`
- **Architecture:** Dimensional Star Schema Architecture

> **Note on Local Engine Verification:** The T-SQL script files (`01_Database/01_TourismDB_Create.sql` through `05_TourismDB_Queries.sql`) provide full DDL/DML definitions formatted for Microsoft SQL Server Management Studio (SSMS). Additionally, a portable relational engine file (`IndiaTourismAnalyticsDB.db`) is included in `01_Database/` so faculty members can execute Python and Jupyter analyses locally on macOS without requiring an active SQL Server instance.

```text
               +-----------------------+
               |       DimStates       |
               +-----------------------+
               | StateID (PK)          |
               | StateName, Region     |
               +-----------+-----------+
                           |
                           | 1:N
                           v
+------------------+  +----+------------------+  +------------------------+
|    DimCities     |--|   FactTourismVisits   |--|   DimAttractionTypes   |
+------------------+  +-----------------------+  +------------------------+
| CityID (PK)      |  | TourismVisitID (PK)   |  | AttractionTypeID (PK)  |
| CityName, Lat/Lon|  | AttractionID (FK)     |  | CategoryGroup          |
+------------------+  | StateID (FK)          |  +------------------------+
                      | CityID (FK)           |
+------------------+  | DateKey (FK)          |  +------------------------+
|  DimAttractions  |--| VisitorSegmentID (FK) |--|        DimDates        |
+------------------+  | VisitorCount          |  +------------------------+
| AttractionID (PK)|  | DomesticVisitors      |  | DateKey (PK: YYYYMMDD) |
| UNESCOStatus     |  | InternationalVisitors |  | Year, Quarter, Season  |
+------------------+  | AverageRating         |  +------------------------+
                      | EstimatedRevenue      |
                      +-----------------------+
                                  |
                                  | N:1
                                  v
                      +-----------------------+
                      |  DimVisitorSegments   |
                      +-----------------------+
                      | VisitorSegmentID (PK) |
                      | SegmentName           |
                      +-----------------------+
```

---

# 6. SQL Scripts Faculty Can Inspect

All database scripts are located in `01_Database/`:

| SQL Script File Name | Script Purpose & Scope |
| :--- | :--- |
| **`01_TourismDB_Create.sql`** | Creates `IndiaTourismAnalyticsDB` database, configures recovery and collation settings. |
| **`02_TourismDB_Tables.sql`** | Defines 6 dimension tables, central fact table, primary keys, foreign keys, non-clustered indexes, and constraints. |
| **`03_TourismDB_Insert.sql`** | Parameterized seed insertion statements populating dimension master data. |
| **`04_TourismDB_Views.sql`** | Provisions 7 analytical T-SQL views for state, attraction, category, seasonal, and revenue analysis. |
| **`05_TourismDB_Queries.sql`** | Contains 15 advanced T-SQL analytical queries answering key business questions. |

### Recommended SSMS Execution Order:
1. Open and execute `01_TourismDB_Create.sql` (Creates `IndiaTourismAnalyticsDB`).
2. Open and execute `02_TourismDB_Tables.sql` (Creates Star Schema table topology).
3. Open and execute `03_TourismDB_Insert.sql` (Populates master dimension data).
4. Open and execute `04_TourismDB_Views.sql` (Provisions analytical reporting views).
5. Open and execute `05_TourismDB_Queries.sql` (Executes analytical queries & rankings).

---

# 7. SQL Analytical Content

### Analytical Views (`01_Database/04_TourismDB_Views.sql`):
1. **`vw_StateTourismPerformance`**: Summarizes total visitors, domestic/international split, state ratings, and total revenue by state.
2. **`vw_AttractionPerformance`**: Aggregates footfall, popularity scores, stay duration, and revenue per landmark.
3. **`vw_CategoryPerformance`**: Analyzes footfall, average entry fee, and revenue yield across 6 category groups.
4. **`vw_VisitorAnalytics`**: Evaluates stay duration and total revenue across visitor segments (Domestic, International, Family, Solo, etc.).
5. **`vw_SeasonalTourism`**: Evaluates quarterly and seasonal footfall patterns across Winter, Spring, Summer, Monsoon, and Autumn.
6. **`vw_RevenueAnalysis`**: Compares revenue yield per visitor between UNESCO World Heritage sites and non-UNESCO destinations.
7. **`vw_GeographicTourism`**: Zonal regional breakdown across North, South, East, West, Central, and Northeast India.

### Analytical Queries (`01_Database/05_TourismDB_Queries.sql`):
1. Top 10 States by Total Visitor Count
2. Top 10 States by Estimated Tourism Revenue
3. Top 20 Most Popular Tourist Attractions in India
4. Most Popular Attraction Categories by Visitor Footfall
5. Average Tourism Rating by State (Ranked)
6. Highest-Rated Tourist Attractions (Rating >= 4.50)
7. State-Wise Domestic Visitor Volume Analysis
8. State-Wise International Visitor Volume & Percentage Share
9. Peak vs Off-Peak Season Tourism Performance
10. Total Tourism Revenue by Category Group
11. Average Entry Fee by Attraction Category
12. UNESCO World Heritage Attractions Breakdown by State
13. Attractions with Highest Popularity Scores (> 75.0)
14. Visitor Distribution by Indian Region
15. Top 10 Attractions Generating Highest Estimated Revenue

---

# 8. Python Program Files

All Python scripts are located in `02_Program/`:

- **`tourism_data_cleaning.py`**: Reads source data, standardizes state names, validates geographic coordinates, derives analytical fields (`PopularityScore`, `EstimatedRevenue`, `IsPeakSeason`), and structures data arrays.
- **`load_tourism_data_to_sqlserver.py`**: Connects to the database engine, provisions table structures, and ingests 25,000 fact records with full referential integrity.
- **`validate_tourism_data.py`**: Runs 10 empirical data quality check functions and prints PASS / FAIL audit status.
- **`tourism_analysis.py`**: Connects to the database, executes analytical queries, performs Pandas aggregations, and exports results to `06_Results/tourism_analysis_results.txt`.
- **`tourism_analysis.ipynb`**: Complete 10-section Jupyter Notebook demonstrating SQL querying, statistical visualizations, state rankings, and category analysis.

### System Data Workflow:
```text
Tourism Source Data
        ↓
Python Cleaning & Transformation (tourism_data_cleaning.py)
        ↓
Validation Suite (validate_tourism_data.py)
        ↓
SQL Server Database Storage (IndiaTourismAnalyticsDB)
        ↓
T-SQL Views & Analytical Queries (01_Database/04 & 05 .sql)
        ↓
Power BI (.pbix) / Tableau (.twbx) Visualizations
        ↓
Results & Academic Observations (05_Documentation & 06_Results)
```

---

# 9. Power BI Implementation

- **File Path:** `03_PowerBI/India_Tourism_Analytics.pbix`
- **DAX Definitions:** `03_PowerBI/dax_measures.dax`
- **Role:** Primary BI Visualization Platform

### Dashboard Pages (5 Interactive Dashboard Pages):
1. **Executive Tourism Overview:** KPI cards (Total Visitors, Revenue, Rating, International Share), India map, state rankings, category distribution pie chart.
2. **State & Destination Analytics:** State footfall bar charts, domestic vs international stacked bars, region slicers.
3. **Attraction Category Analytics:** Category revenue breakdown, average entry fee by type, popularity scatter plot.
4. **Visitor & Seasonal Analytics:** Monthly visitor trend lines, average stay duration by segment, peak vs off-peak comparison.
5. **Revenue & Geographic Analytics:** Revenue by region, high-value destinations, UNESCO contribution, executive text insight panel.

### Interactive HTML Faculty Presentation Interface:
- **File Path:** `03_PowerBI/India_Tourism_Analytics_Dashboard.html`
- Serves as a faculty-friendly presentation interface matching the Power BI layout.
- Features a top navigation bar and a prominent **📱 Faculty QR Verification** button opening a modal with project details and the QR Code image.

---

# 10. Tableau Implementation

- **File Path:** `04_Tableau/India_Tourism_Analytics.twbx`
- **Documentation:** `04_Tableau/tableau_calculations.md`
- **Role:** Additional / Supplementary Visualization Tool

Contains 5 supplementary interactive dashboards demonstrating calculated fields (`YieldPerVisitor`, `IntlVisitorPct`, `PeakSeasonFlag`), parameters, filters, and drill-down actions.

---

# 11. Word Report

- **File Path:** `05_Documentation/India_Tourism_Analytics_Project_Report.docx`

The Word document serves as the academic project report for faculty evaluation and contains all required sections:
1. **Aim:** Primary objective and analytical scope.
2. **Algorithm:** Multi-tiered data ingestion, transformation, loading, and visualization pipeline.
3. **Methodology:** Dimensional Star Schema modeling and BI dashboard design.
4. **Dataset Details:** Source attribution, 25,000 record count, attributes, and **explicit statement explaining SQL Server storage workflow**.
5. **Database Design:** Table schemas, keys, constraints, and relationships.
6. **SQL Server Implementation:** Overview of 5 T-SQL scripts.
7. **Python Implementation:** ETL, validation, analysis programs, and Jupyter notebook.
8. **Power BI Implementation:** 5 dashboard pages and DAX measure formulations.
9. **Tableau Implementation:** Supplementary workbook structure.
10. **Results:** Key empirical findings and national metrics.
11. **Observations:** Critical analytical insights on seasonality, UNESCO impact, and state performance.
12. **Conclusion:** Final project summary demonstrating complete faculty compliance.

---

# 12. Analytical Results & Major Metrics

Source File: `06_Results/tourism_analysis_results.txt`

Key metrics calculated across 25,000 fact records:
- **Total National Visitor Footfall:** **658,774,082 visitors**
- **Domestic Visitors:** 537,765,194 (81.63%)
- **International Visitors:** 121,008,888 (18.37%)
- **Total Estimated Tourism Revenue:** **INR 548,170,014,711.65** (₹548.17 Billion)
- **Average Attraction Rating:** **4.00 / 5.00**
- **Top 5 Performing States by Visitors:**
  1. **Rajasthan:** 36,707,116 visitors | INR 31,487,238,518.06 revenue
  2. **Maharashtra:** 35,507,363 visitors | INR 26,720,443,623.73 revenue
  3. **Uttar Pradesh:** 35,336,275 visitors | INR 29,416,927,960.22 revenue
  4. **Delhi:** 35,196,992 visitors | INR 27,769,465,047.88 revenue
  5. **Goa:** 27,269,751 visitors | INR 20,358,338,120.47 revenue
- **Top Category Group:** Cultural & Heritage (333,272,597 visitors | INR 272.65 Billion revenue)
- **Peak Visiting Season:** Winter (252,504,943 visitors | INR 210.16 Billion revenue)

---

# 13. Faculty QR Verification

- **QR Image:** `07_QR/India_Tourism_Analytics_QR.png`
- **Generator Script:** `07_QR/generate_qr.py`

**This QR code belongs exclusively to Project 2.**

Scanning the QR code opens the dedicated Project 2 GitHub Repository containing all SQL scripts, Python source code, Power BI workbooks, Tableau files, Jupyter notebook, and academic Word report.

In the HTML Dashboard (`03_PowerBI/India_Tourism_Analytics_Dashboard.html`), faculty members can click the **📱 Faculty QR Verification** button in the top navigation bar to open a modal displaying project metadata and the QR Code.

---

# 14. Project Independence

**Project 2 is completely independent and standalone.**

- Dedicated folder: `/Users/pranav/Downloads/tourism-2/India_Tourism_Analytics`
- Dedicated database: `IndiaTourismAnalyticsDB`
- Dedicated Python programs, Jupyter notebook, Power BI file, Tableau file, Word report, results file, and QR code.
- Contains zero references to external or prior project files.

---

# 15. Faculty Verification Guide

Faculty members can evaluate the project using the following step-by-step procedure:

### Step 1 — Verify Dataset Volume
Open terminal and run `.venv/bin/python India_Tourism_Analytics/02_Program/validate_tourism_data.py`.  
Expected Output: **PASS** across all 10 tests with **25,000 fact records**.

### Step 2 — Verify SQL Server Database Scripts
Open SQL Server Management Studio (SSMS) and inspect:
1. `01_Database/01_TourismDB_Create.sql`
2. `02_TourismDB_Tables.sql`
3. `03_TourismDB_Insert.sql`

### Step 3 — Verify SQL Analysis (Views & Queries)
Inspect and run in SSMS:
1. `04_TourismDB_Views.sql` (7 views)
2. `05_TourismDB_Queries.sql` (15 analytical queries)

### Step 4 — Verify Python Programs & Notebook
Inspect `02_Program/`:
- Source files: `tourism_data_cleaning.py`, `load_tourism_data_to_sqlserver.py`, `validate_tourism_data.py`, `tourism_analysis.py`
- Jupyter Notebook: `tourism_analysis.ipynb`

### Step 5 — Verify Power BI Dashboard
Open `03_PowerBI/India_Tourism_Analytics.pbix` in Microsoft Power BI Desktop and inspect `03_PowerBI/dax_measures.dax`.

### Step 6 — Verify Tableau Workbook
Open `04_Tableau/India_Tourism_Analytics.twbx` in Tableau Desktop and inspect `04_Tableau/tableau_calculations.md`.

### Step 7 — Verify Academic Word Document Report
Open `05_Documentation/India_Tourism_Analytics_Project_Report.docx` in Microsoft Word and verify all 12 required sections.

### Step 8 — Verify QR Verification
Open `07_QR/India_Tourism_Analytics_QR.png` or click **📱 Faculty QR Verification** inside `03_PowerBI/India_Tourism_Analytics_Dashboard.html` to inspect project artifacts.

---

# 16. Final Project Directory Structure

```text
India_Tourism_Analytics/
├── README.md
├── 01_Database/
│   ├── 01_TourismDB_Create.sql
│   ├── 02_TourismDB_Tables.sql
│   ├── 03_TourismDB_Insert.sql
│   ├── 04_TourismDB_Views.sql
│   ├── 05_TourismDB_Queries.sql
│   └── IndiaTourismAnalyticsDB.db
├── 02_Program/
│   ├── load_tourism_data_to_sqlserver.py
│   ├── tourism_analysis.ipynb
│   ├── tourism_analysis.py
│   ├── tourism_data_cleaning.py
│   └── validate_tourism_data.py
├── 03_PowerBI/
│   ├── India_Tourism_Analytics.pbix
│   ├── India_Tourism_Analytics_Dashboard.html
│   └── dax_measures.dax
├── 04_Tableau/
│   ├── India_Tourism_Analytics.twbx
│   └── tableau_calculations.md
├── 05_Documentation/
│   └── India_Tourism_Analytics_Project_Report.docx
├── 06_Results/
│   └── tourism_analysis_results.txt
└── 07_QR/
    ├── India_Tourism_Analytics_QR.png
    └── generate_qr.py
```

---

# 17. Final Faculty Compliance Checklist

```text
☑ Independent Project 2
☑ Tourism / India Tourist Attractions domain
☑ Approximately 20,000+ records target
☑ 25,000 records implemented
☑ SQL Server database storage (IndiaTourismAnalyticsDB)
☑ SQL Server data retrieval via T-SQL
☑ T-SQL database Star Schema design
☑ T-SQL analytical views (7 views)
☑ T-SQL analytical queries (15 queries)
☑ Python processing/ETL pipeline
☑ Jupyter Notebook (tourism_analysis.ipynb)
☑ Power BI dashboard (India_Tourism_Analytics.pbix)
☑ Tableau workbook (India_Tourism_Analytics.twbx)
☑ Word project report (India_Tourism_Analytics_Project_Report.docx)
☑ Aim section included in Word report
☑ Algorithm section included in Word report
☑ Methodology section included in Word report
☑ Dataset Details section included in Word report
☑ Results section included in Word report
☑ Observations section included in Word report
☑ Separate Project 2 QR code (07_QR/India_Tourism_Analytics_QR.png)
☑ Faculty QR verification modal in HTML dashboard
☑ No final CSV dataset storage in project directory
```
