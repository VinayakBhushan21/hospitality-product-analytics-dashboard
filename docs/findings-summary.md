# `# Project Brief — Hospitality Product Analytics Dashboard` 

# `## Objective` 

```
Analyze hotel booking data to understand what drives occupancy, cancellations,
and revenue across hotel types, seasons, and customer segments, and present the
findings in an interactive dashboard that a hotel operations or revenue
management team could use to spot patterns and act on them.
```

# `## Data Source` 

```
Kaggle "Hotel Booking Demand" dataset
(https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand) — a
public dataset of hotel booking records from two hotels (a City Hotel and a
Resort Hotel), covering arrivals from 2015 to 2017. Fields include arrival
date, lead time, length of stay, country of origin, market segment,
cancellation status, and average daily rate (ADR).
```

# `## Approach` 

`1. Cleaned the raw dataset in Python (Pandas) — handled missing values, removed invalid revenue entries, and derived new fields (arrival date, total nights stayed) needed for analysis.` 

`2. Ran exploratory SQL queries (via DB Browser for SQLite) to surface seasonal trends, cancellation patterns by hotel type, revenue by market segment, and geographic booking demand.` 

`3. Built an interactive Power BI dashboard on top of the cleaned data, with slicers for year and hotel type so the report can be explored rather than just read.` 

# `## Deliverables` 

- `Cleaned, analysis-ready dataset (`data/clean/hotel_bookings_clean.csv`)` 

- `SQL queries answering key business questions (`/sql`)` 

- `Interactive Power BI dashboard (`/dashboard/hospitality_dashboard.pbix`)` 

- `Short written summary of key findings and one actionable recommendation (`docs/findings-summary.md`)` 

# `## Timeline` 

- `Data sourcing and cleaning: 3 days` 

- `SQL analysis: 1 Day` 

- `Dashboard build: 1 day` 

- `Findings write-up and repo finalization: 1 day` 

