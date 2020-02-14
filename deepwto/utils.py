import json


def read_json(json_path):
    with open(json_path) as f:
        data = json.load(f)
    return data
