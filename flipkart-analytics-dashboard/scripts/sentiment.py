import pandas as pd
from textblob import TextBlob

df = pd.read_csv("data/cleaned/flipkart_cleaned.csv")

df["brand"] = df["product_name"].str.split().str[0]

df["review_length"] = df["review"].apply(len)

def rating_label(r):
    if r >= 4:
        return "Positive"
    elif r == 3:
        return "Neutral"
    else:
        return "Negative"

df["rating_label"] = df["rating"].apply(rating_label)

def get_sentiment(text):
    score = TextBlob(text).sentiment.polarity

    if score > 0:
        return "Positive"
    elif score == 0:
        return "Neutral"
    else:
        return "Negative"

df["sentiment"] = df["review"].apply(get_sentiment)

df.to_csv("data/cleaned/flipkart_final.csv", index=False)