from flask import Blueprint, request, render_template
from functions import load_posts, uploads_posts


loader_blueprint = Blueprint("loader", __name__, url_prefix="/post", static_folder="static", template_folder="templates")


@loader_blueprint.route("/form/")
def form():
    return render_template("post_form.html")

@loader_blueprint.route("/upload/", methods=["POST"])
def upload():
    file = request.files["picture"]
    filename = file.filename
    content = request.values["content"]
    posts = load_posts()
    posts.append({
        "pic": f"uploads/images/{filename}",
        "content": content
    })
    uploads_posts(posts)
