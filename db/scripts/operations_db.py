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
        cur.execute("""
            INSERT INTO users (login, password, name, business_about)
            VALUES (%s, %s, %s, %s)
        """, (login, password, name, info))
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()

    return 0

