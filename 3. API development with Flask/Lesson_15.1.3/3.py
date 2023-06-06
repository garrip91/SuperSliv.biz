"""
Полноценная таблица с индексами и ограничением столбцов

Таблица - books
Столбцы - name, author, description, genre, publication_date, pages_count, price
Первичный ключ - id
Индекс - name
Ограничения:
    - обязательный name
    - pages_count > 0
    - genre по умолчанию Undefined

Типы - bit, int, decimal, float, date, time, datetime, varchar
Модификаторы - AUTOINCREMENT (платформо-зависимый)
"""


import sqlite3


with sqlite3.connect("books_db.sqlite") as connection:
    cursor = connection.cursor()

    query = """
        CREATE TABLE books (
            id integer PRIMARY KEY AUTOINCREMENT,
            name varchar(40) NOT NULL,
            author varchar(80),
            description varchar(255),
            genre varchar(20) CONSTRAINT df_genre DEFAULT 'Undefined',
            publication_date date,
            pages_count integer CONSTRAINT ck_pages_count CHECK ( pages_count > 0 ),
            price decimal
        )
    """

    index_query = """
        CREATE INDEX book_name_idx on books (name)
    """

    cursor.execute(query)
    cursor.execute(index_query)
