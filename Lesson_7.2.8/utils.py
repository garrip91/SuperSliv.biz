import json


#def load_questions():
#    """Загружает вопросы из файла"""

#    with open(file="questions.json", mode="r", encoding="utf-8") as fp:
#        questions_dict = json.load(fp)
#        return questions_dict
#print(type(load_questions()))
#print(load_questions())
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
#print(show_field())
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
questions = load_questions_from_json()
show_field(questions)


def parse_input(string):
    """Делит ввод пользователя на категорию и число"""

    return string.split(" ")
#print(parse_input("Транспорт 400"))


def show_question(parse_input_data):
    """Печатает вопрос"""

    selected = load_questions()[parse_input_data[0]][parse_input_data[1]]
    question = f"Слово {selected['question']} в переводе означает ..."

    return selected, question
#print(show_question()


def show_stats():
    """Выводит статистику"""

    return None
