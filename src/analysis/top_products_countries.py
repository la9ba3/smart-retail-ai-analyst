from pathlib import Path

import pandas as pd


def load_clean_data(path: str = "data/processed/online_retail_clean.csv") -> pd.DataFrame:
    return pd.read_csv(path)


def calculate_top_products_by_revenue(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    top_products = (
        df.groupby(["StockCode", "Description"], as_index=False)
        .agg(total_revenue=("TotalPrice", "sum"))
        .sort_values("total_revenue", ascending=False)
        .head(top_n)
    )

    return top_products


def calculate_top_products_by_quantity(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    top_products = (
        df.groupby(["StockCode", "Description"], as_index=False)
        .agg(total_quantity=("Quantity", "sum"))
        .sort_values("total_quantity", ascending=False)
        .head(top_n)
    )

    return top_products


def calculate_top_countries_by_revenue(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    top_countries = (
        df.groupby("Country", as_index=False)
        .agg(total_revenue=("TotalPrice", "sum"))
        .sort_values("total_revenue", ascending=False)
        .head(top_n)
    )

    return top_countries


def main():
    output_dir = Path("data/processed")
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Loading clean dataset...")
    df = load_clean_data()

    print("Calculating top products by revenue...")
    top_products_revenue = calculate_top_products_by_revenue(df)

    print("Calculating top products by quantity...")
    top_products_quantity = calculate_top_products_by_quantity(df)

    print("Calculating top countries by revenue...")
    top_countries_revenue = calculate_top_countries_by_revenue(df)

    top_products_revenue.to_csv(output_dir / "top_products_by_revenue.csv", index=False)
    top_products_quantity.to_csv(output_dir / "top_products_by_quantity.csv", index=False)
    top_countries_revenue.to_csv(output_dir / "top_countries_by_revenue.csv", index=False)

    print("Analysis completed.")
    print("Top products by revenue:")
    print(top_products_revenue)
    print("Top products by quantity:")
    print(top_products_quantity)
    print("Top countries by revenue:")
    print(top_countries_revenue)


if __name__ == "__main__":
    main()