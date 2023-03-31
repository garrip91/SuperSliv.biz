from flask import Flask
from utils import load_candidates


app = Flask(__name__)

candidates = load_candidates()
print(candidates)


@app.route("/")
def page_index():
    str_candidates = "<pre>"
    for candidate in candidates.values():
        str_candidates += f"{candidate['name']} \n{candidate['position']} \n{candidate['skills']} \n\n"
    str_candidates += "</pre>"
    return str_candidates


@app.route("/candidates/<int:id>/")
def profile(id):
    candidate = candidates[id]
    str_candidates = f"<img src={candidate['picture']} /> <br /><br />{candidate['name']} <br />{candidate['position']} <br />{candidate['skills']} <br /><br />"
    return str_candidates


app.run(debug=True)
