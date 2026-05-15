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


def main():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT id, title, content
                FROM notes
                WHERE embedding IS NULL
                """
            )

            notes = cur.fetchall()

            for note_id, title, content in notes:
                text_to_embed = f"{title}\n{content}"
                embedding = create_embedding(text_to_embed)
                embedding_sql = vector_to_sql(embedding)

                cur.execute(
                    """
                    UPDATE notes
                    SET embedding = %s::vector
                    WHERE id = %s
                    """,
                    (embedding_sql, note_id),
                )

                print(f"Embedded note: {title}")

        conn.commit()

    print("Done generating embeddings.")


if __name__ == "__main__":
    main()