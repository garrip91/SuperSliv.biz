"""
Удаление строк из таблицы
"""


import sqlite3


with sqlite3.connect("books_db.sqlite3") as connection:
    cursor = connection.cursor()

    #query = """
    #    CREATE TABLE genres (
    #        id INTEGER PRIMARY KEY AUTOINCREMENT,
    #        name VARCHAR(100) NOT NULL
    #    );
    #"""
    #query = """
    #    CREATE TABLE books (
    #        id INTEGER PRIMARY KEY AUTOINCREMENT,
    #        name VARCHAR(100) NOT NULL,
    #        genre_id INTEGER,
    #        FOREIGN KEY (genre_id) REFERENCES genres(id) ON DELETE SET NULL ON UPDATE CASCADE
    #    );
    #"""
    #query = """
    #    CREATE TABLE author (
    #        id INTEGER PRIMARY KEY AUTOINCREMENT,
    #        name VARCHAR(100) NOT NULL
    #    );
    #"""
    #query = """
    #    CREATE TABLE book_author (
    #        book_id INTEGER,
    #        author_id INTEGER,
    #        PRIMARY KEY (book_id, author_id),
    #        FOREIGN KEY (book_id) REFERENCES books(id),
    #        FOREIGN KEY (author_id) REFERENCES author(id)
    #    );
    #"""
    #query = """
    #    INSERT INTO genres (name)
    #    VALUES ('Horror'), ('Sci-Fi');
    #"""
    #query = """
    #    INSERT INTO author (name)
    #    VALUES ('Author 1'), ('Author 2'), ('Author 3');
    #"""
    #query = """
    #    INSERT INTO books (name, genre_id)
    #    VALUES ('Book 1', 1), ('Book 2', 2), ('Book 3', 2);
    #"""
    #query = """
    #    INSERT INTO book_author (book_id, author_id)
    #    VALUES (1, 1), (2, 1), (2, 3);
    #"""
    query = """
        SELECT
            books.name AS 'book_name',
            genres.name AS 'genre_name',
            author.name AS 'author_name',
            book_author.*
        FROM books
        INNER JOIN genres ON books.genre_id = genres.id
        INNER JOIN book_author ON books.id = book_author.book_id
        LEFT JOIN author ON book_author.author_id = author.id;
    """

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)
