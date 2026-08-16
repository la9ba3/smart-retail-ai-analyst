# Smart Retail AI Analyst

Smart Retail AI Analyst is an end-to-end data and AI portfolio project built on the Online Retail dataset.

The project combines retail analytics, customer segmentation, a FastAPI backend, a Streamlit dashboard, a Retrieval-Augmented Generation assistant, Docker, Google Cloud Platform deployment, BigQuery integration, and basic automated tests.

## Project Overview

The goal of this project is to build a practical AI-powered retail analytics system able to:

- clean and prepare online retail transaction data;
- analyze sales, products, countries and customers;
- calculate business KPIs;
- build RFM customer segmentation;
- apply KMeans clustering;
- expose analytics through a FastAPI backend;
- provide a Streamlit dashboard;
- answer business questions using a RAG pipeline;
- call an external LLM through the Mistral API;
- track LLM calls with LangFuse;
- package the backend with Docker;
- deploy the API on Google Cloud Run;
- store and query data with Cloud Storage and BigQuery;
- validate key functions with unit tests.

## Tech Stack

- Python
- Pandas
- Scikit-learn
- FastAPI
- Streamlit
- ChromaDB
- Sentence Transformers
- Mistral AI
- LangFuse
- Docker
- Docker Compose
- Google Cloud Run
- Google Cloud Storage
- BigQuery
- Pytest

## Dataset

The project uses the Online Retail dataset from the UCI Machine Learning Repository.

The dataset contains transactional data from an online retail business, including:

- invoice number;
- stock code;
- product description;
- quantity;
- invoice date;
- unit price;
- customer ID;
- country.

Large raw and processed data files are not meant to be committed to GitHub in a production setting. They are stored locally and can also be uploaded to Google Cloud Storage and BigQuery.

## Main Features

### Data Pipeline

The project includes scripts to:

- download or load the Online Retail dataset;
- clean missing and invalid values;
- remove cancelled invoices;
- remove invalid quantities and prices;
- calculate a `TotalPrice` column;
- export cleaned datasets to `data/processed`.

### Business Analytics

The analytics layer calculates:

- total revenue;
- number of invoices;
- number of customers;
- number of products;
- number of countries;
- average basket value;
- monthly revenue;
- top products by revenue;
- top products by quantity;
- top countries by revenue.

### Customer Segmentation

The project implements two segmentation approaches:

- RFM scoring;
- KMeans clustering.

RFM is used to classify customers based on:

- recency;
- frequency;
- monetary value.

KMeans is used to group customers into behavioral clusters based on standardized customer features.

### RAG Assistant

The project includes a local Retrieval-Augmented Generation pipeline based on:

- Markdown business documents;
- text chunking;
- sentence-transformer embeddings;
- ChromaDB vector search;
- Mistral API generation;
- LangFuse tracing.

The assistant can answer questions about the project documentation and cite the document chunks used as sources.

### FastAPI Backend

The backend exposes analytics and AI features through API endpoints.

Main endpoints include:

- `GET /health`
- `GET /dataset-summary`
- `GET /sales-kpis`
- `GET /top-products`
- `GET /top-countries`
- `GET /rfm-segments`
- `POST /chat-docs`
- `POST /chat-data`

Swagger documentation is available at:

```text
/docs
```

### Streamlit Dashboard

The Streamlit frontend provides a simple user interface to explore:

- sales KPIs;
- product and country analysis;
- customer segmentation;
- document chat;
- data chat.

### Observability With LangFuse

LangFuse is used to trace LLM calls and inspect:

- input questions;
- retrieved document chunks;
- model outputs;
- latency;
- retrieval quality;
- prompt behavior.

It was also used to compare RAG quality with different `top_k` values.

### Docker And Cloud Deployment

The backend can be packaged with Docker and launched with Docker Compose.

The backend was also deployed on Google Cloud Run using an image stored in Artifact Registry.

The cloud setup includes:

- Google Cloud CLI;
- Artifact Registry;
- Cloud Run;
- Cloud Storage;
- BigQuery.

### BigQuery Integration

The cleaned CSV dataset was uploaded to Cloud Storage and loaded into BigQuery.

Example analyses were run in BigQuery:

- row count validation;
- revenue by country;
- monthly revenue;
- top customers by revenue.

### Tests

The project includes initial unit tests with Pytest.

The tests cover:

- global KPI calculations;
- top products by revenue;
- top countries by revenue;
- FastAPI `/health`;
- FastAPI `/dataset-summary`.

## Project Structure

```text
smart-retail-ai-analyst/
|-- backend/
|   `-- main.py
|-- data/
|   |-- documents/
|   |-- processed/
|   `-- raw/
|-- docker/
|   `-- backend.Dockerfile
|-- docs/
|   |-- data_dictionary.md
|   `-- progress_journal.md
|-- frontend/
|   `-- app.py
|-- notebooks/
|-- src/
|   |-- analysis/
|   |-- data/
|   |-- ml/
|   `-- rag/
|-- tests/
|-- docker-compose.yml
|-- pytest.ini
|-- requirements-backend.txt
|-- requirements.txt
`-- README.md
```

## Local Installation

Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Create a `.env` file based on `.env.example` and add the required API keys:

```env
MISTRAL_API_KEY=your_mistral_api_key
MISTRAL_MODEL=mistral-small-latest
LANGFUSE_PUBLIC_KEY=your_langfuse_public_key
LANGFUSE_SECRET_KEY=your_langfuse_secret_key
LANGFUSE_HOST=https://cloud.langfuse.com
LANGFUSE_BASE_URL=https://cloud.langfuse.com
```

## Run The Backend Locally

```powershell
uvicorn backend.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Run The Streamlit App

```powershell
streamlit run frontend/app.py
```

## Run With Docker

Build the backend image:

```powershell
docker build -f docker/backend.Dockerfile -t smart-retail-backend .
```

Run the backend container:

```powershell
docker run --env-file .env -p 8000:8000 smart-retail-backend
```

Or use Docker Compose:

```powershell
docker compose up --build
```

Stop Compose:

```powershell
docker compose down
```

## Run Tests

```powershell
pytest
```

## Example API Requests

Health check:

```powershell
curl http://127.0.0.1:8000/health
```

Dataset summary:

```powershell
curl http://127.0.0.1:8000/dataset-summary
```

Document chat example:

```json
{
  "question": "Why use RFM segmentation?",
  "top_k": 3
}
```

## Key Learnings

This project demonstrates:

- building a complete data pipeline;
- transforming raw transactions into business KPIs;
- using RFM and KMeans for customer segmentation;
- building APIs with FastAPI;
- creating dashboards with Streamlit;
- implementing a RAG pipeline;
- connecting an external LLM with Mistral;
- monitoring LLM calls with LangFuse;
- packaging applications with Docker;
- deploying containers to Google Cloud Run;
- storing and querying data with BigQuery;
- writing initial unit tests.

## Limitations And Future Improvements

Possible future improvements include:

- improving the Streamlit frontend design;
- adding authentication or API key protection to Cloud Run;
- cleaning BigQuery column names before loading;
- adding GitHub Actions for automated tests;
- adding integration tests;
- moving data access from local CSV files to BigQuery;
- optimizing Docker image size;
- adding a public demo video;
- adding architecture diagrams and screenshots.
