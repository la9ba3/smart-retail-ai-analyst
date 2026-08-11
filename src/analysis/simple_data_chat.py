from pathlib import Path

import pandas as pd

from src.analysis.kpis import calculate_global_kpis
from src.analysis.top_products_countries import (
    calculate_top_countries_by_revenue,
    calculate_top_products_by_revenue,
)


CLEAN_DATA_PATH = Path("data/processed/online_retail_clean.csv")
RFM_DATA_PATH = Path("data/processed/customer_rfm.csv")


def load_csv(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, skipinitialspace=True)
    df.columns = df.columns.str.strip()
    return df


def detect_intent(question: str) -> str:
    question_lower = question.lower()

    if any(keyword in question_lower for keyword in ["chiffre", "ca", "revenue", "ventes"]):
        return "sales_kpis"

    if any(keyword in question_lower for keyword in ["produit", "produits", "top product"]):
        return "top_products"

    if any(keyword in question_lower for keyword in ["pays", "country", "countries"]):
        return "top_countries"

    if any(keyword in question_lower for keyword in ["client", "clients", "customer"]):
        return "customers"

    if any(keyword in question_lower for keyword in ["segment", "segments", "rfm"]):
        return "segments"

    return "unknown"


def answer_sales_kpis() -> str:
    df = load_csv(CLEAN_DATA_PATH)
    kpis = calculate_global_kpis(df)

    return (
        f"Le chiffre d'affaires total est de {kpis['total_revenue']:,.2f}. "
        f"Le dataset contient {kpis['total_invoices']:,} factures, "
        f"{kpis['total_customers']:,} clients, {kpis['total_products']:,} produits "
        f"et {kpis['total_countries']:,} pays. "
        f"Le panier moyen est de {kpis['average_basket']:,.2f}."
    )


def answer_top_products(limit: int = 5) -> str:
    df = load_csv(CLEAN_DATA_PATH)
    products = calculate_top_products_by_revenue(df, top_n=limit)

    lines = ["Voici les meilleurs produits par chiffre d'affaires :"]

    for _, row in products.iterrows():
        lines.append(
            f"- {row['Description']} : {row['total_revenue']:,.2f}"
        )

    return "\n".join(lines)


def answer_top_countries(limit: int = 5) -> str:
    df = load_csv(CLEAN_DATA_PATH)
    countries = calculate_top_countries_by_revenue(df, top_n=limit)

    lines = ["Voici les meilleurs pays par chiffre d'affaires :"]

    for _, row in countries.iterrows():
        lines.append(
            f"- {row['Country']} : {row['total_revenue']:,.2f}"
        )

    return "\n".join(lines)


def answer_customers() -> str:
    df = load_csv(CLEAN_DATA_PATH)
    kpis = calculate_global_kpis(df)

    return f"Le dataset nettoyé contient {kpis['total_customers']:,} clients uniques."


def answer_segments() -> str:
    rfm = load_csv(RFM_DATA_PATH)

    segment_counts = rfm["segment"].value_counts()

    lines = ["Voici le nombre de clients par segment RFM :"]

    for segment, count in segment_counts.items():
        lines.append(f"- {segment} : {count:,} clients")

    return "\n".join(lines)


def answer_data_question(question: str) -> dict:
    intent = detect_intent(question)

    if intent == "sales_kpis":
        answer = answer_sales_kpis()
    elif intent == "top_products":
        answer = answer_top_products()
    elif intent == "top_countries":
        answer = answer_top_countries()
    elif intent == "customers":
        answer = answer_customers()
    elif intent == "segments":
        answer = answer_segments()
    else:
        answer = (
            "Je peux répondre aux questions sur le chiffre d'affaires, les top produits, "
            "les top pays, le nombre de clients et les segments RFM."
        )

    return {
        "question": question,
        "intent": intent,
        "answer": answer,
    }


def main():
    questions = [
        "Quel est le chiffre d'affaires total ?",
        "Quels sont les top produits ?",
        "Quels sont les meilleurs pays ?",
        "Combien y a-t-il de clients ?",
        "Quels sont les segments RFM ?",
    ]

    for question in questions:
        result = answer_data_question(question)
        print("")
        print(f"Question: {result['question']}")
        print(f"Intent: {result['intent']}")
        print(result["answer"])


if __name__ == "__main__":
    main()