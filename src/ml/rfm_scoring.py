import pandas as pd
from pathlib import Path 


def load_customer_features(path: str = "data/processed/customer_features.csv") -> pd.DataFrame:
    return pd.read_csv(path)



def assign_segment(row: pd.Series) -> str:
    if row["recency_score"] >= 4 and row["frequency_score"] >= 4 and row["monetary_score"] >= 4:
        return "Champions"

    if row["recency_score"] >= 3 and row["frequency_score"] >= 3:
        return "Loyal"

    if row["recency_score"] <= 2 and row["frequency_score"] >= 3:
        return "At risk"

    if row["recency_score"] <= 2 and row["frequency_score"] <= 2:
        return "Lost"

    return "Potential"


def build_rfm_table(customers: pd.DataFrame) -> pd.DataFrame:
    customers = customers.copy()
    customers.columns = customers.columns.str.strip()
    rfm = customers.copy()
    
    rfm["last_purchase_date"] = pd.to_datetime(rfm["last_purchase_date"])

    analysis_date = rfm["last_purchase_date"].max() + pd.Timedelta(days=1)

    rfm["recency"] = (analysis_date - rfm["last_purchase_date"]).dt.days
    rfm["monetary"] = rfm["total_spent"]

    rfm["recency_score"] = pd.qcut(
        rfm["recency"],
        q=5,
        labels=[5, 4, 3, 2, 1],
        duplicates="drop",
    ).astype(int)

    rfm["frequency_score"] = pd.qcut(
        rfm["frequency"].rank(method="first"),
        q=5,
        labels=[1, 2, 3, 4, 5],
        duplicates="drop",
    ).astype(int)

    rfm["monetary_score"] = pd.qcut(
        rfm["monetary"],
        q=5,
        labels=[1, 2, 3, 4, 5],
        duplicates="drop",
    ).astype(int)

    rfm["rfm_score"] = (
        rfm["recency_score"].astype(str)
        + rfm["frequency_score"].astype(str)
        + rfm["monetary_score"].astype(str)
    )

    rfm["segment"] = rfm.apply(assign_segment, axis=1)

    columns = [
        "CustomerID",
        "recency",
        "frequency",
        "monetary",
        "recency_score",
        "frequency_score",
        "monetary_score",
        "rfm_score",
        "segment",
    ]

    return rfm[columns].sort_values(
        ["recency_score", "frequency_score", "monetary_score"],
        ascending=False,
    )


def main():
    output_path = Path("data/processed/customer_rfm.csv")

    print("Loading customer features...")
    customers = load_customer_features()

    print("Building RFM table...")
    rfm = build_rfm_table(customers)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    rfm.to_csv(output_path, index=False)

    print("RFM table created successfully.")
    print(f"Saved file: {output_path}")
    print(rfm.head())
    print("Segments:")
    print(rfm["segment"].value_counts())


if __name__ == "__main__":
    main()