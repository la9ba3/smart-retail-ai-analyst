from pathlib import Path

import pandas as pd


def load_clean_data(path: str = "data/processed/online_retail_clean.csv") -> pd.DataFrame:
    return pd.read_csv(path)


def calculate_global_kpis(df: pd.DataFrame) -> dict:
    total_revenue = df["TotalPrice"].sum()
    total_invoices = df["InvoiceNo"].nunique()
    total_customers = df["CustomerID"].nunique()
    total_products = df["StockCode"].nunique()
    total_countries = df["Country"].nunique()
    average_basket = total_revenue / total_invoices

    return {
        "total_revenue": total_revenue,
        "total_invoices": total_invoices,
        "total_customers": total_customers,
        "total_products": total_products,
        "total_countries": total_countries,
        "average_basket": average_basket,
    }


def main():
    data_path = Path("data/processed/online_retail_clean.csv")

    print("Loading clean dataset...")
    df = load_clean_data(data_path)

    print("Calculating global KPIs...")
    kpis = calculate_global_kpis(df)

    print("Global KPIs")
    print(f"Total revenue: {kpis['total_revenue']:.2f}")
    print(f"Total invoices: {kpis['total_invoices']}")
    print(f"Total customers: {kpis['total_customers']}")
    print(f"Total products: {kpis['total_products']}")
    print(f"Total countries: {kpis['total_countries']}")
    print(f"Average basket: {kpis['average_basket']:.2f}")


if __name__ == "__main__":
    main()