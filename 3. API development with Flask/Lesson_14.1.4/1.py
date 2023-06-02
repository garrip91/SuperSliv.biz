"""
Подключение к SQLite 3
"""


import sqlite3


#connection = sqlite3.connect("netflix.db")
#cursor = connection.cursor()
#cursor.execute("ЗДЕСЬ БУДУТ НАШИ КОМАНДЫ")
#connection.close()

with sqlite3.connect("../netflix.db") as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM netflix LIMIT 10 OFFSET 10")

    for row in cursor.fetchall():
        print(row)
