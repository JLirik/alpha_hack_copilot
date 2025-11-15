import os
from dotenv import load_dotenv
import psycopg2
import psycopg2.errors

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    dbname='alpha_hack_db'
)


def register_user(login, password, name, info):
    try:
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO users (login, password, name, business_about)
            VALUES (%s, %s, %s, %s)
        """, (login, password, name, info))
        conn.commit()
    except Exception as e:
        conn.rollback()
        return e


    return 0


def save_vectors(chunks, vectors, category):
    try:
        batch = []
        for i in range(len(chunks)):
            batch.append((chunks[i], vectors[i], category))

        cur = conn.cursor()
        cur.executemany(
            """INSERT INTO chunks (text, embedding, category) 
                VALUES (%s,%s,%s)
            """, batch
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        return e

    return 0

def comparing_embeddings(embedding):
    try:
        cur = conn.cursor()
        cur.execute(f"""
            SELECT category, embedding <=> '{embedding}' FROM chunks ORDER BY embedding <=> '{embedding}' LIMIT 5;
            """)

        result = cur.fetchall()
    except Exception as e:
        conn.rollback()
        return e

    return result
