import pandas as pd
import re

# Load CSV

url = "https://raw.githubusercontent.com/gchandra10/filestorage/refs/heads/main/stock_market.csv"
df = pd.read_csv(url)

print("Shape:", df.shape)
print(df.head())
print(df.info())

# Normalize column names

df.columns = [re.sub(r'\s+', '_', c.strip().lower()) for c in df.columns]


# Standardize text values & remove empty placeholders

df = df.replace(["", " ", "na", "n/a", "none", "null", "-", "<na>"], pd.NA)

# Trim and lowercase all string columns

for col in df.select_dtypes(include="object"):
    df[col] = df[col].astype(str).str.strip().str.lower()

# Clean again (catch lowercase "na" that appeared after stripping)
df = df.replace(["na", "nan", "none", "-", "<na>", "null"], pd.NA)

# Fix date format (convert to yyyy-MM-dd)

df['trade_date'] = pd.to_datetime(df['trade_date'], errors='coerce').dt.strftime("%Y-%m-%d")


# Drop duplicates and invalid rows

df = df.drop_duplicates().dropna(subset=['trade_date', 'ticker'])  # ensure ticker not missing

# Convert numeric columns

numeric_cols = ['open_price', 'close_price', 'volume']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Optional: Drop rows missing numeric core fields if needed
df = df.dropna(subset=['open_price', 'close_price', 'volume'], how='all')

# Save cleaned file

df.to_parquet("data/cleaned.parquet", index=False)
print(" Cleaned data saved to data/cleaned.parquet")
print(f" Final shape: {df.shape}")
print(f" Unique tickers: {df['ticker'].nunique()}")
