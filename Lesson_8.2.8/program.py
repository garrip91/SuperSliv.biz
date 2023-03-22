class Question:

    def __init__(self, question_text, question_level, true_answer, question_asked=False, user_answer=None, scores=0):
        self.question_text = question_text
        self.question_level = question_level
        self.true_answer = true_answer
        self.question_asked = question_asked
        self.user_answer = user_answer
        self.scores = scores
    
    def __str__(self):
        return f"{self.question_text}, {self.question_level}, {self.true_answer}, {self.question_asked}, {self.user_answer}, {self.scores}"


question = Question("Текст вопроса", "Уровень сложности", "Верный ответ")
print(question)
