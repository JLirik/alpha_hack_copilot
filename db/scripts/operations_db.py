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
            """SELECT id FROM users WHERE login = %s""",
            login
        )

        existing_user = cur.fetchone()
        if existing_user:
            cur.close()

            return False, "Пользователь с таким логином уже существует"

        cur.execute(
            """INSERT INTO users (login, password, name, business_about)
            VALUES (%s, %s, %s, %s)
        """, (login, password, name, info))

        conn.commit()
    except Exception as e:
        conn.rollback()
        return e


    return 0


def login_user(login, password):
    try:
        cur = conn.cursor()

        cur.execute(
            """SELECT id FROM users WHERE login = %s AND password = %s""",
            (login, password)
        )

        existing_user = cur.fetchone()
        if existing_user:
            cur.close()

            return False, "Неверный логин или пароль"

    except Exception as e:
        conn.rollback()
        return e

    return 0


def update_user_information(info, uuid):
    try:
        cur = conn.cursor()
        cur.execute(
            """UPDATE users SET business_about = %s WHERE id = %s
        """, (info, uuid))
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

def insert_request(user_id, prompt_in, answer_out):
    try:
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO requests_story (user_id, prompt_in, answer_out)
            VALUES (%s, %s, %s)
        """, (user_id, prompt_in, answer_out)
        )
        conn.commit()
    except Exception as e:
        return e

    return 0


def get_request(uuid):
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT prompt_in, answer_out FROM requests_story WHERE id = %s
        """, uuid
        )

        result = cur.fetchone()

        return result
    except Exception as e:
        return e
