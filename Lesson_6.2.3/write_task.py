user_language = input("Какой язык Вы учите?\n")
user_time = input("Как давно?\n")
user_institution = input("Где?\n")


with open("answers.txt", "w") as file:
    file.write(f"{user_language}\n")
    file.write(f"{user_time}\n")
    file.write(f"{user_institution}\n")


print("Ответы записаны")
