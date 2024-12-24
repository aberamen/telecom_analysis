import pandas as pd
import numpy as np
import os

def clean_data(input_path, output_path):
    # Load data
    data = pd.read_csv(input_path)

    # Handle missing values
    for col in data.select_dtypes(include=['float64', 'int64']).columns:
        data[col].fillna(data[col].mean(), inplace=True)
    for col in data.select_dtypes(include=['object']).columns:
        data[col].fillna(data[col].mode()[0], inplace=True)

    # Handle outliers using IQR
    for col in data.select_dtypes(include=['float64', 'int64']).columns:
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        data[col] = np.where(data[col] < lower_bound, data[col].mean(), data[col])
        data[col] = np.where(data[col] > upper_bound, data[col].mean(), data[col])

    # Save cleaned data
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    data.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")
