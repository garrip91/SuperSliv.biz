from flask import Flask, request, render_template


app = Flask(__name__)

# Ограничиваем размер файла здесь:
app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024

@app.route("/")
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
    """Эта вьюшка обрабатывает форму"""
    # Получаем объект изображения из формы:
    picture = request.files.get("picture")
    # Получаем имя загруженного файла:
    filename = picture.filename
    # Сохраняем изображение с исходным названием в папку uploads:
    picture.save(f"./uploads/{filename}")
    return f"Файл загружен и сохранён"

@app.errorhandler(413)
def page_not_found(e):
    return "<h1>Файл большеват</h1><p>Поищите файл поменьше, пожалуйста!</p>", 413


app.run(debug=True)
