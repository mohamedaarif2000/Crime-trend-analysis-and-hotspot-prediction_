from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

sys.path.append("/opt/airflow")

from src.data_ingestion.ingest_data import ingest_data
from src.data_cleaning.clean_data import clean_data
from src.feature_engineering.features import create_features
from src.modeling.train_model import train_model
from src.evaluation.evaluate_model import evaluate

default_args = {"start_date": datetime(2024, 1, 1)}

with DAG(
    "crime_analysis_pipeline",
    schedule_interval=None,
    default_args=default_args,
    catchup=False,
) as dag:

    ingest = PythonOperator(
        task_id="data_ingestion",
        python_callable=ingest_data,
        op_args=["data/sample/crime_sample.csv", "data/ingested_data.csv"]
    )

    clean = PythonOperator(
        task_id="data_cleaning",
        python_callable=clean_data,
        op_args=["data/ingested_data.csv", "data/cleaned_data.csv"]
    )

    features = PythonOperator(
        task_id="feature_engineering",
        python_callable=create_features,
        op_args=["data/cleaned_data.csv", "data/features.csv"]
    )

    model = PythonOperator(
        task_id="model_training",
        python_callable=train_model,
        op_args=["data/features.csv"]
    )

    eval_task = PythonOperator(
        task_id="evaluation",
        python_callable=evaluate
    )

    ingest >> clean >> features >> model >> eval_task
