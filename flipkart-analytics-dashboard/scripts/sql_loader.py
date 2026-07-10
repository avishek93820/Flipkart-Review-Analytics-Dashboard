import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:password@localhost/flipkart_reviews"
)

df = pd.read_csv("data/cleaned/flipkart_final.csv")

df.to_sql(
    "reviews",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully")