from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/add", methods=["POST"])
def add_page():
    task = request.form["task_name"]
    return f"Вы добавили задачу ***[[{task}]]***"


app.run(debug=True)
