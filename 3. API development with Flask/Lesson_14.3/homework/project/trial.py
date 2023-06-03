import sqlite3


def load_movies():

    with sqlite3.connect("../../../netflix.db") as connection:
        cursor = connection.cursor()
        query = """
            SELECT type, title, country, release_year, listed_in, description
            FROM netflix
            WHERE type = 'Movie'
            LIMIT 5
        """

        cursor.execute(query)

        netflix_list = []
        for row in cursor.fetchall():
            netflix_dict = {}
            netflix_dict["type"] = row[0]
            netflix_dict["title"] = row[1]
            netflix_dict["country"] = row[2]
            netflix_dict["release_year"] = row[3]
            netflix_dict["genre"] = row[4]
            netflix_dict["description"] = row[5]
            netflix_list.append(netflix_dict)
        #with open(file="netflix.json", mode="a", encoding="utf-8") as file:
            #json.dump(netflix_list, file, ensure_ascii=False, indent=4)
    return netflix_list

#print(type(load_movies()))


dicts_in_list = [
    {
        'type': 'Movie',
        'title': '7:19',
        'country': 'Mexico',
        'release_year': 2016,
        'genre': 'Dramas,International Movies',
        'description': 'After a devastating earthquake hits Mexico City, trapped survivors from all walks of life wait to be rescued while trying desperately to stay alive.\n'
    },
    {
        'type': 'Movie',
        'title': '23:59',
        'country': 'Singapore',
        'release_year': 2011,
        'genre': 'Horror Movies, International Movies',
        'description': "When an army recruit is found dead, his fellow soldiers are forced to confront a terrifying secret that's haunting their jungle island training camp.\n"
    },
    {
        'type': 'Movie',
        'title': '9',
        'country': 'United States',
        'release_year': 2009,
        'genre': 'Action & Adventure, Independent Movies, Sci-Fi & Fantasy',
        'description': 'In a postapocalyptic world, rag-doll robots hide in fear from dangerous machines out to exterminate them, until a brave newcomer joins the group.\n'
    },
    {
        'type': 'Movie',
        'title': '21',
        'country': 'United States',
        'release_year': 2008,
        'genre': 'Dramas',
        'description': 'A brilliant group of students become card-counting experts with the intent of swindling millions out of Las Vegas casinos by playing blackjack.\n'
    },
    {
        'type': 'Movie',
        'title': '122',
        'country': 'Egypt',
        'release_year': 2019,
        'genre': 'Horror Movies, International Movies',
        'description': 'After an awful accident, a couple admitted to a grisly hospital are separated and must find each other to escape — before death finds them.\n'
    }
]


items_count = []
dict_in_list = []
year = 1925
for i in dicts_in_list:
    if i["type"] == "Movie":
        if i["release_year"] > year:
            year = i["release_year"]
            if dict_in_list:
                del dict_in_list[-1]
            dict_in_list.append(i)

#print(dict_in_list)
