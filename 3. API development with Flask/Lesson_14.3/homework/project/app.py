from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/movie/title/")
def main_page():
    return render_template("movie.html")


app.run(debug=True)
