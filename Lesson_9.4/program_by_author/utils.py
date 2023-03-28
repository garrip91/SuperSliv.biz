from config import WORDS_ON_GITHUB
from basic_word import BasicWord


def load_random_word():
    path = WORDS_ON_GITHUB
    data = {
        "word": "набор",
        "sub_words": [
            "бар", "бон", "бор", "раб", "бра", "боа", "нора", "роба", "барон"
        ]
    }
    word = BasicWord(data["word"], data["sub_words"])
    print(word)
