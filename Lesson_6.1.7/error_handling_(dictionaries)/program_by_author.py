all_errors = {
    "out": "Вы вышли из системы",
    "noaccess": "У Вас нет доступа в этот раздел",
    "unknown": "Неизвестная ошибка",
    "timeout": "Система долго не отвечает",
    "robot": "Ваши действия похожи на автоматические",
}


def get_errors(*errors):
    k = []
    for i in errors:
        k.append(all_errors[i])
    return k


print(get_errors("out", "robot"))
