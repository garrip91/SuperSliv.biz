alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "


def checkname(name):
    
    for letter in name:
        if letter.lower() not in alphabet:
            return False
    return True

print(checkname("Василий1"))
