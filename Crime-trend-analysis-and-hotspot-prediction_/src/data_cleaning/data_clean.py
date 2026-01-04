import pandas as pd

def clean_data():
    """
    Cleans ingested crime data:
    - Removes missing values
    - Converts date column
    """
    input_path = "data/sample/ingested_crime_data.csv"
    output_path = "data/sample/cleaned_crime_data.csv"

    df = pd.read_csv(input_path)

    df.dropna(inplace=True)
    df["date"] = pd.to_datetime(df["date"])

    df.to_csv(output_path, index=False)
    print("Data cleaning completed.")

if __name__ == "__main__":
    clean_data()
