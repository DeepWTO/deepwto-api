import json
import yaml

from deepwto.graphql import AppSyncClient
from deepwto.constants import *


def read_data(json_path, stop_idx, split):
    read_idx = 0
    split = "\"{}\"".format(split)

    with open(json_path) as fin:
        for each_line in fin:
            data = json.loads(each_line)
            test_id = data['testid']
            features_content_gov = data['gov']
            features_content_art = data['art']
            label = int(data['label'][0])
            # print(test_id, label)

            ds_numb = test_id.split('_')[0]
            art_numb = test_id.split('_')[1][1:-1]
            ds_art = ds_numb + '_' + art_numb
            print(ds_art, label)

            if label == 0:
                cited = 'false'
            elif label == 1:
                cited = 'true'

            client = AppSyncClient(api_key=api_key, endpoint_url=endpoint_url)

            ds_art = "\"{}\"".format(ds_art)
            version = "\"{}\"".format("1.0.0")

            query = """
                    mutation CreateLabel {{
                              createLabel(
                                input: {{
                                    ds_art: {0},
                                    version: {1},
                                    cited: {2},
                                    split: {3}
                                }}
                             )
                              {{
                                ds_art
                                version
                                cited
                                split
                              }}
                            }}
                    """.format(ds_art, version, cited, split)
            res = client.execute_gql(query).json()
            print(res)
            assert 'errors' not in res.keys()

            if read_idx == stop_idx:
                break
            else:
                read_idx += 1


if __name__ == "__main__":
    test_inst_num = 2287
    train_inst_num = 9153
    # read_data("./data/test_data.json", 0)

    # read_data("./data/test_data.json", test_inst_num-1, 'test')
    read_data("./data/train_data.json", train_inst_num-1, 'train')

    pass

