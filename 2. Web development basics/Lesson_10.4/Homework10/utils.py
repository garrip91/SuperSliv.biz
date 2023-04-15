import json
from pprint import pprint


def load_candidates():
    with open(file="candidates.json", mode="r", encoding="utf-8") as file:
        data = json.load(file)
        candidates = {}
        for i in data:
            candidates[i["id"]] = i
    return candidates


#pprint(load_candidates())
