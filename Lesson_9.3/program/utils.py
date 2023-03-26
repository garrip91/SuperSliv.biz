import json


class BasicWord:

    def __init__(self, original_word, valid_words):
        self.original_word = original_word
        self.valid_words = valid_words
    
    def is_word_in_json_list(self) -> bool:
        with open(file="words.json", mode="r", encoding="utf-8") as file:
            words_and_subwords = json.load(file)
            for word in words_and_subwords:
                if self.original_word in list(word.items())[0]:
                    return True
                else:
                    return False

    def subwords_count(self):
        pass


basic_word = BasicWord("питон", ["пони", "тон", "ион", "опт", "пот", "тип", "топ", "пион", "понт"])
print(basic_word.is_word_in_json_list())
