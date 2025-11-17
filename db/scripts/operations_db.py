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


def register_user(login, password, name, city, info):
    try:
        cur = conn.cursor()

        cur.execute(
            """SELECT * FROM users WHERE login = %s""",
            (login,)
        )

        existing_user = cur.fetchone()
        if existing_user:
            return 409

        cur.execute(
            """INSERT INTO users (login, password, city, name, business_about)
            VALUES (%s, %s, %s, %s, %s)
        """, (login, password, city, name, info))

        conn.commit()
    except Exception as e:
        conn.rollback()
        return e
    return 0


def login_user(login, password):
    try:
        cur = conn.cursor()

        cur.execute(
            """SELECT id FROM users WHERE login = %s""",
            login
        )

        existing_user = cur.fetchone()
        if existing_user:
            return 404  # Not exist

        cur.execute(
            """SELECT id FROM users WHERE login = %s AND password = %s""",
            (login, password)
        )

        if not cur.fetchone():
            return 401  # Wrong password
    except Exception as e:
        conn.rollback()
        return e

    return 0


def get_uuid_by_login(login):
    try:
        cur = conn.cursor()
        cur.execute(
            """SELECT id FROM users WHERE login = %s
        """, (login,))

        return cur.fetchone()[0]
    except Exception as e:
        conn.rollback()
        return e


def get_user_info(uuid):
    try:
        cur = conn.cursor()
        cur.execute(
            """SELECT login, city, name, business_about FROM users WHERE id = %s
        """, (uuid,))

        return cur.fetchone()
    except Exception as e:
        conn.rollback()
        return e


def update_user_information(name, city, info, uuid):
    try:
        cur = conn.cursor()
        cur.execute(
            """UPDATE users SET name = %s, city = %s, business_about = %s WHERE id = %s
        """, (name, city, info, uuid))
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
            SELECT category, embedding <=> '{embedding}' FROM chunks ORDER BY embedding <=> '{embedding}' ASC LIMIT 5;
            """)

        result = cur.fetchall()
    except Exception as e:
        conn.rollback()
        return e

    return result


def insert_request(user_id, prompt_in, answer_out, category):
    try:
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO requests_story (user_id, prompt_in, answer_out, category)
            VALUES (%s, %s, %s, %s) RETURNING id;
        """, (user_id, prompt_in, answer_out, category)
        )

        conn.commit()
        return cur.fetchone()

    except Exception as e:
        conn.rollback()
        return e


def get_request(uuid):
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT prompt_in, answer_out FROM requests_story WHERE id = %s
        """, (uuid,)
                    )

        result = cur.fetchone()

        return result
    except Exception as e:
        conn.rollback()
        return e


def get_request_story(uuid, n):
    try:
        cur = conn.cursor()
        cur.execute(f"""
            SELECT id, prompt_in, answer_out, category, request_time 
            FROM requests_story WHERE user_id = %s ORDER BY request_time DESC LIMIT %s;
            """, (uuid, n))

        result = cur.fetchall()
        return result
    except Exception as e:
        conn.rollback()
        return e


def fill_law_base(law_names, texts, embeddings, code):
    try:
        batch = []
        for i in range(len(law_names)):
            batch.append((law_names[i], texts[i], embeddings[i], code))

        cur = conn.cursor()
        cur.executemany(
            """INSERT INTO law_base (law_name, text, embedding, code) 
                VALUES (%s,%s,%s,%s)
            """, batch
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        return e

    return 0


def find_law(embedding):
    try:
        cur = conn.cursor()
        cur.execute(f"""
            SELECT law_name, code, text FROM law_base ORDER BY embedding <=> '{embedding}' ASC LIMIT 5;
            """)

        result = cur.fetchall()
    except Exception as e:
        conn.rollback()
        return e

    return result
