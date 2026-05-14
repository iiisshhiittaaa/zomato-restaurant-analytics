from dotenv import load_dotenv
import os
load_dotenv()
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine(os.getenv("DATABASE_URL"))

query = """
SELECT listed_in_type,
       AVG(approx_cost) AS avg_cost
FROM restaurants
GROUP BY listed_in_type
ORDER BY avg_cost DESC;
"""

df = pd.read_sql(query, engine)

plt.figure(figsize=(10, 5))
plt.bar(df['listed_in_type'], df['avg_cost'])
plt.xticks(rotation=45)
plt.xlabel("Restaurant Type")
plt.ylabel("Average Cost")
plt.title("Average Cost by Restaurant Type")
plt.tight_layout()
plt.savefig("/Users/ishitakasuhik/Desktop/MINI PROJECTS ZOMATO/python/chart.png")
print("Chart saved!")
