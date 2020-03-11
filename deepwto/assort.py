import json

import deepwto.constants
import deepwto.utils

f_path = "/Users/zachary/deepwto/deepwto-draft/models/cite_wa/OneLabelTextCNN/data/test_data.json"
avails = deepwto.constants.available_ds
avail_arts_num = len(deepwto.constants.available_article)


def collect_unique_gov_art_tks():
    with open(f_path) as fin:
        dss = []
        arts = []
        gov_tks_dict = dict()
        art_tks_dict = dict()

        for each_line in fin:
            data = json.loads(each_line)
            test_id = data['testid']
            ds = int(test_id.split('_')[0])
            art = test_id.split('_')[1][1:-1]

            arts.append(art)
            dss.append(ds)

            gov_tk = data['gov']
            art_tk = data['art']

            if ds not in gov_tks_dict.keys():
                gov_tks_dict[ds] = gov_tk

            if art not in art_tks_dict.keys():
                art_tks_dict[art] = art_tk

        set_dss = set(dss)
        set_avails = set(avails)
        set_arts = set(arts)

        print("len", len(set_dss))
        print("len", len(set_avails))
        print("len", len(set_arts))
        assert set_dss == set_avails, "not equal"
        assert len(set_arts) == avail_arts_num, "not all"

        print("len", len(gov_tks_dict.keys()))
        print("len", len(art_tks_dict.keys()))

        deepwto.utils.dump_pkl(gov_tks_dict, "gov_tks.pkl")
        deepwto.utils.dump_pkl(art_tks_dict, "art_tks.pkl")


if __name__ == "__main__":
    # collect_unique_gov_art_tks()
    art_tks_dict = deepwto.utils.load_pkl("./art_tks.pkl")
    gov_tks_dict = deepwto.utils.load_pkl("./gov_tks.pkl")

    pass
