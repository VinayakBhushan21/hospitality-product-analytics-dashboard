# hospitality-product-analytics-dashboard



An end-to-end analytics project exploring hotel booking behavior — 

seasonality, cancellations, revenue by segment, and geographic demand — 

built from raw booking data through to an interactive Power BI dashboard.



\## Business Question



What drives occupancy, cancellations, and revenue across hotel types, 

seasons, and customer segments — and how can these patterns be surfaced 

in a way a hotel operations or revenue management team could act on?



\## Tools Used



\- \*\*Excel\*\* — initial data inspection

\- \*\*Python (Pandas)\*\* — data cleaning and transformation

\- \*\*SQL (SQLite, via DB Browser)\*\* — exploratory analysis and business-question queries

\- \*\*Power BI\*\* — interactive dashboard



\## Dashboard Preview



!\[Dashboard overview](screenshots/dashboard-overview.png)



!\[Cancellation and revenue trends](screenshots/dashboard-seasonality.png)



\## How This Was Built



1\. \*\*Source\*\* — Raw booking data sourced from Kaggle's public 

&#x20;  \[Hotel Booking Demand dataset](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand) 

&#x20;  (\~119,000 records, 2 hotels, 2015–2017).

2\. \*\*Clean\*\* — Missing values handled, invalid revenue entries removed, and 

&#x20;  new fields (arrival date, total nights stayed) derived using Python/Pandas 

&#x20;  (`scripts/clean\_data.py`).

3\. \*\*Analyze\*\* — Exploratory SQL queries (`/sql`) answering specific business 

&#x20;  questions: seasonal booking trends, cancellation rates by hotel type, 

&#x20;  revenue by market segment, and geographic demand.

4\. \*\*Visualize\*\* — An interactive Power BI dashboard (`/dashboard`) with 

&#x20;  slicers for arrival year and hotel type, built on top of the cleaned data.



\## Repository Structure



├── data/

│ ├── raw/ # Original Kaggle dataset

│ └── clean/ # Cleaned, analysis-ready dataset

├── scripts/

│ └── clean\_data.py # Data cleaning script

├── sql/ # SQL analysis queries

├── dashboard/

│ └── hospitality\_dashboard.pbix

├── screenshots/ # Dashboard preview images

└── docs/

├── project-brief.md # Scope, timeline, deliverables

└── findings-summary.md # Key insights and recommendation



\## Key Documents



\- \[Project Brief](docs/project-brief.md) — objective, scope, and timeline

\- \[Findings Summary](docs/findings-summary.md) — key insights and one 

&#x20; actionable recommendation



\## Notes



The `.pbix` file requires Power BI Desktop (free) to open and interact with 

the live filters. Screenshots above show the dashboard's default view.

