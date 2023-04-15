import json
from pprint import pprint


def load_candidates_from_json():
    with open(file="candidates.json", mode="r", encoding="utf-8") as file:
        data = json.load(file)
        candidates = {}
        for i in data:
            candidates[i["id"]] = i
    return candidates


def get_candidate(candidate_id):
    result = [candidate for candidate in load_candidates_from_json().values() if candidate["id"]==candidate_id][0]
    return result


def get_candidates_by_name(candidate_name):
    result = [candidate for candidate in load_candidates_from_json().values() if candidate_name.title() in candidate["name"].split(" ")]
    return result


def get_candidates_by_skill(skill_name):
    result = [candidate for candidate in load_candidates_from_json().values() if skill_name in candidate["skills"].split(", ")]
    return result


#print(type(load_candidates_from_json()))
#pprint(load_candidates_from_json())
#pprint(get_candidate(5))
#pprint(get_candidates_by_name("love"))
#pprint(get_candidates_by_skill("python"))
