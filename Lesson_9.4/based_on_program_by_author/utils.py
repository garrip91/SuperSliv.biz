import requests
import sqlite3
import random
from config import WORDS_ON_GITHUB
from basic_word import BasicWord


def load_random_word():
    """
    Получает список слов с внешнего ресурса,
    выбирает случайное слово,
    создаёт экземпляр класса BasicWord,
    возвращает созданный экземпляр.
    """
    
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
    #word = random.choice(words_and_subwords)
    word = random.sample(words_and_subwords, 1)
    
    return word[0]


#load_random_word()
print(load_random_word())

#payload = {'key1': 'value1', 'key2': 'value2'}
#response = requests.get(WORDS_ON_GITHUB, params=payload)
#print(response.text)
