from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/test", methods=["GET", "POST"])
def test_page():
    name = request.values.get("name")
    return f"Вы ввели имя ***[[{name}]]***"


app.run(debug=True)
