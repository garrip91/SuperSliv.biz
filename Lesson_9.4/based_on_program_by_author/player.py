class Player:

    def __init__(self, name):
        self.name = name
        self.used_words = []
    
    def used_words_count(self) -> int:
        """Получает количество использованных слов (возвращает int)."""
        return len(self.used_words)
    
    def add_word(self, new_word):
        """Добавляет слова в список использованных (ничего не возвращает)."""
        self.used_words.append(new_word)
    
    def has_used(self, word) -> bool:
        """Проверка введённого слова на повторное использование (возвращает bool)."""
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
#print(vasily.used_words_count())
#print(vasily.has_used("пайтон"))
#print(vasily.has_used("диван"))
