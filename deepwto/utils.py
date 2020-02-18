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

            # Recommend to use debugger to peek into the dataset rather than
            # using print()
            # print(test_id)
            ds_numb = test_id.split('_')[0]
            art_numb = test_id.split('_')[1]
            ds_numbs.append(ds_numb)
            art_numbs.append(art_numb)
            # print(ds_numb)
            # print(features_content_gov)
            # print(features_content_art)
            # print(label)
            if read_idx == stop_idx:
                break
            else:
                read_idx += 1
    print(ds_numbs)
    print(art_numbs)
    ds_numbs_set = set(ds_numbs)
    art_numbs_set = set(art_numbs)
    print(ds_numbs_set)
    print(art_numbs_set)
    print(len(ds_numbs_set))
    print(len(ds_numbs))
    print(len(art_numbs_set))


    ds_numbs_set_list = []
    for e in ds_numbs_set:
        ds_numbs_set_list.append(int(e))
    ds_numbs_set_list.sort()
    print(ds_numbs_set_list)

    art_numbs_set_list = []
    for e in art_numbs_set:
        art_numbs_set_list.append(e)
    art_numbs_set_list.sort()
    print(art_numbs_set_list)


if __name__ == "__main__":
    test_inst_num = 2287
    train_inst_num = 9153
    # read_data("./data/test_data.json", test_inst_num-1)
    read_data("./data/train_data.json", train_inst_num-1)

    pass
