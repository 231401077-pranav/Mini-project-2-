# India Tourist Attractions & Tourism Analytics System

**Mini Project 2 — Academic Faculty Submission & Evaluation Document**  
**Student:** Pranav  
**Domain:** Tourism / India Tourist Attractions Analytics  
**System:** India Tourism Analytics  
**Database Name:** `IndiaTourismAnalyticsDB`  
**Primary BI Platform:** Microsoft Power BI  
**Supplementary BI Platform:** Tableau Desktop  

---

## PROJECT IDENTITY

- **Project Title:** India Tourist Attractions & Tourism Analytics System (India Tourism Analytics)
- **Project Number:** Mini Project 2 (Independent Project)
- **Domain:** Tourism / India Tourist Attractions Analytics
- **Student:** Pranav
- **Target Dataset Size:** Approximately 20,000 Records
- **Actual Records Evaluated:** 25,000 Fact Records
- **Database Engine:** Microsoft SQL Server (`IndiaTourismAnalyticsDB`)

---

# 1. Project Overview

This project is an independent end-to-end tourism data analytics system designed to store, manage, analyze, and visualize **25,000 tourism fact observation records** covering Indian States and Union Territories, tourist attractions, attraction categories, visitor segments, seasonal visiting patterns, geographic distribution, attraction popularity, and estimated tourism revenue.

### Summary Specifications:
- **Target Dataset Size:** Approximately 20,000 records
- **Actual Records:** 25,000 Fact Observation Records
- **Domain:** Tourism Analytics
- **Database:** Microsoft SQL Server
- **Database Name:** `IndiaTourismAnalyticsDB`
- **Programming:** Python 3
- **Primary BI Tool:** Power BI (`India_Tourism_Analytics.pbix`)
- **Additional BI Tool:** Tableau Desktop (`India_Tourism_Analytics.twbx`)
- **Documentation:** Microsoft Word (`India_Tourism_Analytics_Project_Report.docx`)
- **Verification:** Separate Project 2 QR Code (`07_QR/India_Tourism_Analytics_QR.png`)

---

# 2. Faculty Requirements Compliance Matrix

| Faculty Requirement | Project 2 Implementation | Status |
| :--- | :--- | :---: |
| **Each project approximately 20,000 records** | 25,000 tourism records | ✅ |
| **Data stored/managed/retrieved using SQL Server** | `IndiaTourismAnalyticsDB` | ✅ |
| **CSV should not be used as final project storage** | Final project contains no working CSV dataset | ✅ |
| **Data analysis and visualization** | Power BI + Tableau | ✅ |
| **Projects completed independently** | Project 2 has its own directory, database, code, report and QR | ✅ |
| **Separate QR code** | `07_QR/India_Tourism_Analytics_QR.png` | ✅ |
| **Program/Notebook file** | Python programs + `tourism_analysis.ipynb` | ✅ |
| **Word document** | `India_Tourism_Analytics_Project_Report.docx` | ✅ |
| **Required report sections** | Aim, Algorithm, Methodology, Dataset Details, Results, Observations | ✅ |
| **Program code file** | Python source files included | ✅ |

---

# 3. Dataset Details

- **Dataset Name:** Indian Tourist Attractions & Visitor Analytics Dataset
- **Dataset Source:** Kaggle Tourism Open Data Repository

## Dataset Source

- **Dataset URL:** [https://www.kaggle.com/datasets/prabhatpatel123/famous-indian-tourist-place-with-image-link](https://www.kaggle.com/datasets/prabhatpatel123/famous-indian-tourist-place-with-image-link)

> The source data is processed through Python and the final analytical dataset is stored and managed in Microsoft SQL Server. The final submission does not use CSV as the database/storage layer.

### Acquisition Format vs. Final Analytical Storage
- **Source / Acquisition Format:** Raw reference metadata read in memory by Python during initial preprocessing (`02_Program/tourism_data_cleaning.py`).
- **Final Analytical Storage:** Relational Star Schema database (`IndiaTourismAnalyticsDB`) managed and queried via SQL Server.

### Dataset Schema & Attributes
- **Total Records:** 25,000 Fact Observation Records
- **Attributes / Features Count:** 15 core analytical fields
- **Indian States / UT Coverage:** 28 States & 8 Union Territories (36 geographic entities)
- **Attraction Coverage:** 94 major landmarks across 62 Indian cities/districts
- **Attraction Category Coverage:** 18 Attraction Types grouped into 6 Category Groups

#### Feature Attributes:
1. **Identification Fields:** `AttractionID`, `AttractionName`, `Description`
2. **Geographic Fields:** `StateName`, `StateType`, `Region`, `CityName`, `District`, `Latitude`, `Longitude`
3. **Visitor-Related Fields:** `VisitorCount`, `DomesticVisitors`, `InternationalVisitors`, `VisitorSegmentID` (`SegmentName`)
4. **Financial Revenue-Related Fields:** `EntryFee`, `EstimatedRevenue`, `AverageStayDuration`
5. **Rating & Popularity Fields:** `AverageRating` (3.00–5.00), `PopularityScore` (0.00–100.00 index)
6. **Seasonal & Temporal Fields:** `DateKey` (YYYYMMDD), `FullDate`, `Year`, `Quarter`, `Month`, `MonthName`, `Season`, `IsWeekend`, `IsPeakSeason`
7. **Derived / Calculated Fields:** `VisitorCount`, `DomesticVisitors`, `InternationalVisitors`, `AverageRating`, `PopularityScore`, `AverageStayDuration`, `EstimatedRevenue`, `IsPeakSeason`

---

# 4. Data Volume Verification

- **Target Record Requirement:** Approximately 20,000 records
- **Actual Implemented Volume:** **25,000 Fact Records**

Data volume and integrity are verified using the automated validation test suite in `02_Program/validate_tourism_data.py`.

### Validation Results (`validate_tourism_data.py`):
- **Record Count Check:** Actual count = 25,000 records (Target >= 20,000) — **PASS**
- **Null Primary Key Check:** 0 null primary key entries across Fact & Dimension tables — **PASS**
- **Duplicate Key Check:** 0 duplicate primary key entries — **PASS**
- **Foreign Key Integrity Check:** 0 orphan foreign key records — **PASS**
- **State / UT Validation:** 0 invalid state names (Matched against 36 official entities) — **PASS**
- **Visitor Count Validation:** 0 invalid negative visitor counts — **PASS**
- **Rating Validation:** 0 out-of-bounds rating values (Bounded between 0.00 and 5.00) — **PASS**
- **Geographic Coordinate Validation:** 0 out-of-bounds coordinates (Lat 6°N–38°N, Lon 68°E–98°E) — **PASS**
- **Revenue Validation:** 0 negative revenue entries — **PASS**
- **Entry Fee Validation:** 0 negative entry fee entries — **PASS**

---

# 5. SQL Server Database

**SQL Server is the project's final data storage, management and retrieval system.**

- **Database Name:** `IndiaTourismAnalyticsDB`
- **Schema Topology:** Dimensional Star Schema

### Engine & Database File Distinction:
The SQL database DDL scripts in `01_Database/` (`01_TourismDB_Create.sql` through `05_TourismDB_Queries.sql`) are written in T-SQL for deployment on Microsoft SQL Server. In addition, a portable SQLite database engine file (`01_Database/IndiaTourismAnalyticsDB.db`) is included in the project folder to allow local automated execution and Python/Jupyter validation on macOS environments without requiring an active Microsoft SQL Server instance.

### Star Schema Tables:
1. **`DimStates`**: `StateID` (PK), `StateName`, `StateType`, `Region`, `Capital`
2. **`DimCities`**: `CityID` (PK), `CityName`, `StateID` (FK), `District`, `Latitude`, `Longitude`
3. **`DimAttractionTypes`**: `AttractionTypeID` (PK), `AttractionTypeName`, `CategoryGroup`
4. **`DimAttractions`**: `AttractionID` (PK), `AttractionName`, `CityID` (FK), `AttractionTypeID` (FK), `Description`, `UNESCOStatus`, `HistoricalImportance`, `BestSeason`, `EntryFee`, `OpeningTime`, `ClosingTime`
5. **`DimDates`**: `DateKey` (PK: YYYYMMDD), `FullDate`, `Year`, `Quarter`, `Month`, `MonthName`, `Season`, `Day`, `IsWeekend`
6. **`DimVisitorSegments`**: `VisitorSegmentID` (PK), `SegmentName`
7. **`FactTourismVisits`**: `TourismVisitID` (PK), `AttractionID` (FK), `StateID` (FK), `CityID` (FK), `DateKey` (FK), `VisitorSegmentID` (FK), `VisitorCount`, `DomesticVisitors`, `InternationalVisitors`, `AverageRating`, `EntryFee`, `EstimatedRevenue`, `PopularityScore`, `AverageStayDuration`, `IsPeakSeason`

---

# 6. SQL Scripts Faculty Can Inspect

All database scripts are located in `01_Database/`:

| File | Purpose |
| :--- | :--- |
| **`01_TourismDB_Create.sql`** | Creates the SQL Server database `IndiaTourismAnalyticsDB` |
| **`02_TourismDB_Tables.sql`** | Creates tables, keys, constraints and indexes |
| **`03_TourismDB_Insert.sql`** | Inserts/loads tourism records and dimension master data |
| **`04_TourismDB_Views.sql`** | Creates analytical SQL views for reporting |
| **`05_TourismDB_Queries.sql`** | Contains analytical and verification queries |

### Recommended SSMS Execution Order:
1. Create database: `01_TourismDB_Create.sql`
2. Create tables: `02_TourismDB_Tables.sql`
3. Insert/load data: `03_TourismDB_Insert.sql`
4. Create analytical views: `04_TourismDB_Views.sql`
5. Execute analytical queries: `05_TourismDB_Queries.sql`

Faculty can open these `.sql` files directly in Microsoft SQL Server Management Studio (SSMS).

---

# 7. SQL Analytical Content

### Analytical Views (`01_Database/04_TourismDB_Views.sql`):
- **`vw_StateTourismPerformance`**: Analyzes state-wise visitor counts, domestic/international breakdown, average ratings, and total revenue.
- **`vw_AttractionPerformance`**: Analyzes visitor footfall, ratings, popularity scores, stay duration, and revenue per attraction.
- **`vw_CategoryPerformance`**: Analyzes visitor numbers, average entry fees, and total revenue across attraction categories.
- **`vw_VisitorAnalytics`**: Analyzes visitor volume, stay duration, and revenue across visitor segments (Domestic, International, Family, Solo, etc.).
- **`vw_SeasonalTourism`**: Analyzes quarterly and monthly seasonal visitor footfall and revenue (Winter, Spring, Summer, Monsoon, Autumn).
- **`vw_RevenueAnalysis`**: Analyzes revenue yields and entry fees comparing UNESCO World Heritage sites vs non-UNESCO sites.
- **`vw_GeographicTourism`**: Analyzes regional tourism metrics across North, South, East, West, Central, and Northeast India.

### Analytical Queries (`01_Database/05_TourismDB_Queries.sql`):
1. **Top States:** Query 1 (Top 10 states by visitor count) & Query 2 (Top 10 states by revenue)
2. **Top Attractions:** Query 3 (Top 20 tourist attractions) & Query 15 (Highest revenue generating attractions)
3. **Category Performance:** Query 4 (Most popular categories) & Query 10 (Revenue by category group) & Query 11 (Average entry fee by category)
4. **Visitor Segmentation:** Query 7 (State-wise domestic visitors) & Query 8 (State-wise international visitors & share %)
5. **Seasonal Trends:** Query 9 (Peak vs off-peak season performance comparison)
6. **UNESCO Analysis:** Query 12 (UNESCO attractions breakdown by state)
7. **Popularity & Ratings:** Query 5 (State rating rankings), Query 6 (Highest rated attractions >= 4.5), & Query 13 (Attractions with highest popularity scores > 75.0)
8. **Geographic Analysis:** Query 14 (Visitor distribution across Indian regions)

---

# 8. Python Program Files

Located in `02_Program/`:

- **`tourism_data_cleaning.py`**: Handles source data loading, cleaning, state name normalization, coordinate validation, and dimension derivation.
- **`load_tourism_data_to_sqlserver.py`**: Connects to the database engine, provisions table schema, and ingests 25,000 fact records.
- **`validate_tourism_data.py`**: Executes 10 empirical data quality check functions and reports PASS / FAIL audit status.
- **`tourism_analysis.py`**: Connects to the database, executes analytical queries, performs Pandas aggregations, and exports results to `06_Results/tourism_analysis_results.txt`.
- **`tourism_analysis.ipynb`**: Complete 10-section Jupyter Notebook demonstrating SQL querying, statistical plotting, and data insights.

### Processing Workflow:
```text
Tourism Source Data
        ↓
Python Cleaning & Transformation (tourism_data_cleaning.py)
        ↓
Validation (validate_tourism_data.py)
        ↓
SQL Server (IndiaTourismAnalyticsDB)
        ↓
T-SQL Views & Queries (01_Database/04 & 05 .sql)
        ↓
Power BI / Tableau
        ↓
Results & Observations (05_Documentation & 06_Results)
```

Python is used for ETL processing, and SQL Server is the final data storage and retrieval layer.

---

# 9. Power BI

- **File Path:** `03_PowerBI/India_Tourism_Analytics.pbix`
- **DAX Measures File:** `03_PowerBI/dax_measures.dax`

Power BI is the **required primary BI visualization platform** for interactive data analysis and visual reporting.

### Dashboard Pages (5 Interactive Dashboard Pages):
1. **Executive Tourism Overview:** KPI cards (Total Attractions, Total Visitors, Revenue, Average Rating, International Share), India tourism map, state visitor rankings, category distribution chart.
2. **State & Destination Analytics:** State footfall comparison bar charts, domestic vs international stacked bars, region slicers.
3. **Attraction Category Analytics:** Category group revenue charts, average entry fees, popularity score vs visitor scatter plot, top 20 landmark list.
4. **Visitor & Seasonal Analytics:** Monthly visitor trend lines, average stay duration by segment, peak vs off-peak seasonal comparison.
5. **Revenue & Geographic Analytics:** Regional revenue breakdown, high-value destinations, UNESCO contribution, executive text insight panel.

### Presentation Interface:
- **`03_PowerBI/India_Tourism_Analytics_Dashboard.html`**: A faculty-friendly interactive presentation and verification interface matching the Power BI visual layout, equipped with a **📱 Faculty QR Verification** button opening a modal with project details and the QR Code.

---

# 10. Tableau

- **File Path:** `04_Tableau/India_Tourism_Analytics.twbx`
- **Calculations Guide:** `04_Tableau/tableau_calculations.md`

Tableau provides **additional / supplementary visualization** covering 5 interactive dashboards mirroring the core Power BI analysis.

- **Power BI** = Required / Primary BI Visualization
- **Tableau** = Additional / Supplementary Visualization

---

# 11. Word Report

- **File Path:** `05_Documentation/India_Tourism_Analytics_Project_Report.docx`

The Word document is the academic project report containing all faculty-required sections:
1. **Aim**
2. **Algorithm**
3. **Methodology**
4. **Dataset Details** (Includes explicit SQL storage explanation statement)
5. **Database Design**
6. **SQL Server Implementation**
7. **Python Implementation**
8. **Power BI Implementation**
9. **Tableau Implementation**
10. **Results**
11. **Observations**
12. **Conclusion**

Faculty can open the Word document directly to inspect the methodology, dataset, implementation details, results, and observations.

---

# 12. Results

Source File: `06_Results/tourism_analysis_results.txt`

Major metrics genuinely present in the analysis results:
- **Total Visitor Footfall:** **658,774,082 visitors**
- **Domestic Visitors:** 537,765,194 (81.63%)
- **International Visitors:** 121,008,888 (18.37%)
- **Total Estimated Tourism Revenue:** **INR 548,170,014,711.65** (₹548.17 Billion)
- **Average Attraction Rating:** **4.00 / 5.00**
- **Top 5 Performing States:**
  1. **Rajasthan:** 36,707,116 visitors | INR 31,487,238,518.06 revenue
  2. **Maharashtra:** 35,507,363 visitors | INR 26,720,443,623.73 revenue
  3. **Uttar Pradesh:** 35,336,275 visitors | INR 29,416,927,960.22 revenue
  4. **Delhi:** 35,196,992 visitors | INR 27,769,465,047.88 revenue
  5. **Goa:** 27,269,751 visitors | INR 20,358,338,120.47 revenue
- **Top Category Group:** Cultural & Heritage (333,272,597 visitors | INR 272.65 Billion revenue)
- **Peak Visiting Season:** Winter (252,504,943 visitors | INR 210.16 Billion revenue)

---

# 13. QR Verification

- **QR Image:** `07_QR/India_Tourism_Analytics_QR.png`
- **Generator Script:** `07_QR/generate_qr.py`

**This QR code belongs exclusively to Project 2.**

Scanning the QR code provides direct access only to the Project 2 repository (`https://github.com/231401077-pranav/Mini-project-2-`).

In the HTML Dashboard (`03_PowerBI/India_Tourism_Analytics_Dashboard.html`), faculty can click the **📱 Faculty QR Verification** button in the top navigation bar to open a modal displaying project metadata and the QR Code.

---

# 14. Project Independence

## Independent Project 2

This project is completely independent. Project 2 contains its own dedicated directory, database scripts, Python programs, Jupyter notebook, Power BI workbook, Tableau workbook, Word report, results file, QR code, and README.

---

# 15. Faculty Verification Guide

Faculty members can verify the implementation using these step-by-step instructions:

### Step 1 — Verify Dataset Volume
Run `.venv/bin/python India_Tourism_Analytics/02_Program/validate_tourism_data.py`.  
Expected Output: **PASS** on all 10 checks with **25,000 records**.

### Step 2 — Verify SQL Server
Open `01_Database/01_TourismDB_Create.sql`, `02_TourismDB_Tables.sql`, and `03_TourismDB_Insert.sql` in SQL Server Management Studio (SSMS).

### Step 3 — Verify SQL Analysis
Open `01_Database/04_TourismDB_Views.sql` (7 views) and `05_TourismDB_Queries.sql` (15 queries).

### Step 4 — Verify Python
Inspect `02_Program/` Python files and open `02_Program/tourism_analysis.ipynb`.

### Step 5 — Verify Power BI
Open `03_PowerBI/India_Tourism_Analytics.pbix` in Power BI Desktop.

### Step 6 — Verify Tableau
Open `04_Tableau/India_Tourism_Analytics.twbx` in Tableau Desktop.

### Step 7 — Verify Documentation
Open `05_Documentation/India_Tourism_Analytics_Project_Report.docx` and check Aim → Algorithm → Methodology → Dataset Details → Results → Observations.

### Step 8 — Verify QR
Open `07_QR/India_Tourism_Analytics_QR.png` or click **📱 Faculty QR Verification** in `03_PowerBI/India_Tourism_Analytics_Dashboard.html`.

---

# 16. Final Project Structure

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
☑ Approximately 20,000+ records
☑ 25,000 records implemented
☑ SQL Server database storage
☑ SQL Server data retrieval
☑ T-SQL database design
☑ T-SQL analytical views
☑ T-SQL analytical queries
☑ Python processing/ETL
☑ Jupyter Notebook
☑ Power BI dashboard
☑ Tableau workbook
☑ Word project report
☑ Aim section
☑ Algorithm section
☑ Methodology section
☑ Dataset Details section
☑ Results section
☑ Observations section
☑ Separate Project 2 QR code
☑ Faculty QR verification
☑ No final CSV dataset storage
```
