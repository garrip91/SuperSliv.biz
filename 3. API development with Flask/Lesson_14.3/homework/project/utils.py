import sqlite3
import json
from pprint import pprint


def load_needed_movie(title):

    with sqlite3.connect("../../../netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
            SELECT title, country, release_year, listed_in, description
            FROM netflix
            WHERE title = '{title}'
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
        #with open(file="netflix.json", mode="a", encoding="utf-8") as file:
            #json.dump(netflix_list, file, ensure_ascii=False, indent=4)
        
        if len(netflix_list) > 1:
            dict_in_list = []
            year = 1925
            for i in netflix_list:
                if i["title"] == f"{title}":
                    if i["release_year"] > year:
                        year = i["release_year"]
                        if dict_in_list:
                            del dict_in_list[-1]
                        dict_in_list.append(i)
            return dict_in_list
        else:
            return netflix_list


def load_children_movies_list():

    with sqlite3.connect("../../../netflix.db") as connection:
        cursor = connection.cursor()
        query = """
            SELECT title, rating, description
            FROM netflix
            WHERE rating = 'G'
        """

        cursor.execute(query)

        netflix_list = []
        for row in cursor.fetchall():
            netflix_dict = {}
            netflix_dict["title"] = row[0]
            netflix_dict["rating"] = row[1]
            netflix_dict["description"] = row[2]
            netflix_list.append(netflix_dict)
    
    return netflix_list


def load_family_movies_list():

    with sqlite3.connect("../../../netflix.db") as connection:
        cursor = connection.cursor()
        query = """
            SELECT title, rating, description
            FROM netflix
            WHERE rating IN ('G', 'PG', 'PG-13')
        """

        cursor.execute(query)

        netflix_list = []
        for row in cursor.fetchall():
            netflix_dict = {}
            netflix_dict["title"] = row[0]
            netflix_dict["rating"] = row[1]
            netflix_dict["description"] = row[2]
            netflix_list.append(netflix_dict)
    
    return netflix_list


def load_adult_movies_list():

    with sqlite3.connect("../../../netflix.db") as connection:
        cursor = connection.cursor()
        query = """
            SELECT title, rating, description
            FROM netflix
            WHERE rating IN ('R', 'NC-17')
        """

        cursor.execute(query)

        netflix_list = []
        for row in cursor.fetchall():
            netflix_dict = {}
            netflix_dict["title"] = row[0]
            netflix_dict["rating"] = row[1]
            netflix_dict["description"] = row[2]
            netflix_list.append(netflix_dict)
    
    return netflix_list


#print(load_adult_movies_list())
