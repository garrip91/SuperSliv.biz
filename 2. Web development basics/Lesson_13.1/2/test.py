from main import get_rating


assert get_rating("*") == "Ужасно", "Ошибка для 1 звезды"
assert get_rating("*"*2) == "Очень плохо", "Ошибка для 2 звёзд"
assert get_rating("*"*3) == "Средненько", "Ошибка для 3 звёзд"
assert get_rating("*"*4) == "Всё в порядке", "Ошибка для 4 звёзд"
assert get_rating("*"*5) == "Прекрасная поездка!", "Ошибка для 5 звёзд"

assert get_rating("") == "Ошибка", "Пустая строка должна вернуть ошибку"
assert get_rating("*"*6) == "Ошибка", "6 звёзд должны вернуть ошибку"
assert get_rating(27) == "Ошибка", "Число должно вернуть ошибку"