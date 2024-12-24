import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from src.clustering import perform_kmeans

# Load aggregated user data
data = pd.read_csv("results/task_1_user_overview.csv")

# Normalize metrics
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data.iloc[:, 1:])

# Perform k-means clustering
clusters, model = perform_kmeans(normalized_data, 3)
data["engagement_cluster"] = clusters

# Save results
data.to_csv("results/task_2_user_engagement.csv", index=False)
