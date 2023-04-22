from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/search")
def search_page():
    s = request.args["s"]
    return f"Вы ввели слово ***[{s}]***"


app.run()
