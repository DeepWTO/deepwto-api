import json


def read_data(json_path, stop_idx):
    read_idx = 0
    ds_numbs = []
    art_numbs = []
    with open(json_path) as fin:
        for each_line in fin:
            data = json.loads(each_line)
            test_id = data['testid']
            features_content_gov = data['gov']
            features_content_art = data['art']
            label = data['label']
            print(test_id, label)

            ds_numb = test_id.split('_')[0]
            art_numb = test_id.split('_')[1]
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
    test_inst_num = 2287
    train_inst_num = 9153
    read_data("./data/test_data.json", 0)

    # read_data("./data/test_data.json", test_inst_num-1)
    # read_data("./data/train_data.json", train_inst_num-1)

    pass
