from flask import Blueprint, render_template
from .dao.candidates_dao import CandidateDAO


# Создаём блюпринт:
candidates_blueprint = Blueprint("candidates_blueprint", __name__, template_folder="templates")

# Создаём DAO:
candidates_dao = CandidateDAO("./data/candidates.json")

# Создаём вьюшку для кандидатов:
@candidates_blueprint.route("/candidates/")
def page_candidates_all():
    candidates = candidates_dao.get_all()
    return render_template("candidates_index.html", candidates=candidates)

# Создаём вьюшку для одного кандидата:
@candidates_blueprint.route("/candidates/<int:pk>/")
def page_candidate_one(pk):
    candidate = candidates_dao.get_by_pk(pk)
    return render_template("candidate_single.html", candidate=candidate)
