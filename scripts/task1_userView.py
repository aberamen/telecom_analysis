import pandas as pd
from src.preprocessing import handle_missing_values, handle_outliers

# Load data
data = pd.read_csv("data/telecom_data.csv")

# Handle missing values and outliers
data = handle_missing_values(data)
columns_with_outliers = ["session_duration", "download_data", "upload_data"]
data = handle_outliers(data, columns_with_outliers)

# Aggregate user-level metrics
user_aggregates = data.groupby("MSISDN").agg({
    "xDR_sessions": "count",
    "session_duration": "sum",
    "download_data": "sum",
    "upload_data": "sum"
}).reset_index()

# Save results
user_aggregates.to_csv("results/task_1_user_overview.csv", index=False)
