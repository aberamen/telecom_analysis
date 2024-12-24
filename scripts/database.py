import pandas as pd
from sqlalchemy import create_engine

# Replace these with your actual database credentials
username = 'your_username'
password = 'your_password'
host = 'your_host'
port = 'your_port'
database = 'your_database'

# Create engine and connect to the database
engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')

# Example query to get xDR data
query = "SELECT * FROM xdr_table_name;"
df = pd.read_sql(query, engine)
