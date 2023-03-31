from flask import Flask


app = Flask(__name__)

# @app.route("/")
def page_index():
    return "Hello, World!"


app.add_url_rule("/", view_func=page_index)


app.run()
