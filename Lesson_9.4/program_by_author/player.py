class Player:

    def __init__(self, name):
        self.name = name
        self.used_words = []
    
    def count_words(self): # ДОРАБОТАТЬ
        return 3           # МЕТОД
    
    def add_word(self, word):
        self.used_words += word
    
    def has_used(self, word):
        return word in self.used_words
