import json
import random


#print("Сегодня мы потренируемся расшифровывать азбуку Морзе")
#start = input("Нажмите Enter и начнём")

words = ["code", "bit", "list", "soul", "next"]
answers = []


def get_word():
    """Возвращает случайное слово из списка"""


    random_word = random.sample(words, 1)[0]
    result = random_word[:]
    return result


def morse_encode(sentence=get_word()):
    """Переводит слова на английском языке в последовательности точек и тире"""


    with open(file="morse-code.json", mode="r", encoding="UTF-8") as f:
        json_dict = json.load(f)
        result = ""
        for i in sentence:
            for k, v in json_dict.items():
                if k == i:
                    result += f"{v}|"
                else:
                    continue
        result = result[:-1].replace("|", " ")
    return result


def print_statistics():
    """Выводит какую-то статистику"""


    pass

#print(get_word())
""" print("Сегодня мы потренируемся расшифровывать морзянку.")
start = input("Нажмите Enter и начнём")


n = 1
for i in range(len(words)):
    print(f"{morse_encode()} - это {get_word()}")
    user_answer = input(f"Слово {n} - {morse_encode()}:\n")
    if user_answer == get_word():
        print(f"Верно, {get_word()}!")
    else:
        print(f"Неверно, {get_word()}!")
    n += 1 """
