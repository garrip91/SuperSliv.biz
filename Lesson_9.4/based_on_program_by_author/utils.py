import requests
import sqlite3
import random
from config import WORDS_ON_GITHUB
from basic_word import BasicWord


def load_random_word():
    #path = WORDS_ON_GITHUB
    #response = requests.get(WORDS_ON_GITHUB)
    #print(response.text)

    #data = {
    #    "word": "набор",
    #    "sub_words": [
    #        "бар", "бон", "бор", "раб", "бра", "боа", "нора", "роба", "барон"
    #    ]
    #}
    #word = BasicWord(data["word"], data["sub_words"])
    #return word
    
    # Настраиваем подключение к базе данных:
    conn = sqlite3.connect('DATA.db')
    # Настраиваем "курсор", с помощью которого будем обращаться к БД:
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, word, sub_word FROM words_and_subwords")
    words_and_subwords = []
    for line in cursor.fetchall():
        words_and_subwords.append(BasicWord(
            line[1],
            line[2]
        ))

    random.shuffle(words_and_subwords)
    word = random.sample(words_and_subwords, 1)
    return word


#load_random_word()
print(load_random_word())

#payload = {'key1': 'value1', 'key2': 'value2'}
#response = requests.get(WORDS_ON_GITHUB, params=payload)
#print(response.text)
