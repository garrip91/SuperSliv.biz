# import posts


# /

# /posts
# /posts/1
# /posts/create
# /posts/1/edit
# /posts/1/delete

# /form/show
# /form/send


from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/form", methods=["GET", "POST"])
def page_form_show():
    if request.method == "POST":
        name = request.values.get("name")
        return f"Я тебя услышал {name}"
    else:
        return "<form action='/form', method='POST'><input type='text' name='name' /><input type='submit' /></form>"

# @app.route("/posts")
# def page_posts_show():
#     return "Я показываю все посты"
#
# @app.route("/posts", methods=["POST"])
# def page_post_create():
#     return "Я создаю пост"
#
# @app.route("/posts/1", methods=["GET"])
# def page_post_get():
#     return "Я показываю пост - красивое|"
#
# @app.route("/posts/1", methods=["PATCH"])
# def page_post_patch():
#     return "Я обновляю пост - красивое|", 200
#
# @app.route("/posts/1", methods=["DELETE"])
# def page_post_delete():
#     return "Я удаляю пост"


app.run(debug=True)
