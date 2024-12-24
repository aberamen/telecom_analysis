import psycopg2
import pandas as pd

def connect_to_postgresql():
    conn = psycopg2.connect(
        dbname="telecom",
        user="username",
        password="password",
        host="localhost",
        port="5432"
    )
    return conn

def export_to_postgresql(df, table_name):
    conn = connect_to_postgresql()
    cursor = conn.cursor()
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.commit()
    cursor.close()
    conn.close()
