import pandas as pd

def build_features():
    """
    Feature engineering:
    - Extract year, month
    """
    input_path = "data/sample/cleaned_crime_data.csv"
    output_path = "data/sample/featured_crime_data.csv"

    df = pd.read_csv(input_path)
    df["year"] = pd.to_datetime(df["date"]).dt.year
    df["month"] = pd.to_datetime(df["date"]).dt.month

    df.to_csv(output_path, index=False)
    print("Feature engineering completed.")

if __name__ == "__main__":
    build_features()
