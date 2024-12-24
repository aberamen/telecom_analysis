import pandas as pd
from sklearn.metrics import pairwise_distances
from src.database import export_to_postgresql

# Load engagement and experience data
engagement_data = pd.read_csv("results/task_2_user_engagement.csv")
experience_data = pd.read_csv("results/task_3_experience.csv")

# Merge datasets
merged_data = pd.merge(engagement_data, experience_data, on="MSISDN")

# Compute scores
merged_data["engagement_score"] = pairwise_distances(
    merged_data[["session_duration", "download_data", "upload_data"]],
    merged_data[["session_duration", "download_data", "upload_data"]].min(axis=0).values.reshape(1, -1),
    metric="euclidean"
).flatten()

merged_data["experience_score"] = pairwise_distances(
    merged_data[["TCP_retransmission", "RTT", "throughput"]],
    merged_data[["TCP_retransmission", "RTT", "throughput"]].max(axis=0).values.reshape(1, -1),
    metric="euclidean"
).flatten()

merged_data["satisfaction_score"] = (merged_data["engagement_score"] + merged_data["experience_score"]) / 2

# Export to PostgreSQL
export_to_postgresql(merged_data, "user_satisfaction")
