# Stock Market Dashboard

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
