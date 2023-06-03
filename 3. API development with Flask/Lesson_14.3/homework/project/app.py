from flask import Flask, request, render_template
from utils import load_needed_movie, load_children_movies_list
from flask_paginate import Pagination, get_page_args


app = Flask(__name__)


# generating data for pagination
users = list(range(100))

def get_users(offset=0, per_page=10):
    return users[offset: offset+per_page]


@app.route("/movie/<title>/")
def movie_page(title):
    context = load_needed_movie(title)
    return render_template("movie.html", context=context)

@app.route("/rating/children/")
def children_rating_page():
    context = load_children_movies_list()
    page, per_page, offset = get_page_args(page_parameter="page", per_page_parameter="per_page")
    total = len(users)
    pagination_users = get_users(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework="bootstrap4")
    return render_template("children.html", context=context, users=pagination_users, page=page, per_page=per_page, pagination=pagination)


app.run(debug=True)
