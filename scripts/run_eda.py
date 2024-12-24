from src.eda import generate_summary_statistics, create_plots, segment_users
import pandas as pd

data_path = "data/processed/cleaned_data.csv"
summary_path = "data/processed/eda_summary.json"
plots_folder = "data/output/plots/"
segmentation_path = "data/output/tables/user_segmentation.csv"

if __name__ == "__main__":
    data = pd.read_csv(data_path)
    generate_summary_statistics(data, summary_path)
    create_plots(data, plots_folder)
    segment_users(data, segmentation_path)
