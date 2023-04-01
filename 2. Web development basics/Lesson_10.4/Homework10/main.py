from flask import Flask
from utils import load_candidates


app = Flask(__name__)

candidates = load_candidates()
print("================================================================")
print(candidates)
print("----------------------------------------------------------------")
print(candidates.values())
print("================================================================")


@app.route("/")
def page_index():
    str_candidates = "<pre>"
    for candidate in candidates.values():
        str_candidates += f"Имя кандидата - {candidate['name']} \nПозизия кандидата - {candidate['position']} \nНавыки через запятую - {candidate['skills']} \n\n"
    str_candidates += "</pre>"
    return str_candidates


@app.route("/candidates/<int:id>/")
def page_profile(id):
    candidate = candidates[id]
    str_candidates = f"<img src={candidate['picture']} /> <br /><br />Имя кандидата - {candidate['name']} <br />Позизия кандидата - {candidate['position']} <br />Навыки через запятую - {candidate['skills']} <br /><br />"
    return str_candidates


@app.route("/skills/<skill>/")
def page_skill(skill):
    str_candidates = "<pre>"
    for candidate in candidates.values():
        candidate_skills = candidate["skills"].split(", ")
        candidate_skills = [x.lower() for x in candidate_skills]
        if skill.lower() in candidate_skills:
            str_candidates += f"Имя кандидата - {candidate['name']} \nПозизия кандидата - {candidate['position']} \nНавыки через запятую - {candidate['skills']} \n\n"
    str_candidates += "</pre>"
    return str_candidates


app.run(debug=True)
