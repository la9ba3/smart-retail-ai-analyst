from pathlib import Path
from ucimlrepo import fetch_ucirepo

def main():
    print("Downloading Online Retail dataset from UCI Machine Learning Repository...")


    online_retail = fetch_ucirepo(id=352)
    df = online_retail.data.original

    output_dir = Path("data/raw")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / "online_retail_raw.csv"
    df.to_csv(output_path, index=False)

    print("dataset downloaded successfuly.")
    print(f"Saved to {output_path}")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    print("Column names:")
    print(list(df.columns))

if __name__ == "__main__":
    main()
    

