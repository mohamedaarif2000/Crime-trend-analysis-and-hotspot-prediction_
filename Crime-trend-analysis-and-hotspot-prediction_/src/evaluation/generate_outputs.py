import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_outputs():
    os.makedirs("figures", exist_ok=True)
    os.makedirs("tables", exist_ok=True)


    # Load data for RQ1 & RQ3

    df = pd.read_csv("data/sample/featured_crime_data.csv")


    # RQ1: Crime Trend Over Years

    trend = (
        df.groupby("year")
        .size()
        .reset_index(name="crime_count")
    )

    plt.figure(figsize=(8, 5))
    plt.plot(trend["year"], trend["crime_count"], marker="o")
    plt.xlabel("Year")
    plt.ylabel("Number of Crimes")
    plt.title("Crime Trend Over Years")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("figures/RQ1_Fig1.pdf")
    plt.close()

    trend.to_excel("tables/RQ1_Table1.xlsx", index=False)

   # 2
    cluster_df = pd.read_csv("data/sample/crime_with_clusters.csv")

    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(
        cluster_df["longitude"],
        cluster_df["latitude"],
        c=cluster_df["hotspot_cluster"],
        s=10
    )
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Crime Hotspots Identified Using KMeans")
    plt.colorbar(scatter, label="Cluster ID")
    plt.tight_layout()
    plt.savefig("figures/RQ2_Fig1.pdf")
    plt.close()


    # RQ3: Crime Type Distribution

    crime_type_dist = (
        df["crime_type"]
        .value_counts()
        .reset_index()
    )

    crime_type_dist.columns = ["crime_type", "count"]
    crime_type_dist.to_excel("tables/RQ3_Table1.xlsx", index=False)

    print("All figures and tables generated successfully.")

if __name__ == "__main__":
    generate_outputs()
