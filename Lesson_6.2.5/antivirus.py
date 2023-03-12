virus_code = "Я вирус!"

with open("answers.py") as file:
    content = file.read()
    if virus_code in content:
        print("Обнаружен вирус!")
    else:
        print("Вирусов не обнаружено!")
