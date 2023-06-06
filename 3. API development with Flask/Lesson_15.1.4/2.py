"""
Редактирование строк в таблице (полное, условное)

Примеры:
    - добавление описания книги
    - переименовать жанр
    - увеличить стоимость на 10%
"""


import sqlite3


with sqlite3.connect("books_db.sqlite") as connection:
    cursor = connection.cursor()

    query = """
        UPDATE books
        SET price = price + 30
        WHERE id IN (1, 2)
    """

    cursor.execute(query)
