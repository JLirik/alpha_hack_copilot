import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()


def create_database():
    # Подключаемся к дефолтной БД для создания новой БД
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        dbname=os.getenv('postgres')
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""
        CREATE DATABASE alpha_hack_db;
    """)
    conn.commit()
    conn.close()


def create_tables():
    # Подключаемся к нашей БД
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        dbname='alpha_hack_db'
    )

    with conn.cursor() as cursor:
        # Создаем таблицы
        with open('../sql/schema.sql', 'r') as f:
            sql_script = f.read()
            cursor.execute(sql_script)
        conn.commit()
        print("Таблицы созданы успешно")

    conn.close()


if __name__ == "__main__":
    create_database()
    create_tables()