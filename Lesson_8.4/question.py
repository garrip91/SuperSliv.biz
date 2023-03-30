class Question:

    def __init__(self, question_text, question_level, question_answer):
        self.question_text = question_text
        self.question_level = question_level
        self.question_answer = question_answer
        self.is_asked = False
        self.user_answer = None
        self.points = self.question_level * 10

    def get_points(self) -> int:
        """
        Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 даётся 10 баллов, за 5 - 50.
        """
        return self.points

    def is_correct(self) -> bool:
        """Возвращает True, если ответ пользователя совпадает с верным ответом, иначе - False."""
        return self.user_answer == self.question_answer

    def build_question(self) -> str:
        """
        Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность: 4/5.
        """
        question_text = f"\nВопрос: {self.question_text}\nСложность: {self.question_level}/5"
        return question_text

    def build_positive_feedback(self) -> str:
        """
        Возвращает:
        Ответ верный, получено __ баллов.
        """
        positive_reply_text = f"Ответ верный, получено {self.points} баллов!"
        return positive_reply_text

    def build_negative_feedback(self) -> str:
        """
        Возвращает:
        Ответ неверный, верный ответ - __.
        """
        negative_reply_text = f"Ответ неверный, верный ответ - {self.question_answer} !"
        return negative_reply_text
    
    def __repr__(self):
        return f"{self.question_text} - {self.question_answer} ({self.question_level}/5)"
