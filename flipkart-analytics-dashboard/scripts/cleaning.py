import pandas as pd

df = pd.read_csv("data/raw/flipkart.csv")

# remove useless column
df.drop(columns=["Unnamed: 0"], inplace=True)

# rename columns
df.columns = ["product_name", "review", "rating"]

# remove duplicates
df.drop_duplicates(inplace=True)

# remove null rows
df.dropna(inplace=True)

# fix review text
df["review"] = df["review"].astype(str).str.strip()

# fix product names
df["product_name"] = df["product_name"].astype(str).str.strip()

# ensure rating numeric
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

# remove invalid ratings
df = df[(df["rating"] >= 1) & (df["rating"] <= 5)]

df.to_csv("data/cleaned/flipkart_cleaned.csv", index=False)

print(df.shape)