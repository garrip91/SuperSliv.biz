def get_rating(stars):
    
    if stars == "*":
        return "Ужасно"
    elif stars == "**":
        return "Очень плохо"
    elif stars == "***":
        return "Средненько"
    elif stars == "****":
        return "Всё в порядке"
    elif stars == "*****":
        return "Прекрасная поездка!"
    else:
        return "Ошибка"
