import json


POST_PATH = "posts_.json"


def load_posts():
    with open(file=POST_PATH, mode="r", encoding="utf-8") as file:
        posts = json.load(file)
    return posts


def uploads_posts(posts):
    with open(file=POST_PATH, mode="w", encoding="utf-8") as file:
        # json.dump(file, ensure_ascii=False)
        json.dump(posts, file, indent=4)