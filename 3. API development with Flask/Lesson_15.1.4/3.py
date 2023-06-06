"""
Удаление строк из таблицы
"""


import sqlite3


with sqlite3.connect("books_db.sqlite") as connection:
    cursor = connection.cursor()

    query = """
        DELETE FROM books
        WHERE price < 130
    """

    cursor.execute(query)
