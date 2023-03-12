import copy


def check_pin(pin: str) -> bool:
    """ Проверяет является ли строка четырёхбуквенным пин-кодом """


    if (len(pin) != 4) or (pin[0]==pin[1]==pin[2]==pin[3]) or (pin == "1234"):
        return False
    else:
        return True


def check_pass(pswd: str) -> bool:
    """ Проверяет, чтобы пароль был не меньше 8-и символов, а также содержал буквы и цифры """


    if (len(pswd) < 8) or (pswd.isalpha()) or (pswd.isdigit()):
        return False
    else:
        return True


def check_mail(mail: str) -> bool:
    """ Проверяет наличие символов \"@\" и \".\" """


    if ("@" not in mail) or ("." not in mail):
        return False
    else:
        return True


def check_name(name: str) -> bool:
    """ Проверяет содержание в имени только кириллических символов и пробелов """


    russian_alphabet_upper = [chr(i) for i in range(1040, 1071+1)]
    russian_alphabet_upper.insert(6, chr(1025))
    russian_alphabet_lower = [chr(i) for i in range(1072, 1103+1)]
    russian_alphabet_lower.insert(6, chr(1105))
    russian_alphabet = russian_alphabet_upper + russian_alphabet_lower
    russian_alphabet_and_empty_space_1 = copy.deepcopy(russian_alphabet)
    russian_alphabet_and_empty_space_1.append(" ")
    result = ""
    for i in name:
        if i not in russian_alphabet_and_empty_space_1:
            return False
        else:
            result += i
    if (result[0] == " ") or (result[-1] == " "):
        return False
    else:
        return True
