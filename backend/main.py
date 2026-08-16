from pathlib import Path
import os
import logging
import pandas as pd
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

from src.analysis.kpis import calculate_global_kpis
from src.analysis.top_products_countries import (
    calculate_top_countries_by_revenue,
    calculate_top_products_by_revenue,
)
from src.rag.local_rag import answer_question, search_documents
from src.analysis.simple_data_chat import answer_data_question
from src.rag.mistral_rag import generate_answer_with_mistral
from dotenv import load_dotenv



logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(name)s - %(message)s",
)

logger = logging.getLogger(__name__)


load_dotenv()

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

class ChatDataRequest(BaseModel):
    question: str = Field(..., min_length=3)

def load_csv(path: Path) -> pd.DataFrame:
    logger.info("Loading CSV file: %s", path)

    if not path.exists():
        logger.error("CSV file not found: %s", path)

        raise HTTPException(
            status_code=404,
            detail=f"File not found: {path}. Please run the data pipeline first.",
        )

    df = pd.read_csv(path, skipinitialspace=True)
    df.columns = df.columns.str.strip()

    logger.info("CSV loaded successfully: %s rows, %s columns", df.shape[0], df.shape[1])

    return df

@app.get("/health")
def health_check() -> dict:
    logger.info("Health check called")
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
    logger.info("Document chat requested with top_k=%s", request.top_k)

    if not os.getenv("MISTRAL_API_KEY"):
        logger.error("MISTRAL_API_KEY is missing")

        raise HTTPException(
            status_code=503,
            detail="MISTRAL_API_KEY is missing. Please configure the backend environment.",
        )

    try:
        response = generate_answer_with_mistral(
            question=request.question,
            top_k=request.top_k,
        )

        logger.info("Document chat completed successfully")

        return response

    except Exception as error:
        logger.exception("Document chat failed")

        raise HTTPException(
            status_code=500,
            detail=f"Document chat failed: {error}",
        ) from error

    
@app.post("/chat-data")
def chat_data(request: ChatDataRequest) -> dict:
    logger.info("Data chat requested")

    try:
        response = answer_data_question(request.question)

        logger.info("Data chat completed successfully")

        return response

    except Exception as error:
        logger.exception("Data chat failed")

        raise HTTPException(
            status_code=500,
            detail=f"Data chat failed: {error}",
        ) from error