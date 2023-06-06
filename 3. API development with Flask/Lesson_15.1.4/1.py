"""
Добавление новых значений (одиночное, множественное)
"""


import sqlite3


with sqlite3.connect("books_db.sqlite") as connection:
    cursor = connection.cursor()

    query = """
        INSERT INTO books (name, pages_count)
        VALUES ('New book 2', 53), ('Second book', 49)
    """

    cursor.execute(query)
