# Stock Market Dashboard

This project demonstrates an end-to-end data engineering + visualization workflow using Python.
It begins with a messy CSV of daily stock data and ends with an interactive Streamlit web app displaying trends, sector breakdowns, and ticker-wise analytics, all powered by clean, reproducible code.

# Core Highlights: 

Automated Data Cleaning: Handles inconsistent values, fixes date formats, normalizes schema, and removes duplicates
Data Aggregations: Generates Parquet-based summaries — average close price, sector volume, and daily returns
Interactive Dashboard: Streamlit app with filters for ticker, date range, and multiple charts (line, bar, pie, multi-ticker comparison)
Lightweight & Reproducible: Ideal for beginners learning data wrangling, EDA, and dashboard deployment

## Steps
1. **Data Cleaning:**  
   Run `python stock_cleaning.py` → creates `data/cleaned.parquet`

2. **Aggregations:**  
   Run `python stock_aggregations.py` → creates `agg1.parquet`, `agg2.parquet`, `agg3.parquet`

3. **Visualization:**  
   Run `streamlit run app.py` → interactive dashboard with filters for ticker and date.

## Libraries
- pandas
- streamlit
- altair
- pyarrow (for parquet)

## Example Views
Include screenshots of:
- Dashboard home  
- Avg close by ticker chart  
- Avg volume by sector  
- Daily return line chart

