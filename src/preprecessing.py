import pandas as pd

def handle_missing_values(df):
    return df.fillna(df.mean())

def handle_outliers(df, columns):
    for col in columns:
        df[col] = df[col].clip(lower=df[col].quantile(0.05), upper=df[col].quantile(0.95))
    return df
