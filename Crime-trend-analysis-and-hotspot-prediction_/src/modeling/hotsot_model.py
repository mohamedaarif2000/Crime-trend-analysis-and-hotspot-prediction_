import pandas as pd
from sklearn.cluster import KMeans

def train_hotspot_model():
    """
    Applies KMeans clustering to identify crime hotspots.
    """
    input_path = "data/sample/featured_crime_data.csv"
    output_path = "data/sample/crime_with_clusters.csv"

    df = pd.read_csv(input_path)

    coords = df[["latitude", "longitude"]]

    kmeans = KMeans(n_clusters=3, random_state=42)
    df["hotspot_cluster"] = kmeans.fit_predict(coords)

    df.to_csv(output_path, index=False)
    print("Hotspot model training completed.")

if __name__ == "__main__":
    train_hotspot_model()
