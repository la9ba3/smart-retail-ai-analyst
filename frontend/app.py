import streamlit as st
import requests
import pandas as pd

API_BASE_URL = "http://127.0.0.1:8000"

def get_api_data(endpoint: str):
    try:
        response = requests.get(f"{API_BASE_URL}{endpoint}", timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        st.error(f"API request failed: {error}")
        return None

st.set_page_config(
    page_title="Smart Retail AI Analyst",
    page_icon="🛒",
    layout="wide",
)

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "Dataset",
        "Sales KPIs",
        "Products",
        "Customers",
        "RFM Segments",
        "Chat Documents",
        "Architecture",
    ],
)

st.title("Smart Retail AI Analyst")
st.caption("Retail analytics, customer segmentation and future RAG assistant.")

try:
    response = requests.get(f"{API_BASE_URL}/health", timeout=2)
    if response.status_code == 200:
        st.success("Backend API connected")
    else:
        st.warning("Backend API is reachable but returned an unexpected status")
except requests.exceptions.RequestException:
    st.info("Backend API is not running")


if page == "Home":
    st.header("Project Overview")
    st.write(
        "This application analyzes the Online Retail dataset and prepares a complete "
        "portfolio project with data analysis, customer segmentation, API, frontend, "
        "RAG, Docker and GCP deployment."
    )

    st.subheader("Current Status")
    st.write(
        "The project currently includes data loading, cleaning, KPIs, product and country "
        "analysis, RFM scoring, KMeans segmentation and a FastAPI backend."
    )

elif page == "Dataset":
    st.header("Dataset Summary")

    summary = get_api_data("/dataset-summary")

    if summary:
        col1, col2 = st.columns(2)

        col1.metric("Rows", f"{summary['rows']:,}")
        col2.metric("Columns", summary["columns"])

        st.subheader("Columns")
        st.write(summary["column_names"])

elif page == "Sales KPIs":
    st.header("Sales KPIs")

    kpis = get_api_data("/sales-kpis")

    if kpis:
        col1, col2, col3 = st.columns(3)
        col4, col5, col6 = st.columns(3)

        col1.metric("Total Revenue", f"{kpis['total_revenue']:,.2f}")
        col2.metric("Invoices", f"{kpis['total_invoices']:,}")
        col3.metric("Customers", f"{kpis['total_customers']:,}")
        col4.metric("Products", f"{kpis['total_products']:,}")
        col5.metric("Countries", f"{kpis['total_countries']:,}")
        col6.metric("Average Basket", f"{kpis['average_basket']:,.2f}")

elif page == "Products":
    st.header("Top Products")

    products = get_api_data("/top-products?limit=10")

    if products:
        products_df = pd.DataFrame(products)

        st.subheader("Top 10 Products by Revenue")
        st.dataframe(products_df, use_container_width=True)

        st.bar_chart(
            products_df.set_index("Description")["total_revenue"]
        )


elif page == "Customers":
    st.header("Customers")
    st.write("This page will display customer-level analysis.")

elif page == "RFM Segments":
    st.header("RFM Segments")

    segments = get_api_data("/rfm-segments")

    if segments:
        segments_df = pd.DataFrame(segments)

        st.subheader("Customers by Segment")
        st.dataframe(segments_df, use_container_width=True)

        st.bar_chart(
            segments_df.set_index("segment")["customer_count"]
        )

elif page == "Chat Documents":
    st.header("Chat Documents")

    question = st.text_input(
        "Ask a question about the project documents",
        value="Pourquoi utiliser RFM ?",
    )

    top_k = st.slider("Number of document chunks", min_value=1, max_value=5, value=3)

    if st.button("Search documents"):
        try:
            response = requests.post(
                f"{API_BASE_URL}/chat-docs",
                json={
                    "question": question,
                    "top_k": top_k,
                },
                timeout=30,
            )
            response.raise_for_status()
            result = response.json()

            st.subheader("Answer")
            st.write(result["answer"])

            st.subheader("Sources")
            for source in result["sources"]:
                st.markdown(f"**{source['source']} - chunk {source['chunk_index']}**")
                st.write(source["text"])
                st.caption(f"Distance: {source['distance']:.4f}")

        except requests.exceptions.RequestException as error:
            st.error(f"Document chat failed: {error}")

elif page == "Architecture":
    st.header("Architecture")

    st.write(
        "The project separates data processing, machine learning, API delivery and user interface."
    )

    st.code(
        """
data/raw
   ↓
data/processed
   ↓
src/analysis + src/ml
   ↓
backend FastAPI
   ↓
frontend Streamlit
        """,
        language="text",
    )