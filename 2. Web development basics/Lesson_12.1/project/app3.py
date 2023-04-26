from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/search")
def search_page():
    s = request.args.get("s")
    if s:
        return f"Вы ввели слово ***[{s}]***"
    else:
        return f"Вы не ввели ничего"


app.run(debug=True)
