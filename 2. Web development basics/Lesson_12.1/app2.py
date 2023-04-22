from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/filter")
def filter_page():
    from_value = request.args["from"]
    to_value = request.args["to"]
    return f"Ищем в диапазоне от ***[{from_value}]*** до ***[{to_value}]***"


app.run(debug=True)
