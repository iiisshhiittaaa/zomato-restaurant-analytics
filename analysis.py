from dotenv import load_dotenv
import os
load_dotenv()
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(os.getenv("DATABASE_URL"))

query = """
SELECT listed_in_type,
       AVG(rate) AS avg_rating
FROM restaurants
GROUP BY listed_in_type
ORDER BY avg_rating DESC;
"""

df = pd.read_sql(query, engine)

print(df)