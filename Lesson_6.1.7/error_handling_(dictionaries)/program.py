errors = {
    "out": "Вы вышли из системы",
    "noaccess": "У Вас нет доступа в этот раздел",
    "unknown": "Неизвестная ошибка",
    "timeout": "Система долго не отвечает",
    "robot": "Ваши действия похожи на автоматические",
}

def get_errors(*error):
    """Функция возвращает набор ошибок списком в ответ на список аргументов, который был ей передан"""


    result = []
    for i in error:
        result.append(errors[i])
    #return list(errors[error])
    return result


#print(get_errors("robot", "unknown", "out"))
print(get_errors("out", "noaccess"))
