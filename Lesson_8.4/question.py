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
        answer_text = f"\nВопрос: {self.question_text}\nСложность: {self.question_level}/5"
        return answer_text

    def build_positive_feedback(self):
        answer_text = f"Ответ верный, получено {self.points} баллов!"
        return answer_text

    def build_negative_feedback(self):
        answer_text = f"Ответ неверный, верный ответ - {self.question_answer} !"
        return answer_text
    
    def __repr__(self):
        return f"{self.question_text} - {self.question_answer} ({self.question_level}/5)"


# data = {
#     "q": "How many days do we have in a week?",
#     "d": "2",
#     "a": "7"
# }
#
# q_1 = Question(data.get("q"), int(data.get("d")), data.get("a"))
# print(q_1.get_points())
#
# q_1.user_answer = data.get("a")
# print(q_1.is_correct())
#
# print(q_1.build_question())
#
# print(q_1.build_positive_feedback())
#
# print(q_1.build_negative_feedback())
