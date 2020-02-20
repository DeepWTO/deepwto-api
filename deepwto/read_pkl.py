# import sys
import pickle

from deepwto.graphql import AppSyncClient
from deepwto.Constants import *


def load_pkl(pickle_path):
    with open(pickle_path, 'rb') as f:
        py_obj = pickle.load(f)
    return py_obj


if __name__ == "__main__":
    path = './data/factual.pkl'

    classes = load_pkl(path)
    keys = list(classes.keys())
    keys.sort()
    print(keys)
    print(len(classes))

    client = AppSyncClient(api_key=api_key, endpoint_url=endpoint_url)

    over_array = []
    for key in keys:
        # Check size over 400 KB : but looks like it's okay to the longest
        # case of 480544. So we comment-out the size checking block
        # byte_size = sys.getsizeof(classes[key])
        # dynamo_limit = 400000
        # limit_over = byte_size > dynamo_limit
        # if limit_over:
        #     over_array.append(key)

        ds = key
        version = "\"{}\"".format("1.0.0")
        factual = "\"\"\"{}\"\"\"".format(classes[key])

        query = """
                mutation CreateFactual {{
                          createFactual(
                            input: {{
                                ds: {0},
                                version: {1},
                                factual: {2}
                            }}
                         )
                          {{
                            ds
                            version
                            factual
                          }}
                        }}
                """.format(ds, version, factual)
        res = client.execute_gql(query).json()
