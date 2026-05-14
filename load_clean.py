from dotenv import load_dotenv
import os
load_dotenv()

import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection
engine = create_engine(os.getenv("DATABASE_URL"))

# Load CSV
df = pd.read_csv("Zomato-data-.csv")

# Rename columns
df.columns = [
    "restaurant_name",
    "online_order",
    "book_table",
    "rate",
    "votes",
    "approx_cost",
    "listed_in_type"
]

# Clean ratings
df['rate'] = (
    df['rate']
    .astype(str)
    .str.replace('/5', '', regex=False)
)

df['rate'] = pd.to_numeric(
    df['rate'],
    errors='coerce'
)

# Clean cost
df['approx_cost'] = (
    df['approx_cost']
    .astype(str)
    .str.replace(',', '', regex=False)
)

df['approx_cost'] = pd.to_numeric(
    df['approx_cost'],
    errors='coerce'
)

# Convert yes/no to boolean
df['online_order'] = (
    df['online_order']
    .map({'Yes': True, 'No': False})
)

df['book_table'] = (
    df['book_table']
    .map({'Yes': True, 'No': False})
)

# Drop missing values
df = df.dropna()


df.to_sql(
    "restaurants",
    engine,
    if_exists="append",
    index=False
)

print("Data cleaned and inserted successfully!")