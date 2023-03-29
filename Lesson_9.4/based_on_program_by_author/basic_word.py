class BasicWord:

    def __init__(self, word, sub_words):
        self.word = word
        self.sub_words = sub_words.split(", ")
    
    def has_subword(self, candidate):              # ДОРАБОТАТЬ
        return candidate.lower() in self.sub_words # МЕТОД
    
    def subwords_count(self):         # ДОРАБОТАТЬ
        return len(self.sub_words)                      # МЕТОД
    
    #def __repr__(self):
    #    return f"Составьте {self.subwords_count()} слов из слова {self.word.upper()}"
    
    #def from_list_to_str(self):
    #    pass


#basic_word = BasicWord("питон", "пони, тон, ион, опт, пот, тип, топ, пион, понт")
#print(basic_word.has_subword("123"))
