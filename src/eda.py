import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def generate_summary_statistics(data, output_path):
    summary = data.describe().to_dict()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(summary, f)
    print(f"Summary statistics saved to {output_path}")

def create_plots(data, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    
    # Univariate Analysis: Histograms
    for col in data.select_dtypes(include=['float64', 'int64']).columns:
        plt.figure()
        sns.histplot(data[col], kde=True)
        plt.title(f'Histogram of {col}')
        plt.savefig(f"{output_folder}/{col}_histogram.png")
    
    # Correlation Heatmap
    plt.figure(figsize=(10, 8))
    corr_matrix = data.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.savefig(f"{output_folder}/correlation_heatmap.png")

def segment_users(data, output_path):
    data['decile'] = pd.qcut(data['session_duration'], 10, labels=False)
    total_data_per_decile = data.groupby('decile')['total_data_volume'].sum()
    total_data_per_decile.to_csv(output_path)
    print(f"User segmentation saved to {output_path}")
