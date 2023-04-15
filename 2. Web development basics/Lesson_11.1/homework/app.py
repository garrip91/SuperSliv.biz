from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill
from pprint import pprint


app = Flask(__name__)

candidates = load_candidates_from_json()


@app.route("/")
def page_list():
    return render_template("list.html", candidates=candidates.values())


@app.route("/candidate/<int:id>/")
def page_card(id):
    candidate = get_candidate(candidate_id=id)
    return render_template("card.html", candidate=candidate)


@app.route("/search/<candidate_name>/")
def page_search(candidate_name):
    found_candidates = get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=found_candidates)


@app.route("/skill/<skill_name>/")
def page_skill(skill_name):
    found_candidates = get_candidates_by_skill(skill_name)
    return render_template("skill.html", skill_name=skill_name, candidates=found_candidates)


app.run(debug=True)

# pprint(candidates)
# {
#     1: {
#         "id": 1,
#         "name": "Adela Hendricks",
#         "picture": "https://picsum.photos/200",
#         "position": "Go разработчик",
#         "gender": "female",
#         "age": 40,
#         "skills": "go, python"
#     },
#     2: {
#         "id": 2,
#         "name": "Sheri Torres",
#         "picture": "https://picsum.photos/200",
#         "position": "Delphi developer",
#         "gender": "female",
#         "age": 26,
#         "skills": "Delphi, pascal, fortran, basic"
#     },
#     3: {
#         "id": 3,
#         "name": "Burt Stein",
#         "picture": "https://picsum.photos/200",
#         "position": "Team lead",
#         "gender": "male",
#         "age": 33,
#         "skills": "делегирование, пользоваться календарем, обсуждать важные вопросы"
#     },
#     4: {
#         "id": 4,
#         "name": "Bauer Adkins",
#         "picture": "https://picsum.photos/200",
#         "position": "CTO",
#         "gender": "male",
#         "age": 37,
#         "skills": "very important face"
#     },
#     5: {
#         "id": 5,
#         "name": "Day Holloway",
#         "picture": "https://picsum.photos/200",
#         "position": "HR manager",
#         "gender": "male",
#         "age": 35,
#         "skills": "LinkedIn, telegram, spam, spam, spam"
#     },
#     6: {
#         "id": 6,
#         "name": "Austin Cochran",
#         "picture": "https://picsum.photos/200",
#         "position": "python-develop",
#         "gender": "male",
#         "age": 26,
#         "skills": "python, html"
#     },
#     7: {
#         "id": 7,
#         "name": "Sheree Love",
#         "picture": "https://picsum.photos/200",
#         "position": "Django developer",
#         "gender": "female",
#         "age": 33,
#         "skills": "Python, Django, flask"
#     }
# }
