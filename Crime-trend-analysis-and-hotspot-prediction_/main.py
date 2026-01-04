from src.data_ingestion.ingestion_data import ingest_data
from src.data_cleaning.data_clean import clean_data
from src.feature_engineering.build_features import build_features
from src.modeling.hotsot_model import train_hotspot_model
from src.evaluation.generate_outputs import generate_outputs

if __name__ == "__main__":
    print("Starting Crime Trend Analysis & Hotspot Prediction Pipeline...")

    ingest_data()
    clean_data()
    build_features()
    train_hotspot_model()
    generate_outputs()

    print("Pipeline executed successfully.")
