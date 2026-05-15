import json


def export_json(programs, filename="results.json"):

    with open(filename, "w", encoding="utf-8") as file:

        json.dump(
            programs,
            file,
            indent=4,
            ensure_ascii=False
        )
