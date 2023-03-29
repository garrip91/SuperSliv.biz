class Player:

    def __init__(self, name):
        self.name = name
        self.used_words = []
    
    def count_words(self):
        return len(self.used_words)
    
    def add_word(self, new_word):
        self.used_words.append(new_word)
    
    def has_used(self, word):
        return word in self.used_words
    
    def __repr__(self):
        return f"{self.name} угадал слова {', '.join(self.used_words)}"


vasily = Player("Василий")
vasily.add_word("пайтон")
vasily.add_word("словарь")
vasily.add_word("Алтай")
vasily.add_word("Борисполь")
vasily.add_word("Вологда")
#print(vasily)
#print(vasily.count_words())
#print(vasily.has_used("пайтон"))
#print(vasily.has_used("диван"))
