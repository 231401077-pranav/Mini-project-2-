# Tableau Calculated Fields & Dashboard Documentation
**Project:** India Tourist Attractions & Tourism Analytics System  
**File:** `04_Tableau/India_Tourism_Analytics.twbx`  
**Database Connection:** SQL Server (`IndiaTourismAnalyticsDB`) / Relational Engine  

---

## 1. Overview of Tableau Implementation

The Tableau packaged workbook (`India_Tourism_Analytics.twbx`) contains 5 supplementary analytical dashboards designed for faculty evaluation:

1. **India Tourism Overview Dashboard**
2. **State Tourism Performance Dashboard**
3. **Tourist Attraction Analytics Dashboard**
4. **Seasonal & Demographic Visitor Dashboard**
5. **Tourism Revenue & Economic Yield Dashboard**

---

## 2. Key Calculated Fields

### Total Visitor Footfall
```tableau
SUM([VisitorCount])
```

### Total Tourism Revenue
```tableau
SUM([EstimatedRevenue])
```

### International Visitor Percentage Share
```tableau
(SUM([InternationalVisitors]) / SUM([VisitorCount])) * 100
```

### Domestic Visitor Percentage Share
```tableau
(SUM([DomesticVisitors]) / SUM([VisitorCount])) * 100
```

### Revenue Yield Per Visitor
```tableau
SUM([EstimatedRevenue]) / SUM([VisitorCount])
```

### Peak Season Traffic Flag
```tableau
IF [IsPeakSeason] = 1 THEN "Peak Tourism Season"
ELSE "Off-Peak Tourism Season"
END
```

### Attraction Popularity Classification
```tableau
IF [PopularityScore] >= 75.0 THEN "Iconic Destination (>75)"
ELSEIF [PopularityScore] >= 50.0 THEN "Major Destination (50-75)"
ELSE "Regional Destination (<50)"
END
```

---

## 3. Parameters & Dynamic Controls

1. **`[Select Metric Parameter]`**: Allows dynamic switching between `Total Visitors`, `Total Revenue`, and `Average Rating` across map views.
2. **`[Top N Attractions Parameter]`**: Slider parameter enabling dynamic top 5, 10, 15, or 20 attraction filtering.
3. **`[Region Filter Parameter]`**: Multi-select filter across North, South, East, West, Central, and Northeast India.

---

## 4. Dashboard Actions & Drill-Downs

- **Action 1: Map to State Drill-Down**  
  Clicking any state on the India Choropleth map filters the State Tourism and Attraction Performance dashboards to show cities and attractions within that state.
  
- **Action 2: Attraction to Category Drill-Down**  
  Clicking a specific attraction category (e.g. Fort, Beach, Temple) highlights associated attractions and seasonal trendlines.

- **Action 3: Season Filter Action**  
  Selecting a season (Winter, Spring, Summer, Monsoon) updates visitor demographic breakdowns and stay duration metrics.
