from flask import Flask

# Импортируем блюпринт:
from app.main.views import main_blueprint

# Создаём экземпляр Flask:
app = Flask(__name__)

# Регистрируем первый блюпринт:
app.register_blueprint(main_blueprint)

# Запускаем сервер только в случае, если файл сам запущен, а не импортирован:
if __name__ == "__main__":
    app.run(debug=True)
