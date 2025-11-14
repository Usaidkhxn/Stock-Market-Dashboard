import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

# APP CONFIG

st.set_page_config(page_title="Stock Market Dashboard", layout="wide")
st.title(" Stock Market Dashboard")
st.caption("Data source: stock_market.csv | Cleaned & Aggregated with Pandas | Visualized in Streamlit")

# LOAD DATA

agg1 = pd.read_parquet("data/agg1.parquet")   # Daily avg close by ticker
agg2 = pd.read_parquet("data/agg2.parquet")   # Avg volume by sector
agg3 = pd.read_parquet("data/agg3.parquet")   # Daily returns

# SIDEBAR FILTERS

st.sidebar.header(" Filters")

tickers = sorted(agg1['ticker'].dropna().unique())
ticker = st.sidebar.selectbox("Select Ticker", tickers)

dates = pd.to_datetime(agg1['trade_date'])
start_date = st.sidebar.date_input("Start Date", dates.min())
end_date = st.sidebar.date_input("End Date", dates.max())

# Filter data based on user selections
filtered = agg1[
    (agg1['ticker'] == ticker)
    & (pd.to_datetime(agg1['trade_date']) >= pd.to_datetime(start_date))
    & (pd.to_datetime(agg1['trade_date']) <= pd.to_datetime(end_date))
]

# MAIN LAYOUT

col1, col2 = st.columns(2)

# Chart 1: Average Close Price Over Time
with col1:
    st.subheader(f"Average Close Price for {ticker}")
    chart1 = (
        alt.Chart(filtered)
        .mark_line(point=True)
        .encode(
            x=alt.X('trade_date:T', title='Date'),
            y=alt.Y('close_price:Q', title='Average Close Price'),
        )
        .properties(height=350)
    )
    st.altair_chart(chart1, use_container_width=True)

# Chart 2: Average Volume by Sector (Bar) 
with col2:
    st.subheader("Average Volume by Sector")
    st.bar_chart(agg2.set_index('sector')['volume'])

# Chart 3: Daily Returns Line Chart 
st.subheader(f"Daily Returns for {ticker}")
returns = agg3[agg3['ticker'] == ticker].sort_values('trade_date')
st.line_chart(returns.set_index('trade_date')['daily_return'])

# Chart 4: Sector-wise Volume Distribution (Pie)
st.subheader("Sector-wise Volume Share")
fig_pie = px.pie(
    agg2,
    names='sector',
    values='volume',
    color_discrete_sequence=px.colors.sequential.Tealgrn,
)
st.plotly_chart(fig_pie, use_container_width=True)

#  Chart 5: Multi-Ticker Comparison of Average Close 
st.subheader("Compare Average Close Across Tickers (Daily)")
compare = agg1.groupby(['trade_date', 'ticker'], as_index=False)['close_price'].mean()
fig_multi = px.line(compare, x='trade_date', y='close_price', color='ticker',
                    title="Daily Avg Close Price by Ticker")
st.plotly_chart(fig_multi, use_container_width=True)
