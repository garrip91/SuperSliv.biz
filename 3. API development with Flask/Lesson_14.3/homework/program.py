import sqlite3
import json


with sqlite3.connect("../../netflix.db") as connection:
    cursor = connection.cursor()
    query = """
        SELECT title, country, release_year, listed_in, description
        FROM netflix
        LIMIT 100
    """

    cursor.execute(query)

    for row in cursor.fetchall():
        #print(row)
        for sub_row in row:
            print(sub_row)
