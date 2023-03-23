class Question:

    def __init__(self, question_text, question_level, question_answer):
        self.question_text = question_text
        self.question_level = question_level
        self.question_answer = question_answer
        self.is_asked = False
        self.user_answer = None
        self.points = self.question_level * 10

    def get_points(self):
        pass

    def is_correct(self):
        pass

    def build_question(self):
        pass

    def build_positive_feedback(self):
        pass

    def build_negative_feedback(self):
        pass
