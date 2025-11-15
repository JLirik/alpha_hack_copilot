## Настройка базы данных

1. Установите PostgreSQL локально
2. Установите расширение pgvector: https://github.com/pgvector/pgvector.
3. Введите в терминал команду `pip install python-dotenv`.
4. Создайте файл `.env` в соответствии с `.env.example`.
5. Заполните своими значениями. Файл `.env` локален на вашем компьютере.
6. Для создания БД запустите файл `db\scripts\init_db.py`.
7. Создайте базу знаний. Для этого запустите
   файл `ml_learning\knowledge_base.py`.
8. Все функции размещены в файле `db\scripts\operations_db.py`.
   В случае неполадок БД можно удалить `db\scripts\delete_db.py`.