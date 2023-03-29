import requests
from config import WORDS_ON_GITHUB
from basic_word import BasicWord


def load_random_word():
    path = WORDS_ON_GITHUB
    #response = requests.get(WORDS_ON_GITHUB)
    #print(response.text)
    data = {
        "word": "набор",
        "sub_words": [
            "бар", "бон", "бор", "раб", "бра", "боа", "нора", "роба", "барон"
        ]
    }
    word = BasicWord(data["word"], data["sub_words"])
    return word


#print(load_random_word())

payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.get(WORDS_ON_GITHUB, params=payload)
print(response.text)
