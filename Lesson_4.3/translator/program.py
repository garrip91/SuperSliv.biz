easy = {"word1.1": "слово1.1", "word1.2": "слово1.2", "word1.3": "слово1.3", "word1.4": "слово1.4", "word1.5": "слово1.5"}
medium = {"word2.1": "слово2.1", "word2.2": "слово2.2", "word2.3": "слово2.3", "word2.4": "слово2.4", "word2.5": "слово2.5"}
hard = {"word3.1": "слово3.1", "word3.2": "слово3.2", "word3.3": "слово3.3", "word3.4": "слово3.4", "word3.5": "слово3.5"}

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично"
}

answers = {}

level_input = input(f"Выберите уровень сложности среди вариантов \"Лёгкий\", \"Средний\" и \"Сложный\":\n")

words = None
if level_input == "Лёгкий":
    words = easy
elif level_input == "Средний":
    words = medium
elif level_input == "Сложный":
    words = hard
else:
    print("Так как Вы не ввели ни один из трёх предложенных вариантов, мы приходим к выводу, что Вы не хотите играть в англо-русский переводчик. Очень жаль, до свидания!")

results = {}
if (level_input == "Лёгкий") or (level_input == "Средний") or (level_input == "Сложный"):
    for k, v in words.items():
        input("нажмите Enter")
        question_input = input(f"{k}, {len(v)} букв, начинается на {v[0]}...:\n")
        if question_input == v:
            print(f"Верно. {k.title()} - это {v}")
            results[k] = True
        else:
            print(f"Неверно. {k.title()} - это {v}")
            results[k] = False

correct_answers_words = []
incorrect_answers_words = []
for k, v in results.items():
    if v == True:
        correct_answers_words.append(k)
    elif v == False:
        incorrect_answers_words.append(k)

if correct_answers_words and incorrect_answers_words:
    print("\n")
    print("Вы правильно ответили на вопросы про:")
    print("\n".join(correct_answers_words))
    print("Вы неправильно ответили на вопросы про:")
    print("\n".join(incorrect_answers_words))
elif correct_answers_words and not incorrect_answers_words:
    print("\n")
    print("Вы на все вопросы ответили правильно!")
    print("\n")
elif not correct_answers_words and incorrect_answers_words:
    print("\n")
    print("Вы на все вопросы ответили неправильно!")
    print("\n")

print(f"Ваш ранг:\n{levels[len(correct_answers_words)]}")
