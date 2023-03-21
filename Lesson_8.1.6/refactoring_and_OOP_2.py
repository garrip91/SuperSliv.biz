#question_1 = "My name __ Vova"
#correct_1 = "is"
#
#answer = input("Введите ответ")
#
#if answer == correct_1:
#    print("Ответ верный!")
#else:
#    print("Ответ неверный!")
#    print("Верный:", correct_1)

class Question:

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    
    def check(self, answer):
        return answer == self.answer


question_1 = Question("Текст вопроса?", "Правильный ответ!")

print(question_1.check("test"))
print(question_1.check("Правильный ответ!"))
