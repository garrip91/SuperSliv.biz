class Question:

    def __init__(self, question_text, question_level, question_answer):
        self.question_text = question_text
        self.question_level = question_level
        self.question_answer = question_answer
        self.is_asked = False
        self.user_answer = None
        self.points = self.question_level * 10

    def get_points(self):
        return self.points

    def is_correct(self):
        return self.user_answer == self.question_answer

    def build_question(self):
        question_text = f"\nВопрос: {self.question_text}\nСложность: {self.question_level}/5"
        return question_text

    def build_positive_feedback(self):
        positive_reply_text = f"Ответ верный, получено {self.points} баллов!"
        return positive_reply_text

    def build_negative_feedback(self):
        negative_reply_text = f"Ответ неверный, верный ответ - {self.question_answer} !"
        return negative_reply_text
    
    def __repr__(self):
        return f"{self.question_text} - {self.question_answer} ({self.question_level}/5)"
