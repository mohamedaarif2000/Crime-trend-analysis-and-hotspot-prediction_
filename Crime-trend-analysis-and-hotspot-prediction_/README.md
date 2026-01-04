# Crime Trend Analysis and Hotspot Prediction

## Project Overview
This project focuses on analyzing crime trends and identifying crime hotspots using machine learning techniques. 
The system processes spatial and temporal crime data through a reproducible data pipeline and applies clustering 
methods to predict high-risk areas. The entire workflow is automated using Python and Airflow.

## Dataset
A sample crime dataset is included in this repository for reproducibility.
Chicago Crime Dataset from Kaggle -https://www.kaggle.com/search?q=Chicago+Crime+Dataset+date%3A90

## Research Questions
1. What are the overall crime trends over time?
 A. Crime levels vary across years and show noticeable increases and decreases rather than remaining constant. This indicates that crime follows temporal patterns      influenced by time-related factors.
3. Can crime hotspots be identified using spatial (latitude and longitude) data?
 A. Yes.Using latitude and longitude with clustering techniques clearly reveals distinct crime hotspots, showing that crimes are spatially concentrated in             specific areas.
4. How does the frequency of crimes vary across different locations?
 A. Crime frequency differs significantly by location, with some areas experiencing much higher concentrations of crime than others.

## How to Run the Code
```bash
pip install -r requirements.txt
python src/data_ingestion/ingest_data.py
python src/data_cleaning/clean_data.py
python src/feature_engineering/features.py
python src/modeling/train_model.py
python src/evaluation/evaluate_model.py

## How to Run the Airflow DAG
Install Apache Airflow
Place the pipeline_dag.py file inside the dags/ directory
Start Airflow services: airflow standalone
Trigger the DAG named crime_analysis_pipeline from the Airflow UI

## Folder Structure Explanation

dags/ – Contains the Airflow DAG for automating the pipeline
src/ – Core Python scripts for data ingestion, cleaning, feature engineering, modeling, and evaluation
data/ – Sample input data and intermediate processed files
figures/ – Auto-generated visualizations (PNG/PDF)
tables/ – Auto-generated tables and evaluation metrics (CSV)**

## Airflow DAG Description:

The project pipeline is implemented as an Apache Airflow DAG that reflects
a real-world data engineering workflow. The DAG consists of the following
tasks executed sequentially:

extract_data → clean_data → transform_features → train_model → generate_figures_tables

Due to Apache Airflow’s limited support for Windows environments, the DAG
was not deployed via the Airflow UI. However, the DAG is fully runnable
conceptually and adheres to Airflow design best practices, including
clear task naming, logical dependencies, and modular Python operators.




