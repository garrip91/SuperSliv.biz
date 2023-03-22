class Question:

    def __init__(self, question_text, question_level, true_answer, question_asked=False, user_answer=None, scores=0):
        """
        Наш инициализатор.
        """
        self.question_text = question_text
        self.question_level = question_level
        self.true_answer = true_answer
        self.question_asked = question_asked
        self.user_answer = user_answer
        self.scores = scores
    
    def get_points(self) -> int:
        """
        Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 даётся 10 баллов, за 5 даётся 50 баллов.
        """
        return int(self.question_level.split("/")[0]) * 10
    
    def is_correct(self) -> bool:
        """
        Возвращает True, если ответ пользователя совпадает с верным ответом, иначе False.
        """
        return True if self.user_answer==self.true_answer else False
    
    def build_question(self) -> str:
        """
        Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        (то есть, возвращает строковый тип данных)
        Сложность 4/5.
        """
        return self.question_text
    
    def build_positive_or_negative_feedback(self) -> str:
        """
        Возвращает: Ответ верный, получено __ баллов! - в случае верного ответа;
        Ответ неверный, верный ответ: __ ! - в случае неверного ответа.
        """
        if self.is_correct():
            return f"Ответ верный, получено {self.scores} баллов!"
        else:
            return f"Ответ неверный, верный ответ: {self.true_answer} !"
    
    def __str__(self):
        """
        Метод для проверки класса.
        """
        return f"{self.question_text}\n{self.question_level}\n{self.true_answer}\n{self.question_asked}\n{self.user_answer}\n{self.scores}\n{self.get_points()}\n{self.is_correct()}\n{self.build_question()}\n{self.build_positive_or_negative_feedback()}"


question = Question(question_text="What do people often call American flag?", question_level="4/5", true_answer="stars and stripes", question_asked=False, user_answer="!stars and stripes", scores=0)
print(question)
