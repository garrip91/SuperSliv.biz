import json


""" data = {
    "transport": {
        100: {"bike": "велосипед", "motobike": "мотоцикл", "car": "машина"},
        200: {"train": "поезд", "bus": "автобус", "taxi": "такси"},
        300: {"airplane": "самолёт", "helicopter": "вертолёт", "airship": "дирижабль"}
    },
    "animals": {
        100: {"dog": "собака", "cat": "кошка", "rat": "крыса"},
        200: {"wolf": "волк", "tiger": "тигр", "bear": "медведь"},
        300: {"penguin": "пингвин", "elephant": "слон", "camel": "верблюд"}
    },
    "food": {
        100: {"bread": "хлеб", "cheese": "сыр", "egg": "яйцо"},
        200: {"lemon": "лимон", "potato": "картошка", "cabbage": "капуста"},
        300: {"apple": "яблоко", "orange": "апельсин", "banana": "банан"}
    }
} """
questions = {
    "Транспорт": {
        100: {"question": "plane", "answer": "самолёт", "asked": False},
        200: {"question": "train", "answer": "поезд", "asked": False},
        300: {"question": "boarding", "answer": "посадка", "asked": False}
    },
    "Животные": {
        100: {"question": "dog", "answer": "собака", "asked": False},
        200: {"question": "shark", "answer": "акула", "asked": False},
        300: {"question": "sparrow", "answer": "воробей", "asked": False}
    },
    "Еда": {
        100: {"question": "apple", "answer": "яблоко", "asked": False},
        200: {"question": "berry", "answer": "ягода", "asked": False},
        300: {"question": "venison", "answer": "оленина", "asked": False}
    }
}


with open(file="questions.json", mode="w", encoding="utf-8") as file:
    json.dump(questions, file, ensure_ascii=False, indent=4)
