questions_and_answers_dict = {
    "My name __ Vova:\n": "is",
    "I __ a coder:\n": "am",
    "I live __ Moscow:\n": "in"
}

flag = False
questions_count = 0
true_answers_count = 0
questions_and_answers_dict_len = len(questions_and_answers_dict)

while flag == False:
    start_input_value = input('Привет! Предлагаю проверить свои знания английского! Набери "ready", чтобы начать:\n')
    if (start_input_value == "ready"):
        flag = True

while (flag == True) and (questions_count < questions_and_answers_dict_len):
    for k,v in questions_and_answers_dict.items():
        question_answer = input(k)
        questions_count += 1
        if question_answer == v:
            print("Ответ верный!")
            true_answers_count += 1
        else:
            print(F'Неправильно! Правильный ответ: "{v}"')

result = round(true_answers_count*100/questions_count)

print(F"Ну вот и всё! Вы ответили на {true_answers_count} вопросов из {questions_count} верно, это {result} процентов")
