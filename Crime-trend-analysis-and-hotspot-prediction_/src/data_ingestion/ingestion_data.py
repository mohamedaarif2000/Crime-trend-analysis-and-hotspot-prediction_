import pandas as pd
import os

def ingest_data():
    """
    Loads raw crime data (sample) and saves it for downstream processing.
    """
    input_path = "data/sample/crime_sample.csv"
    output_path = "data/sample/ingested_crime_data.csv"

    df = pd.read_csv(input_path)
    df.to_csv(output_path, index=False)

    print("Data ingestion completed.")

if __name__ == "__main__":
    ingest_data()
