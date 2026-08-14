import pandas as pd

from src.analysis.kpis import calculate_global_kpis


def test_calculate_global_kpis():
    df = pd.DataFrame(
        {
            "InvoiceNo": ["A001", "A001", "A002"],
            "StockCode": ["P1", "P2", "P1"],
            "Quantity": [2, 1, 3],
            "UnitPrice": [10.0, 5.0, 10.0],
            "CustomerID": [1001, 1001, 1002],
            "Country": ["France", "France", "Germany"],
            "TotalPrice": [20.0, 5.0, 30.0],
        }
    )

    kpis = calculate_global_kpis(df)

    assert kpis["total_revenue"] == 55.0
    assert kpis["total_invoices"] == 2
    assert kpis["total_customers"] == 2
    assert kpis["total_products"] == 2
    assert kpis["total_countries"] == 2
    assert kpis["average_basket"] == 27.5