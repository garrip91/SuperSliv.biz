from flask import Flask, request, render_template
from utils import load_needed_movie, load_children_movies_list


app = Flask(__name__)

@app.route("/movie/<title>/")
def movie_page(title):
    context = load_needed_movie(title)
    print(context)
    return render_template("movie.html", context=context)

@app.route("/rating/children/")
def children_rating_page():
    context = load_children_movies_list()
    print(context)
    return render_template("children.html", context=context)


app.run(debug=True)
