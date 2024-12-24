from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import pandas as pd

# Load processed data
df = pd.read_csv('data/processed/telecom_data.csv')

# Normalize metrics
scaler = MinMaxScaler()
df[['sessions', 'total_duration', 'total_data']] = scaler.fit_transform(
    df[['sessions', 'total_duration', 'total_data']]
)

# K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42).fit(df[['sessions', 'total_duration', 'total_data']])
df['engagement_cluster'] = kmeans.labels_

# Save results
df.to_csv('data/processed/telecom_data.csv', index=False)
