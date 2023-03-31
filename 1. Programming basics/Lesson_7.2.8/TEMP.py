import json

from utils import load_questions


with open(file="questions.json", mode="r", encoding="utf-8") as fp:
    questions_dict = json.load(fp)
    table = ""
    for k, v in questions_dict.items():
        score_str_with_spaces = "   ".join([i for i in v.keys()])
        table += f"{k}   {score_str_with_spaces}\n"
    #print(table)


for k, v in load_questions().items():
    print(k, v)
    """
    Транспорт {'100': {'question': 'plane', 'answer': 'самолёт', 'asked': False}, '200': {'question': 'train', 'answer': 'поезд', 'asked': False}, '300': {'question': 'boarding', 'answer': 'посадка', 'asked': False}}
    Животные {'100': {'question': 'dog', 'answer': 'собака', 'asked': False}, '200': {'question': 'shark', 'answer': 'акула', 'asked': False}, '300': {'question': 'sparrow', 'answer': 'воробей', 'asked': False}}
    Еда {'100': {'question': 'apple', 'answer': 'яблоко', 'asked': False}, '200': {'question': 'berry', 'answer': 'ягода', 'asked': False}, '300': {'question': 'venison', 'answer': 'оленина', 'asked': False}}
    """
