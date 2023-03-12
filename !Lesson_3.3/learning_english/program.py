from random import randrange


questions_and_answers_dict = {
    "My name __ Vova:\n": "is",
    "I __ a coder:\n": "am",
    "I live __ Moscow:\n": "in"
}

flag = None
questions_count = 0
true_answers_count = 0
false_answers_count = 3
questions_and_answers_dict_len = len(questions_and_answers_dict)

while flag == None:
    start_input_value = input('Привет! Предлагаю проверить свои знания английского! Набери "ready", чтобы начать:\n')
    if (start_input_value == "ready"):
        flag = True
    else:
        flag = False
        print("Кажется, Вы не хотите играть. Очень жаль")

while (flag == True) and (questions_count < questions_and_answers_dict_len):
    for k,v in questions_and_answers_dict.items():
        while false_answers_count == 3:
            question_answer = input(k)
            questions_count += 1
            if question_answer == v:
                print("Ответ верный!")
                true_answers_count += 1
                continue
            else:
                #print(F'Неправильно! Правильный ответ: "{v}"')
                false_answers_count -= 1
                print(F'Неправильно! Осталось попыток: {false_answers_count}')
                """ for i in range(false_answers_count):
                    false_answers_count -= 1
                    print(F'Неправильно! Осталось попыток: {false_answers_count}')
                    question_answer = input(k) """

try:
    randrange(1000000)/questions_count # произвольное целое число из диапазона от 0 до 1 000 000 (число взято не из условия задачи) делим на значение переменной чтобы получить либо ожидаемый результат либо ошибку
except:
    pass
else:
    result = round(true_answers_count*100/questions_count)
    print(F"Ну вот и всё! Вы ответили на {true_answers_count} вопросов из {questions_count} верно, это {result} процентов")
