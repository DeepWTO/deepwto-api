import requests
import json

from deepwto.constants import available_ds, available_article


class AppSyncClient:
    latest_version = '1.0.0'
    available_ds_num = len(available_ds)
    available_ds = available_ds

    available_article_num = len(available_article)
    available_article = available_article

    def __init__(self, api_key, endpoint_url):
        self.api_key = api_key
        self.endpoint_url = endpoint_url
        self.headers = {
                'Content-Type': "application/graphql",
                'x-api-key': api_key,
                'cache-control': "no-cache"
        }

    def execute_gql(self, query):
        payload_obj = {"query": query}
        payload = json.dumps(payload_obj)
        response = requests.request("POST",
                                    self.endpoint_url,
                                    data=payload,
                                    headers=self.headers)
        return response

    def get_factual(self, ds: int, version: str = "1.0.0"):
        assert ds in self.available_ds, "Make sure choose ds number from " \
                                        "available_ds"
        ds = "{}".format(str(ds))
        version = "\"{}\"".format(version)

        query = """
                query GetFactual{{
                    getFactual(
                        ds: {0}, 
                        version: {1}) {{
                               factual
                            }}
                        }}
                """.format(ds, version)

        res = self.execute_gql(query).json()
        return res['data']['getFactual']['factual']

    def get_article(self, article: str, version: str = "1.0.0"):
        assert article in self.available_article, "Make sure choose article " \
                                                  "from available_article "

        article = "\"{}\"".format(article)
        version = "\"{}\"".format(version)
        query = """
                query GetGATT{{
                    getGATT(
                        article: {0}, 
                        version: {1}) {{
                               content
                            }}
                        }}
                """.format(article, version)

        res = self.execute_gql(query).json()
        return res['data']['getGATT']['content']

    def get_label(self, ds:int, article: str, version: str = "1.0.0"):
        assert ds in self.available_ds, "Make sure choose ds number from " \
                                        "available_ds"
        assert article in self.available_article, "Make sure choose article " \
                                                  "from available_article "

        ds_art = "\"{}\"".format(str(ds)+"_"+article)
        version = "\"{}\"".format(version)
        query = """
                query GetLabel{{
                    getLabel(
                        ds_art: {0}, 
                        version: {1}) {{
                               cited
                            }}
                        }}
                """.format(ds_art, version)

        res = self.execute_gql(query).json()
        return res['data']['getLabel']['cited']


if __name__ == "__main__":

    api_key = ""
    endpoint_url = "https://3oedq5prgveqvdax2xtkc2lv34.appsync-api.us-east-1.amazonaws.com/graphql"

    client = AppSyncClient(api_key=api_key, endpoint_url=endpoint_url)
    print(client.available_ds)
    print(client.latest_version)
    print(client.available_ds_num)

    factual = client.get_factual(ds=2)
    print(factual)
    #
    print(client.available_article)
    print(client.available_article_num)

    content = client.get_article(article='Article I')
    print(content)

    cited = client.get_label(article='Article I', ds=2)
    print(cited)

    # ds = 1
    #
    # query = """
    #         query ListFactual {{
    #                   listFactual(
    #                     input: {{
    #                         ds: {0},
    #                         version: {1},
    #                         factual: {2}
    #                     }}
    #                  )
    #                   {{
    #                     ds
    #                     version
    #                     factual
    #                   }}
    #                 }}
    #         """.format(1, "\"1.0.4\"", "\"this-is-version4\"")
    # print(type(query))
    # print(query)
    # res = client.execute_gql(query).json()
    # print(res)
