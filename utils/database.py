import json
from datetime import datetime

with open("database.json", "r", encoding="utf-8") as db:
    data = json.load(db)


def save():
    with open("database.json", "w", encoding="utf-8") as db:
        json.dump(data, db, indent=4, ensure_ascii=False)


def timestamp():
    return datetime.now().isoformat()
