import pandas as pd
from src.preprocessing import handle_missing_values

# Load data
data = pd.read_csv("data/telecom_data.csv")

# Handle missing values
data = handle_missing_values(data)

# Aggregate user experience metrics
experience_data = data.groupby("MSISDN").agg({
    "TCP_retransmission": "mean",
    "RTT": "mean",
    "throughput": "mean"
}).reset_index()

# Save results
experience_data.to_csv("results/task_3_experience.csv", index=False)
