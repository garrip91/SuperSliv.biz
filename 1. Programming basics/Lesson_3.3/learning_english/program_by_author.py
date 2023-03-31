# Задаём список вопросов
questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
# Задаём список ответов
answers = ["is", "am", "in"]
# Задаём кол-во правильных ответов = 0
correct_count = 0
# Задаём кол-во неправильных ответов = 0
incorrect_count = 0

# Здороваемся
print("Привет! Предлагаю проверить свои знания английского!")
print("Набери \"ready\", чтобы начать:\n")
# Получаем ввод пользователя
user_input = input()
# Сравниваем с ready
# Если нет:
if user_input != "ready":
#     Кажется, Вы не хотите играть. Очень жаль
    print("Кажется, Вы не хотите играть. Очень жаль")
else:
# Запускаем цикл по вопросам, используя индексы:
    for i in range(len(questions)):
# Для каждого индекса
#     Выводим вопрос
        question_text = questions[i]
        answer_text = answers[i]
        print(question_text)
#     Получаем ответ
        user_input = input()
#     Сравниваем с правильным ответом
#     Ответы совпадают?
#     Если да:
        if user_input == answer_text:
#         Выводим, что ответ верный!
            print("Ответ верный!")
#         кол-во правильных ответов += 1
            correct_count += 1
#     Если нет:
        else:
#         Выводим, что ответ неверный, правильный ответ: ___
            print(f"Неправильно! Правильный ответ: {answer_text}")
            incorrect_count += 1

# Всего вопросов
questions_total = len(questions)
# Считаем проценты
correct_percent = round((correct_count / questions_total) * 100)
# Вывести "Вот и всё! Вы ответили на ___ вопросов из ___ верно, это ___ процентов."
print(f"Ну вот и всё! Вы ответили на {correct_count} вопросов "
      f"из {questions_total} верно, "
      f"это {correct_percent} процентов")
