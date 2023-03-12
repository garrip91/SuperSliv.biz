words_easy = {"cat":"котенка","dog":"собаня","owl":"совуня"}
words_medium = {"river":"речка","mirror":"зеркало","divide":"разделять"}
words_hard = {"usual":"обычный","library":"библиотека","execute":"выполнять"}

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}

answers = {}

print("Выберите уровень сложности")
print("Лёгкий, средний, сложный")

user_answer = input().lower()

if user_answer == "средний":
    words = words_medium
elif user_answer == "сложный":
    words = words_hard
else:
    words = words_easy

words_count = len(words)

print(f"Выбран уровень сложности, мы предложим {words_count} слов, подберите перевод")

for word_en, word_ru in words.items():
    
    print("нажмите Enter")
    input()
    ...
    
    letter_count = len(word_ru)
    first_letter = word_ru[0]
    
    print(f"{word_en}, {letter_count} букв, начинается на {first_letter}...")
    
    user_answer = input().lower()

    if user_answer == word_ru:
        print(f"Верно, {word_en.title()} это {word_ru}")
        answers[word_en] = True
    
    else:
        print(f"Неверно, {word_en.title()} это {word_ru}")
        answers[word_en] = False

correct_words = []
incorrect_words = []

for word_en, is_correct in answers.items():
    if is_correct:
        correct_words.append(word_en)
    else:
        incorrect_words.append(word_en)

print("Правильно отвечены слова:")
print("\n".join(correct_words))
print("Неправильно отвечены слова:")
print("\n".join(incorrect_words))

""" Выводим уровень пользователя """

correct_count = len(correct_words)
user_level = levels[correct_count]

print()
print("Ваш ранг:")
print(f"{user_level}")
