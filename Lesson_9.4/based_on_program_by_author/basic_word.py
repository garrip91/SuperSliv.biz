class BasicWord:

    def __init__(self, word, sub_words):
        self.word = word
        self.sub_words = sub_words.split(", ")
    
    def has_subword(self, candidate) -> bool:
        """Проверяет наличие/отсутствие введённого слова в списке допустимых подслов (возвращает bool)."""
        return candidate.lower() in self.sub_words
    
    def subwords_count(self) -> int:
        """Ведёт подсчёт количества подслов (возвращает int)."""
        return len(self.sub_words)
    
    #def __repr__(self):
    #    return f"Составьте {self.subwords_count()} слов из слова {self.word.upper()}"


#basic_word = BasicWord("питон", "пони, тон, ион, опт, пот, тип, топ, пион, понт")
#print(basic_word.has_subword("123"))
