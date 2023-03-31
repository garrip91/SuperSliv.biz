import random


name = input("Введите Ваше имя:\n")

points = 0
with open(file="words.txt", mode="r", encoding="utf-8") as file:
    words = file.read().split("\n")
    for word in words:
        user_input = input(f"Угадайте слово: {''.join(random.sample(word, len(word)))}\n")
        if user_input == word:
            print(f"Верно! Вы получаете 10 очков")
            points += 10
        else:
            print(f"Неверно! Верный ответ - {word}.")
    with open(file="history.txt", mode="a", encoding="utf-8") as file:
        file.write(f"{name} - {points}\n")

print(words())
