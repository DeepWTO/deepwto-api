import yaml

from deepwto.graphql import AppSyncClient
from deepwto.Constants import *

if __name__ == "__main__":

    with open("./data/gatt.yaml", 'r') as stream:
        try:
            data = yaml.safe_load(stream)
            keys = list(data.keys())
            keys.sort()

        except yaml.YAMLError as exc:
            print(exc)

    client = AppSyncClient(api_key=api_key, endpoint_url=endpoint_url)

    for key in keys:
        article = key
        version = "\"{}\"".format("1.0.0")
        content = "\"\"\"{}\"\"\"".format(data[key])

        query = """
                mutation CreateGATT {{
                          createGATT(
                            input: {{
                                article: {0},
                                version: {1},
                                content: {2}
                            }}
                         )
                          {{
                            article
                            version
                            content
                          }}
                        }}
                """.format(article, version, content)
        res = client.execute_gql(query).json()
        break
