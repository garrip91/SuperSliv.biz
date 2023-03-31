# Сперва импортируем Flask

from flask import Flask

# Затем создадим экземпляр этого Flask, назовём его app -
# это будет наше приложение

app = Flask(__name__)

# Что такое __name__ ?
# При запуске сценария значение переменной __name__ равно __main__
# Эта переменная помогает Flask разобраться, где он находится
# и без неё он просто не заработает

# Теперь создадим функцию, которая будет что-то делать
# Например, page_index - это функция, которая будет возвращать страницу 'Я страничка'

@app.route("/test/")
def page_test():
    return "Тестовая страница"

@app.route("/")
def page_index():
    return "Главная страница"

@app.route("/profile/")
def page_profile():
    return "Страница профиля пользователя"

@app.route("/feed/")
def page_feed():
    return "Страница ленты пользователя"

@app.route("/messages/")
def page_messages():
    return "Страница сообщений пользователя"


@app.route("/users/<uid>")
def profile1(uid):
    return f"<h1>Профиль {uid}</h1>"

@app.route("/catalog/items/<itemid>")
def profile2(itemid):
    return f"<h1>Страница товара {itemid}</h1>"

# Теперь используем метод у приложения, который зарегистрирует маршрут
# Например, для главной страницы будет вызвана функция page_index

app.run()
