from src.data_cleaning import clean_data

input_path = "data/raw/telecom_data.csv"
output_path = "data/processed/cleaned_data.csv"

if __name__ == "__main__":
    clean_data(input_path, output_path)
