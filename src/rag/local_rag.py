from pathlib import Path
import sys
import chromadb
from sentence_transformers import SentenceTransformer


DOCUMENTS_DIR = Path("data/documents")
CHROMA_DIR = Path("data/processed/chroma_db")
COLLECTION_NAME = "smart_retail_documents"


def load_markdown_documents(documents_dir: Path = DOCUMENTS_DIR) -> list[dict]:
    documents = []

    for path in documents_dir.glob("*.md"):
        text = path.read_text(encoding="utf-8")

        documents.append(
            {
                "source": path.name,
                "text": text,
            }
        )

    return documents


def split_text(text: str, chunk_size: int = 800, chunk_overlap: int = 100) -> list[str]:
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start = end - chunk_overlap

    return chunks


def build_chunks(documents: list[dict]) -> list[dict]:
    all_chunks = []

    for document in documents:
        chunks = split_text(document["text"])

        for index, chunk in enumerate(chunks):
            all_chunks.append(
                {
                    "id": f"{document['source']}-{index}",
                    "source": document["source"],
                    "chunk_index": index,
                    "text": chunk,
                }
            )

    return all_chunks


def get_embedding_model() -> SentenceTransformer:
    return SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def create_chroma_collection():
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"description": "Smart Retail project business documents"},
    )

    return collection


def index_documents() -> None:
    print("Loading documents...")
    documents = load_markdown_documents()

    print("Splitting documents into chunks...")
    chunks = build_chunks(documents)

    print(f"Chunks created: {len(chunks)}")

    print("Loading embedding model...")
    model = get_embedding_model()

    texts = [chunk["text"] for chunk in chunks]
    ids = [chunk["id"] for chunk in chunks]
    metadatas = [
        {
            "source": chunk["source"],
            "chunk_index": chunk["chunk_index"],
        }
        for chunk in chunks
    ]

    print("Creating embeddings...")
    embeddings = model.encode(texts).tolist()

    print("Saving chunks into ChromaDB...")
    collection = create_chroma_collection()

    existing = collection.get()

    if existing["ids"]:
        collection.delete(ids=existing["ids"])

    collection.add(
        ids=ids,
        documents=texts,
        metadatas=metadatas,
        embeddings=embeddings,
    )

    print("Indexing completed.")


def search_documents(question: str, top_k: int = 3) -> list[dict]:
    model = get_embedding_model()
    question_embedding = model.encode([question]).tolist()[0]

    collection = create_chroma_collection()

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=top_k,
    )

    matches = []

    for index in range(len(results["ids"][0])):
        matches.append(
            {
                "source": results["metadatas"][0][index]["source"],
                "chunk_index": results["metadatas"][0][index]["chunk_index"],
                "text": results["documents"][0][index],
                "distance": results["distances"][0][index],
            }
        )

    return matches


def answer_question(question: str, top_k: int = 3) -> str:
    matches = search_documents(question, top_k=top_k)

    answer_parts = [
        f"Question: {question}",
        "",
        "Relevant context found in project documents:",
    ]

    for match in matches:
        answer_parts.append("")
        answer_parts.append(f"Source: {match['source']} | Chunk: {match['chunk_index']}")
        answer_parts.append(match["text"])

    return "\n".join(answer_parts)


def main():
    index_documents()

    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
    else:
        question = "Comment gérer les clients à risque ?"

    answer = answer_question(question)

    print("")
    print(answer)


if __name__ == "__main__":
    main()