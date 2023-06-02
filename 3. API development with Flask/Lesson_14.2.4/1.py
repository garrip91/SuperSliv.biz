"""
Агрегирующие функции

COUNT()
DISTINCT
MIN()
MAX()
AVG()
SUM()
"""


import sqlite3


with sqlite3.connect("../netflix.db") as connection:
    cursor = connection.cursor()
    query = """
        SELECT country, SUM(duration) AS total_duration
        FROM netflix
        WHERE type = 'TV Show'
        AND country != ''
        GROUP BY country
        ORDER BY total_duration DESC
        LIMIT 10
    """

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)
