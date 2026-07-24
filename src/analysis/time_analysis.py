from pathlib import Path
import pandas as pd


def load_clean_data(path: str = "data/processed/online_retail_clean.csv") -> pd.DataFrame:
    return pd.read_csv(path)


def add_time_columns(df: pd.DataFrame) -> pd.DataFrame:
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["Year"] = df["InvoiceDate"].dt.year
    df["Month"] = df["InvoiceDate"].dt.month
    df["Day"] = df["InvoiceDate"].dt.day
    df["Hour"] = df["InvoiceDate"].dt.hour
    df["YearMonth"] = df["InvoiceDate"].dt.to_period("M").astype(str)
    return df


def calculate_monthly_sales(df : pd.DataFrame) -> pd.DataFrame:
    monthly_sales = ( 
        df.groupby("YearMonth", as_index = False)
        .agg(
            total_revenue=("TotalPrice", "sum"),
            total_invoices=("InvoiceNo", "nunique"),
        )
        .sort_values("YearMonth")
    )
    return monthly_sales


def main():
    output_path = Path("data/processed/monthly_sales.csv")

    print("Loading clean dataset...")
    df = load_clean_data()

    print("Adding time columns...")
    df = add_time_columns(df)

    print("Calculating monthly sales...")
    monthly_sales = calculate_monthly_sales(df)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    monthly_sales.to_csv(output_path, index=False)

    print("Monthly sales calculated successfully.")
    print(f"Saved file: {output_path}")
    print(monthly_sales.head())
    print(monthly_sales.tail())


if __name__ == "__main__":
    main()