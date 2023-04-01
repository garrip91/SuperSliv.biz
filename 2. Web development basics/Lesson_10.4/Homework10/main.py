from flask import Flask
from utils import load_candidates


app = Flask(__name__)

candidates = load_candidates()
#print(candidates)


@app.route("/")
def page_index():
    str_candidates = "<pre>"
    for candidate in candidates.values():
        str_candidates += f"{candidate['name']} \n{candidate['position']} \n{candidate['skills']} \n\n"
    str_candidates += "</pre>"
    return str_candidates


@app.route("/candidates/<int:id>/")
def page_profile(id):
    candidate = candidates[id]
    str_candidates = f"<img src={candidate['picture']} /> <br /><br />{candidate['name']} <br />{candidate['position']} <br />{candidate['skills']} <br /><br />"
    return str_candidates


@app.route("/skills/<skill>/")
def page_skill(skill):
    str_candidates = "<pre>"
    for candidate in candidates.values():
        candidate_skills = candidate["skills"].split(", ")
        candidate_skills = [x.lower() for x in candidate_skills]
        if skill.lower() in candidate_skills:
            str_candidates += f"{candidate['name']} \n{candidate['position']} \n{candidate['skills']} \n\n"
    str_candidates += "</pre>"
    return str_candidates


app.run(debug=True)
