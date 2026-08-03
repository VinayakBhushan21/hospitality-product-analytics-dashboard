"""
clean_data.py
Cleans and transforms the raw Hotel Booking Demand dataset (from Kaggle)
into an analysis-ready CSV for the Power BI dashboard.

Run from the repo root with:
    python scripts\\clean_data.py
"""

import pandas as pd

# ---------------------------------------------------------
# 1. Load the raw data
# ---------------------------------------------------------
raw_path = "data/raw/hotel_bookings.csv"
clean_path = "data/clean/hotel_bookings_clean.csv"

print(f"Loading raw data from {raw_path} ...")
df = pd.read_csv(raw_path)
print(f"Loaded {len(df):,} rows and {len(df.columns)} columns.")

# ---------------------------------------------------------
# 2. Fill missing 'children' values with 0
#    (a blank here means no children were on the booking)
# ---------------------------------------------------------
df["children"] = df["children"].fillna(0)

# ---------------------------------------------------------
# 3. Handle missing 'country' values
#    Rather than dropping rows outright, flag them clearly
#    so they can be filtered or reviewed later without losing data.
# ---------------------------------------------------------
missing_country_count = df["country"].isna().sum()
df["country"] = df["country"].fillna("Unknown")
print(f"Flagged {missing_country_count} rows with missing country as 'Unknown'.")

# ---------------------------------------------------------
# 4. Remove rows with invalid revenue (adr = average daily rate)
#    adr <= 0 is treated as a data error, not a real booking rate.
# ---------------------------------------------------------
before_rows = len(df)
df = df[df["adr"] > 0]
after_rows = len(df)
print(f"Removed {before_rows - after_rows} rows with adr <= 0.")

# ---------------------------------------------------------
# 5. Build a proper arrival_date column
#    The raw data splits this across three separate columns:
#    arrival_date_year, arrival_date_month (as a month name), arrival_date_day_of_month
# ---------------------------------------------------------
df["arrival_date"] = pd.to_datetime(
    df["arrival_date_year"].astype(str)
    + "-"
    + df["arrival_date_month"]
    + "-"
    + df["arrival_date_day_of_month"].astype(str),
    format="%Y-%B-%d",
    errors="coerce",
)

# ---------------------------------------------------------
# 6. Create a total_nights column
#    (weekend nights + week nights stayed, useful for length-of-stay analysis)
# ---------------------------------------------------------
df["total_nights"] = df["stays_in_weekend_nights"] + df["stays_in_week_nights"]

# ---------------------------------------------------------
# 7. Save the cleaned dataset
# ---------------------------------------------------------
df.to_csv(clean_path, index=False)
print(f"Saved cleaned dataset to {clean_path} ({len(df):,} rows).")
