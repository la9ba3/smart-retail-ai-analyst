import pandas as pd

from src.analysis.top_products_countries import (
    calculate_top_countries_by_revenue,
    calculate_top_products_by_revenue,
)


def test_calculate_top_products_by_revenue():
    df = pd.DataFrame(
        {
            "StockCode": ["P1", "P1", "P2", "P3"],
            "Description": ["Product 1", "Product 1", "Product 2", "Product 3"],
            "Quantity": [1, 2, 1, 1],
            "TotalPrice": [10.0, 20.0, 50.0, 5.0],
        }
    )

    result = calculate_top_products_by_revenue(df, top_n=2)

    assert len(result) == 2
    assert result.iloc[0]["StockCode"] == "P2"
    assert result.iloc[0]["total_revenue"] == 50.0
    assert result.iloc[1]["StockCode"] == "P1"
    assert result.iloc[1]["total_revenue"] == 30.0


def test_calculate_top_countries_by_revenue():
    df = pd.DataFrame(
        {
            "Country": ["France", "France", "Germany", "Spain"],
            "TotalPrice": [10.0, 20.0, 50.0, 5.0],
        }
    )

    result = calculate_top_countries_by_revenue(df, top_n=2)

    assert len(result) == 2
    assert result.iloc[0]["Country"] == "Germany"
    assert result.iloc[0]["total_revenue"] == 50.0
    assert result.iloc[1]["Country"] == "France"
    assert result.iloc[1]["total_revenue"] == 30.0