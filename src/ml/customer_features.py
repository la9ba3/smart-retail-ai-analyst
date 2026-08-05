from pathlib import Path
import pandas as pd

def load_clean_data(path: str = "data/processed/online_retail_clean.csv") -> pd.DataFrame:
    return pd.read_csv(path)

def get_most_frequent_country(series: pd.Series) -> str:
    return series.mode().iloc[0] 

def build_customer_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    customer_features = (
        df.groupby("CustomerID", as_index=False)
        .agg(
            last_purchase_date=("InvoiceDate", "max"),
            frequency=("InvoiceNo", "nunique"),
            total_quantity=("Quantity", "sum"),
            total_spent=("TotalPrice", "sum"),
            country=("Country", get_most_frequent_country),
        )
        .sort_values("total_spent", ascending=False
    ))
    return customer_features

def main():
    output_path = Path("data/processed/customer_features.csv")

    print("Loading clean dataset...")
    df = load_clean_data()

    print("Building customer features...")
    customer_features = build_customer_features(df)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    customer_features.to_csv(output_path, index=False)

    print("Customer features created successfully.")
    print(f"Saved file: {output_path}")
    print(customer_features.head())
    print(f"Rows: {customer_features.shape[0]}")
    print(f"Columns: {customer_features.shape[1]}")


if __name__ == "__main__":
    main()