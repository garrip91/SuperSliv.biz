import json


#def load_questions():
#    """Загружает вопросы из файла"""

#    with open(file="questions.json", mode="r", encoding="utf-8") as fp:
#        questions_dict = json.load(fp)
#        return questions_dict
def load_questions_from_json():
    """Загружает вопросы из файла"""

    with open(file="questions.json", mode="r", encoding="utf-8") as fp:
        data = json.load(fp)
        return data


#def show_field():
#    """Выводит игровое поле"""

#    table = ""
#    for k, v in load_questions().items():
#        score_str_with_spaces = "   ".join([i for i in v.keys()])
#        table += f"{k}   {score_str_with_spaces}\n"
#    return table
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
#questions = load_questions_from_json()
#show_field(questions)


#def parse_input(string):
#    """Делит ввод пользователя на категорию и число"""

#    return string.split(" ")
def parse_input(user_input):
    """Делит ввод пользователя на категорию и число"""

    user_data = user_input.split(" ")
    if len(user_data) != 2:
        return False
    # ... всякая валидация
    return {"category": user_data[0], "price": user_data[1]}
#print(parse_input("Животные 100"))


#def show_question(parse_input_data):
#    """Печатает вопрос"""

#    selected = load_questions()[parse_input_data[0]][parse_input_data[1]]
#    question = f"Слово {selected['question']} в переводе означает ..."

#    return selected, question
def print_question(question_text):
    print(f"Слово {question_text} в переводе означает ...")


def show_stats():
    """Выводит статистику"""

    return None
