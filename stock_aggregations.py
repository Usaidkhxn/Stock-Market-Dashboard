import pandas as pd

# Load cleaned parquet
df = pd.read_parquet("data/cleaned.parquet")

#  Ensure consistent lowercase column names
df.columns = [c.lower() for c in df.columns]

#  Daily average close by ticker
agg1 = df.groupby(['trade_date', 'ticker'], as_index=False)['close_price'].mean()
agg1.to_parquet("data/agg1.parquet", index=False)

#  Average volume by sector
agg2 = df.groupby('sector', as_index=False)['volume'].mean()
agg2.to_parquet("data/agg2.parquet", index=False)

#  Simple daily return by ticker
df_sorted = df.sort_values(['ticker', 'trade_date'])
df_sorted['daily_return'] = df_sorted.groupby('ticker')['close_price'].pct_change()
agg3 = df_sorted[['trade_date', 'ticker', 'daily_return']].dropna()
agg3.to_parquet("data/agg3.parquet", index=False)

print("Aggregations saved to data/agg1.parquet, data/agg2.parquet, data/agg3.parquet")
