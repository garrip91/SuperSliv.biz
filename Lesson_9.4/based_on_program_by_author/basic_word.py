class BasicWord:

    def __init__(self, word, sub_words):
        self.word = word
        self.sub_words = sub_words
    
    def has_subwords(self, candidate):              # ДОРАБОТАТЬ
        return candidate.lower() in self.sub_words # МЕТОД
    
    def subwords_count(self):         # ДОРАБОТАТЬ
        return len(self.sub_words.split(", "))                      # МЕТОД
    
    def __repr__(self):
        return f"{self.word} содержит {self.subwords_count()} слов"


#basic_word = BasicWord("питон", "пони, тон, ион, опт, пот, тип, топ, пион, понт")
#print(basic_word)
