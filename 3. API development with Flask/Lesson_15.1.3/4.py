"""
Изменение таблицы базы данных

Таблица - books
Столбцы - id, name, author, description, genre, publication_date, pages_count, price

ADD, RENAME, DROP
"""


import sqlite3


with sqlite3.connect("books_db.sqlite") as connection:
    cursor = connection.cursor()

    query = """
        ALTER TABLE books
        DROP COLUMN publication_country
    """

    cursor.execute(query)
