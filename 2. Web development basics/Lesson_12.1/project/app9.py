from flask import Flask, request, render_template


app = Flask(__name__)

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


app.run(debug=True)
