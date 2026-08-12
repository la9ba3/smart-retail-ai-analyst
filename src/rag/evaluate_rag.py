from src.rag.mistral_rag import generate_answer_with_mistral


TEST_QUESTIONS = [
    "Pourquoi utiliser RFM ?",
    "Comment gérer les clients à risque ?",
    "Quels sont les objectifs du projet ?",
    "Quelles sont les limites du dataset ?",
    "Pourquoi utiliser KMeans ?",
]


def run_evaluation(top_k: int = 3) -> None:
    print(f"Running RAG evaluation with top_k={top_k}")

    for question in TEST_QUESTIONS:
        print("=" * 80)
        print(f"Question: {question}")

        result = generate_answer_with_mistral(question=question, top_k=top_k)

        print("")
        print("Answer:")
        print(result["answer"])

        print("")
        print("Sources:")
        for source in result["sources"]:
            print(
                f"- {source['source']} | chunk {source['chunk_index']} | "
                f"distance={source['distance']:.4f}"
            )


def main():
    run_evaluation(top_k=3)
    


if __name__ == "__main__":
    main()