import streamlit as st
import requests

API_BASE_URL = "http://127.0.0.1:8000"
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
    st.header("Dataset")
    st.write("This page will display dataset summary information from the FastAPI backend.")

elif page == "Sales KPIs":
    st.header("Sales KPIs")
    st.write("This page will display global sales indicators.")

elif page == "Products":
    st.header("Products")
    st.write("This page will display top products by revenue and quantity.")

elif page == "Customers":
    st.header("Customers")
    st.write("This page will display customer-level analysis.")

elif page == "RFM Segments":
    st.header("RFM Segments")
    st.write("This page will display RFM customer segments.")

elif page == "Architecture":
    st.header("Architecture")
    st.write(
        "The project is organized into a data pipeline, machine learning modules, "
        "FastAPI backend and Streamlit frontend."
    )