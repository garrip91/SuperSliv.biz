# chr(1025) == "Ё"
# chr(1105) == "ё"

english_alphabet_upper = [chr(i) for i in range(65, 90+1)]
english_alphabet_lower = [chr(i) for i in range(97, 122+1)]
russian_alphabet_upper = [chr(i) for i in range(1040, 1071+1)]
russian_alphabet_upper.insert(6, chr(1025))
russian_alphabet_lower = [chr(i) for i in range(1072, 1103+1)]
russian_alphabet_lower.insert(6, chr(1105))
ru_en_alphabet = english_alphabet_upper + english_alphabet_lower + russian_alphabet_upper + russian_alphabet_lower


def shift_encode(string):
    """Шифрует строку"""


    result = ""
    for i in string:
        if i == "Z":
            result += "A"
        elif i == "z":
            result += "a"
        elif i == "Я":
            result += "А"
        elif i == "я":
            result += "а"
        else:
            result += ru_en_alphabet[ru_en_alphabet.index(i)+1]
    return result


def shift_decode(string):
    """Дешифрует строку обратно"""


    result = ""
    for i in string:
        if i == "A":
            result += "Z"
        elif i == "a":
            result += "z"
        elif i == "А":
            result += "Я"
        elif i == "а":
            result += "я"
        else:
            result += ru_en_alphabet[ru_en_alphabet.index(i)-1]
    return result


#print(shift_encode("ябеда"))
print(shift_decode("авёеб"))
#print(ru_en_alphabet)
