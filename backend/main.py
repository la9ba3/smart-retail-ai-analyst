from fastapi import FastAPI

app = FastAPI(
    title = "Smart Retail AI A analyst API",
    description = "Backend API for retail analytics, customer segmentation and RAG.",
    version = "0.1.0",
)


@app.get("/health")
def health_check() -> dict:
    return {
        "status": "ok",
        "service": "smart-retail-ai-analyst-api",
        "version": "0.1.0",
    }