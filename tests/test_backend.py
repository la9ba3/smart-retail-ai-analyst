from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "ok"
    assert data["service"] == "smart-retail-ai-analyst-api"
    assert data["version"] == "0.2.0"



def test_dataset_summary_endpoint():
    response = client.get("/dataset-summary")

    assert response.status_code == 200

    data = response.json()

    assert data["rows"] > 0
    assert data["columns"] > 0
    assert "column_names" in data
    assert "InvoiceNo" in data["column_names"]