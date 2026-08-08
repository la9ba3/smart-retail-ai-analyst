from pathlib import Path
import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def load_rfm_data(path: str = "data/processed/customer_rfm.csv") -> pd.DataFrame:
    return pd.read_csv(path)


def prepare_features(rfm: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    rfm = rfm.copy()
    rfm.columns = rfm.columns.str.strip()

    features = rfm[["recency", "frequency", "monetary"]]

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    scaled_features_df = pd.DataFrame(
        scaled_features,
        columns=["recency_scaled", "frequency_scaled", "monetary_scaled"],
        index=rfm.index,
    )

    return features, scaled_features_df


def calculate_elbow_scores(scaled_features: pd.DataFrame, max_k: int = 10) -> pd.DataFrame:
    results = []

    for k in range(1, max_k + 1):
        model = KMeans(n_clusters=k, random_state=42, n_init=10)
        model.fit(scaled_features)

        results.append(
            {
                "k": k,
                "inertia": model.inertia_,
            }
        )

    return pd.DataFrame(results)


def train_kmeans(scaled_features: pd.DataFrame, n_clusters: int = 4) -> KMeans:
    model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    model.fit(scaled_features)

    return model


def add_cluster_labels(rfm: pd.DataFrame, model: KMeans, scaled_features: pd.DataFrame) -> pd.DataFrame:
    segmented = rfm.copy()
    segmented["cluster"] = model.predict(scaled_features)

    return segmented


def summarize_clusters(segmented: pd.DataFrame) -> pd.DataFrame:
    cluster_summary = (
        segmented.groupby("cluster", as_index=False)
        .agg(
            customer_count=("CustomerID", "count"),
            avg_recency=("recency", "mean"),
            avg_frequency=("frequency", "mean"),
            avg_monetary=("monetary", "mean"),
        )
        .sort_values("avg_monetary", ascending=False)
    )

    return cluster_summary


def main():
    output_dir = Path("data/processed")
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Loading RFM data...")
    rfm = load_rfm_data()
    rfm.columns = rfm.columns.str.strip()

    print("Preparing and scaling features...")
    features, scaled_features = prepare_features(rfm)

    print("Calculating elbow scores...")
    elbow_scores = calculate_elbow_scores(scaled_features)

    print("Training KMeans model...")
    model = train_kmeans(scaled_features, n_clusters=4)

    print("Adding cluster labels...")
    segmented = add_cluster_labels(rfm, model, scaled_features)

    print("Summarizing clusters...")
    cluster_summary = summarize_clusters(segmented)

    segmented.to_csv(output_dir / "customer_segments.csv", index=False)
    elbow_scores.to_csv(output_dir / "kmeans_elbow_scores.csv", index=False)
    cluster_summary.to_csv(output_dir / "kmeans_cluster_summary.csv", index=False)

    print("KMeans segmentation completed.")
    print("Elbow scores:")
    print(elbow_scores)
    print("Cluster summary:")
    print(cluster_summary)


if __name__ == "__main__":
    main()