import sqlite3
import json


with sqlite3.connect("../../../netflix.db") as connection:
    cursor = connection.cursor()
    query = """
        SELECT title, country, release_year, listed_in, description
        FROM netflix
        WHERE title = 'A Single Man'
    """

    cursor.execute(query)

    netflix_list = []
    for row in cursor.fetchall():
        netflix_dict = {}
        netflix_dict["title"] = row[0]
        netflix_dict["country"] = row[1]
        netflix_dict["release_year"] = row[2]
        netflix_dict["genre"] = row[3]
        netflix_dict["description"] = row[4]
        netflix_list.append(netflix_dict)
    with open(file="netflix.json", mode="a", encoding="utf-8") as file:
        json.dump(netflix_list, file, ensure_ascii=False, indent=4)


print(netflix_list)
