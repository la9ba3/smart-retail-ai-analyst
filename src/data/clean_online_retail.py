from pathlib import Path 
import pandas as pd 



def main(): 
    input_path = Path("data/raw/online_retail_raw.csv")
    output_path = Path("data/processed/online_retail_clean.csv")  

    print("loading raw dataset...")
    df = pd.read_csv(input_path) 

    rows_before  = len(df)

    print("Analyzing dataset before cleaning ...")

    missing_customer_id = df['CustomerID'].isna().sum()
    invalid_quantity = (df["Quantity"] <= 0).sum()
    invalid_unit_price = (df["UnitPrice"] <= 0).sum()
    cancelled_invoces= (df["InvoiceNo"].str.startswith("C")).sum()

    print(f"Rows before cleaning: {rows_before}")
    print(f"Missing CustomerID: {missing_customer_id}")
    print(f"Invalid Quantity: {invalid_quantity}")
    print(f"Invalid UnitPrice: {invalid_unit_price}")
    print(f"Cancelled Invoices: {cancelled_invoces}")

    print("Cleaning dataset ...")

    clean_df = df.copy()

    clean_df = clean_df.dropna(subset=['CustomerID'])
    clean_df = clean_df[clean_df["Quantity"] > 0]
    clean_df = clean_df[clean_df["UnitPrice"] > 0]
    clean_df = clean_df[~clean_df["InvoiceNo"].astype(str).str.startswith("C")]

    clean_df["InvoiceDate"] = pd.to_datetime(clean_df["InvoiceDate"])
    clean_df["CustomerID"] = clean_df["CustomerID"].astype(int)
    clean_df["TotalPrice"] = clean_df["Quantity"] * clean_df["UnitPrice"]

    rows_after = len(clean_df)
    rows_removed = rows_before - rows_after

    clean_df.to_csv(output_path, index=False)

    print(f"Cleaning complete.")
    print(f"Rows after cleaning: {rows_after}")
    print(f"Rows removed: {rows_removed}")
    print(f"Clean dataset columns: {clean_df.columns.tolist()}")

if __name__ == "__main__":
    main()
