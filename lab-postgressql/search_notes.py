import os

import psycopg
from dotenv import load_dotenv
from openai import AzureOpenAI


load_dotenv()


client = AzureOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version=os.environ.get("AZURE_OPENAI_API_VERSION", "2024-02-01"),
)


def get_connection():
    return psycopg.connect(
        host=os.environ["POSTGRES_HOST"],
        dbname=os.environ["POSTGRES_DB"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
        port=os.environ.get("POSTGRES_PORT", "5432"),
        sslmode="require",
    )


def create_embedding(text: str) -> list[float]:
    response = client.embeddings.create(
        model=os.environ["AZURE_OPENAI_EMBEDDING_DEPLOYMENT"],
        input=text,
    )

    return response.data[0].embedding


def vector_to_sql(vector: list[float]) -> str:
    return "[" + ",".join(str(value) for value in vector) + "]"


def search_notes(query: str, limit: int = 3):
    query_embedding = create_embedding(query)
    query_vector = vector_to_sql(query_embedding)

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT
                    title,
                    content,
                    embedding <=> %s::vector AS distance
                FROM notes
                WHERE embedding IS NOT NULL
                ORDER BY embedding <=> %s::vector
                LIMIT %s
                """,
                (query_vector, query_vector, limit),
            )

            return cur.fetchall()


def main():
    print("Semantic Notes Search")
    print("Type a search like: vacation ideas, getting healthier, stress, focus")
    print("Type 'quit' to exit.\n")

    while True:
        query = input("Search: ").strip()

        if query.lower() == "quit":
            break

        results = search_notes(query)

        print("\nTop matches:")
        for title, content, distance in results:
            print(f"\n- {title}")
            print(f"  {content}")
            print(f"  similarity distance: {distance:.4f}")

        print()


if __name__ == "__main__":
    main()