import json


def load_questions_from_json():
    """Загружает вопросы из файла"""

    with open(file="questions.json", mode="r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def show_field(questions):
    """Выводит игровое поле"""

    for category_name, category_question in questions.items():
        print(category_name.ljust(17), end="")
        for price, question_data in category_question.items():
            asked = question_data["asked"]
            if not asked:
                print(price.ljust(5), end=" ")
            else:
                print("   ".ljust(5), end=" ")
        print()


def parse_input(user_input):
    """Делит ввод пользователя на категорию и число"""

    user_data = user_input.split(" ")
    if len(user_data) != 2:
        return False
    if not user_data[0].isalpha():
        return False
    if not user_data[1].isdigit():
        return False
    return {"category": user_data[0], "price": user_data[1]}


def print_question(question_text):
    """Печатает вопрос"""

    print(f"Слово {question_text} в переводе означает ...")


def show_stats(points, correct, incorrect):
    """Выводит статистику"""

    print("У нас закончились вопросы!")
    print("")
    print(f"Ваш счёт: {points}")
    print(f"Верных ответов: {correct}")
    print(f"Неверных ответов: {incorrect}")


def save_results_to_file(points, correct, incorrect):
    """Записывает результаты в JSON-файл"""

    with open(file="results.json", mode="r", encoding="utf-8") as file:
        results = json.load(file)

    results.append({
        "points": points,
        "correct": correct,
        "incorrect": incorrect
    })

    with open(file="results.json", mode="w", encoding="utf-8") as file:
        results = json.dump(results, file)


def get_number_of_questions(questions):
    """Получает общее количество вопросов"""
    counter = 0
    for cat_questions in questions.values():
        counter += len(cat_questions)
    return counter
