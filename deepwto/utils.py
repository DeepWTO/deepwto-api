import json


def read_data(json_path):
    with open(json_path) as fin:

        for each_line in fin:
            data = json.loads(each_line)
            test_id = data['testid']
            features_content_gov = data['gov']
            features_content_art = data['art']
            label = data['label']
