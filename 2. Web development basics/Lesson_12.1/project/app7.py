from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def page_form():
    """Эта вьюшка показывает форму, которая отправляет файлы"""
    form_content = """
        <form action="/upload" method="POST" enctype="multipart/form-data">
          <input type="file" name="picture" />
          <input type="submit" value="Отправить" />
        </form>
    """
    return form_content

@app.route("/upload", methods=["POST"])
def page_upload():
    """Эта вьюшка обрабатывает форму, вытаскивает из запроса файл и показывает ..."""
    # Получаем объект изображения из формы:
    picture = request.files.get("picture")
    return f"Загружен файл ***[[{picture.filename}]]***"


app.run(debug=True)
