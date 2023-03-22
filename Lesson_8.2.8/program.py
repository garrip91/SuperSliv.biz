class Question:

    def __init__(self, question_text, question_level, true_answer, question_asked=False, user_answer=None, scores=0):
        self.question_text = question_text
        self.question_level = question_level
        self.true_answer = true_answer
        self.question_asked = question_asked
        self.user_answer = user_answer
        self.scores = scores
    
    def get_points(self):
        """
        Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 даётся 10 баллов, за 5 даётся 50 баллов.
        """
        return int(self.question_level.split("/")[0]) * 10
    
    def __str__(self):
        """Метод для проверки класса"""
        return f"{self.question_text}\n{self.question_level}\n{self.true_answer}\n{self.question_asked}\n{self.user_answer}\n{self.scores}\n{self.get_points()}"


question = Question(question_text="What do people often call American flag?", question_level="4/5", true_answer="stars and stripes")
print(question)
