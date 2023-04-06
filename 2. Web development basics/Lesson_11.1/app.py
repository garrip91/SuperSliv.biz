from flask import Flask, request, render_template


app = Flask(__name__)

#@app.route("/")
#def page_index():
#    page_content = """
#        <h1>Смотри, это - моя страничка</h1>
#        <p>Страничек много, но это - моя!</p>
#        <p>Фронтенд - мой лучший друг!</p>
#    """
#    return page_content


@app.route("/")
def hello():
    user_data = {
        "name": "Ivan",
        "phone": "+7 (123) 456-78-90",
        "email": "ivan_dev@gmail.com",
        "telegram": "ivan_dev"
    }
    items = ["Python", "Java", "Kotlin", "Go"]
    is_blocked = True # или is_blocked = False
    return render_template("hello.html", user=user_data, items=items, is_blocked=is_blocked)


app.run()
