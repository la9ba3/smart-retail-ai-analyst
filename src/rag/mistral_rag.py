import os

from dotenv import load_dotenv
from mistralai.client import Mistral

from src.rag.local_rag import search_documents

from langfuse import get_client, observe

load_dotenv()


def get_mistral_client() -> Mistral:
    api_key = os.getenv("MISTRAL_API_KEY")

    if not api_key:
        raise ValueError("MISTRAL_API_KEY is missing. Please add it to your .env file.")

    return Mistral(api_key=api_key)


def build_context(sources: list[dict]) -> str:
    context_parts = []

    for source in sources:
        context_parts.append(
            f"Source: {source['source']} | Chunk: {source['chunk_index']}\n"
            f"{source['text']}"
        )

    return "\n\n---\n\n".join(context_parts)

@observe(name="mistral-rag-answer")
def generate_answer_with_mistral(question: str, top_k: int = 3) -> dict:
    sources = search_documents(question, top_k=top_k)
    context = build_context(sources)

    model = os.getenv("MISTRAL_MODEL", "mistral-small-latest")
    client = get_mistral_client()

    system_prompt = (
        "Tu es un assistant data spécialisé en retail et analyse client. "
        "Tu réponds en français, de manière claire, structurée et pédagogique. "
        "Tu dois utiliser uniquement le contexte fourni. "
        "Si le contexte ne contient pas assez d'information pour répondre, dis-le clairement. "
        "N'invente pas de chiffres, de résultats ou de sources. "
        "Quand tu utilises une source, cite-la avec le format [nom_du_fichier - chunk X]."
)

    user_prompt = f"""
    Question utilisateur :
    {question}

    Contexte disponible :
    {context}

    Réponds avec exactement ces sections :

    ### Réponse
    Donne une réponse courte, claire et directement liée à la question.

    ### Points clés
    - Donne les idées importantes.
    - Reste basé uniquement sur le contexte fourni.
    - Ne rajoute pas d'information externe non présente dans les documents.

    ### Sources utilisées
    - Cite uniquement les sources réellement utiles avec le format [source - chunk X].
"""

    response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
        temperature=0.2,
        max_tokens=500,
    )

    answer = response.choices[0].message.content

    langfuse = get_client()
    langfuse.update_current_span(
        metadata={
            "model": model,
            "top_k": top_k,
            "sources": [
                {
                    "source": source["source"],
                    "chunk_index": source["chunk_index"],
                    "distance": source["distance"],
                }
                for source in sources
            ],
        }
    )

    
    return {
        "question": question,
        "answer": answer,
        "sources": sources,
        "model": model,
    }


def main():
    result = generate_answer_with_mistral("Pourquoi utiliser RFM ?", top_k=3)

    print("Question:")
    print(result["question"])
    print("")
    print("Model:")
    print(result["model"])
    print("")
    print("Answer:")
    print(result["answer"])


if __name__ == "__main__":
    main()