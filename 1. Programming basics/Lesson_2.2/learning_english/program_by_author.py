# Приветствуем пользователя:
print("Привет! Предлагаю проверить свои знания английского!")
user_name = input("Как тебя зовут?\n")
print(f"Привет, {user_name}. Начинаем тренировку!")

# Счётчик правильных ответов:
correct_answers = 0

# Начинаем задавать вопросы:
# Первый вопрос:
first_question = "My name __ Vova\n"
first_answer = "is"
user_answer = input(first_question)
if user_answer == first_answer:
    correct_answers += 1
    print("Ответ верный!\nВы получаете 10 баллов!")
else:
    print(F'Неправильно! Правильный ответ: "{first_answer}"')
# Второй вопрос:
second_question = "I __ a coder:\n"
second_answer = "am"
user_answer = input(second_question)
if user_answer == second_answer:
    correct_answers += 1
    print("Ответ верный!\nВы получаете 10 баллов!")
else:
    print(F'Неправильно! Правильный ответ: "{second_answer}"')
# Третий вопрос:
third_question = "I live __ Moscow:\n"
third_answer = "in"
user_answer = input(third_question)
if user_answer == third_answer:
    correct_answers += 1
    print("Ответ верный!\nВы получаете 10 баллов!")
else:
    print(F'Неправильно! Правильный ответ: "{third_answer}"')

# Количество баллов пользователя:
user_score = correct_answers * 10
# Количество процентов:
user_percentage = round((correct_answers / 3) * 100)

print(
    F"Вот и всё, {user_name}!\n"
    F"Вы ответили на {correct_answers} вопросов из 3 верно.\n"
    F"Вы заработали {user_score} баллов.\n"
    F"Это {user_percentage} процентов."
)
