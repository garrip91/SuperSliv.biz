import json


def load_json():
    with open(file="words.json", mode="r", encoding="utf-8") as file:
        words_and_subwords = json.load(file)
    return words_and_subwords


class BasicWord:

    def __init__(self, original_word, valid_words):
        self.original_word = original_word
        self.valid_words = valid_words
    
    def is_word_in_json_list(self) -> bool:
        for word in load_json():
            if self.original_word in list(word.items())[0]:
                return True
            else:
                return False

    def subwords_count(self):
        if self.is_word_in_json_list():
            for word in load_json():
                return len(list(word.items())[1][1])
        else:
            return None
        
        #for word in load_json():
        #    if self.original_word in list(word.items())[0]:
        #        return True
        #    else:
        #        return False


basic_word = BasicWord("питон", ["пони", "тон", "ион", "опт", "пот", "тип", "топ", "пион", "понт"])
#print(basic_word.is_word_in_json_list())

print(basic_word.subwords_count())
