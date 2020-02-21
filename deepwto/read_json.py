import json
import yaml


def read_data(json_path, stop_idx, cited):
    read_idx = 0
    ds_numbs = []
    art_numbs = []

    with open(json_path) as fin:
        for each_line in fin:
            data = json.loads(each_line)
            test_id = data['testid']
            features_content_gov = data['gov']
            features_content_art = data['art']
            label = int(data['label'][0])
            print(test_id, label)

            ds_numb = test_id.split('_')[0]
            art_numb = test_id.split('_')[1][1:-1]
            cited_art_numb = cited[art_numb].split(', ')

            # print(ds_numb, art_numb, label)
            # print(cited_art_numb)

            if label == 0:
                # print('DS{}'.format(ds_numb))
                assert 'DS{}'.format(ds_numb) not in cited_art_numb
            elif label == 1:
                print(ds_numb, art_numb, label)
                print(cited_art_numb)
                print('DS{}'.format(ds_numb))
                assert 'DS{}'.format(ds_numb) in cited_art_numb

            ds_numbs.append(ds_numb)
            art_numbs.append(art_numb)

            if read_idx == stop_idx:
                break
            else:
                read_idx += 1
    ds_numbs_set = set(ds_numbs)
    art_numbs_set = set(art_numbs)

    ds_numbs_set_list = []
    for e in ds_numbs_set:
        ds_numbs_set_list.append(int(e))
    ds_numbs_set_list.sort()

    art_numbs_set_list = []
    for e in art_numbs_set:
        art_numbs_set_list.append(e)
    art_numbs_set_list.sort()


if __name__ == "__main__":
    with open("./data/cited.yaml", 'r') as stream:
        try:
            cited = yaml.safe_load(stream)
            keys = list(cited.keys())
            keys.sort()

        except yaml.YAMLError as exc:
            print(exc)

    test_inst_num = 2287
    train_inst_num = 9153
    read_data("./data/test_data.json", 0, cited)

    # read_data("./data/test_data.json", test_inst_num-1, cited)
    # read_data("./data/train_data.json", train_inst_num-1, cited)

    pass
