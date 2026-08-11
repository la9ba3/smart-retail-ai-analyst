from pathlib import Path

import pandas as pd
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

from src.analysis.kpis import calculate_global_kpis
from src.analysis.top_products_countries import (
    calculate_top_countries_by_revenue,
    calculate_top_products_by_revenue,
)
from src.rag.local_rag import answer_question, search_documents


app = FastAPI(
    title="Smart Retail AI Analyst API",
    description="Backend API for retail analytics, customer segmentation and RAG.",
    version="0.2.0",
)

CLEAN_DATA_PATH = Path("data/processed/online_retail_clean.csv")
RFM_DATA_PATH = Path("data/processed/customer_rfm.csv")



class ChatDocsRequest(BaseModel):
    question: str = Field(..., min_length=3)
    top_k: int = Field(default=3, ge=1, le=5)



def load_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise HTTPException(
            status_code=404,
            detail=f"File not found: {path}. Please run the data pipeline first.",
        )

    df = pd.read_csv(path, skipinitialspace=True)
    df.columns = df.columns.str.strip()
    return df


@app.get("/health")
def health_check() -> dict:
    return {
        "status": "ok",
        "service": "smart-retail-ai-analyst-api",
        "version": "0.2.0",
    }


@app.get("/dataset-summary")
def dataset_summary() -> dict:
    df = load_csv(CLEAN_DATA_PATH)

    return {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "column_names": df.columns.tolist(),
    }


@app.get("/sales-kpis")
def sales_kpis() -> dict:
    df = load_csv(CLEAN_DATA_PATH)
    kpis = calculate_global_kpis(df)

    return {
        "total_revenue": round(float(kpis["total_revenue"]), 2),
        "total_invoices": int(kpis["total_invoices"]),
        "total_customers": int(kpis["total_customers"]),
        "total_products": int(kpis["total_products"]),
        "total_countries": int(kpis["total_countries"]),
        "average_basket": round(float(kpis["average_basket"]), 2),
    }


@app.get("/top-products")
def top_products(limit: int = Query(default=10, ge=1, le=50)) -> list[dict]:
    df = load_csv(CLEAN_DATA_PATH)
    products = calculate_top_products_by_revenue(df, top_n=limit)

    products["total_revenue"] = products["total_revenue"].round(2)

    return products.to_dict(orient="records")


@app.get("/top-countries")
def top_countries(limit: int = Query(default=10, ge=1, le=50)) -> list[dict]:
    df = load_csv(CLEAN_DATA_PATH)
    countries = calculate_top_countries_by_revenue(df, top_n=limit)

    countries["total_revenue"] = countries["total_revenue"].round(2)

    return countries.to_dict(orient="records")


@app.get("/rfm-segments")
def rfm_segments() -> list[dict]:
    rfm = load_csv(RFM_DATA_PATH)
    rfm.columns = rfm.columns.str.strip()

    segment_counts = (
        rfm["segment"]
        .value_counts()
        .reset_index()
    )

    segment_counts.columns = ["segment", "customer_count"]

    return segment_counts.to_dict(orient="records")


@app.post("/chat-docs")
def chat_docs(request: ChatDocsRequest) -> dict:
    try:
        answer = answer_question(request.question, top_k=request.top_k)
        sources = search_documents(request.question, top_k=request.top_k)

        return {
            "question": request.question,
            "answer": answer,
            "sources": sources,
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Document chat failed: {error}",
        ) from error