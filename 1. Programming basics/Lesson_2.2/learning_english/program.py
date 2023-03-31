questions_and_answers_dict = {    # Заводим
    "My name __ Vova:\n": "is",   # словарик и заполняем
    "I __ a coder:\n": "am",      # его вопросами и
    "I live __ Moscow:\n": "in"   # правильными ответами на
}                                 # них

flag = False # заводим переменную-флаг для отработки кода
questions_count = 0 # заводим переменную-счётчик для подсчёта количества вопросов
true_answers_count = 0 # заводим переменную-счётчик для подсчёта количества правильных ответов
scores = 0 # заводим переменную-счётчик для подсчёта количества набранных баллов
questions_and_answers_dict_len = len(questions_and_answers_dict) # считаем количество вопросов в словарике

while flag == False:
    print("Привет! Предлагаю проверить свои знания английского!")
    start_input_value = input("Расскажи как тебя зовут:\n")
    if start_input_value:
        flag = True
        print(f"Привет, ({start_input_value}), начинаем тренировку!")

while (flag == True) and (questions_count < questions_and_answers_dict_len):
    for k,v in questions_and_answers_dict.items():
        question_answer = input(k)
        questions_count += 1
        if question_answer == v:
            print("Ответ верный!")
            true_answers_count += 1
            scores += 10
        else:
            print(F'Неправильно! Правильный ответ: "{v}"')

result = round(true_answers_count*100/questions_count)

print(f"Вот и всё, ({start_input_value})! Вы ответили на {true_answers_count} вопросов из {questions_count}. Вы заработали {scores} баллов. Это {result}%")
