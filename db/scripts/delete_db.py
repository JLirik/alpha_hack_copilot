import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def delete_database():
    # Подключаемся к дефолтной БД для создания новой БД
    input('Проверьте, чтобы никто не был подключен к базе данных. \n'
          'Если подключены в pgAdmin 4 или в psql - отключитесь. \n'
          'Когда всё сделаете, нажмите Enter')
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
        DROP DATABASE IF EXISTS alpha_hack_db;
    """)
    conn.commit()
    conn.close()
    print('База данных удалена')


if __name__ == "__main__":
    delete_database()