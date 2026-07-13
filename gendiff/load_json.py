import json


def load_json(file_path):
    with open(file_path) as f1:
        result = json.load(f1)

    return result