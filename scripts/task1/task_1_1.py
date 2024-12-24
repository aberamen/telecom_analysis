import pandas as pd

# Load dataset
df = pd.read_csv('data/raw/telecom_data.csv')

# Aggregate per user
aggregated = df.groupby('MSISDN').agg(
    sessions=('xDR_sessions', 'count'),
    total_duration=('session_duration', 'sum'),
    total_download=('download_data', 'sum'),
    total_upload=('upload_data', 'sum'),
    total_data=('data_volume', 'sum')
).reset_index()

# Save processed data
aggregated.to_csv('data/processed/user_overview.csv', index=False)
