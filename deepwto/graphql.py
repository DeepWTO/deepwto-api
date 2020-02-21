import requests
import json

import yaml

with open("./v.1.0.0.yaml", 'r') as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)


class AppSyncClient:
    latest_version = '1.0.0'
    available_ds = [int(e) for e in data['available_ds'].split(", ")]
    available_ds_num = len(available_ds)

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
        assert ds in self.available_ds, "Make sure choose one of ds_num"
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


if __name__ == "__main__":

    api_key = "da2-hgitmt7z45he3mlvrltgmwqlhm"
    endpoint_url = "https://3oedq5prgveqvdax2xtkc2lv34.appsync-api.us-east-1.amazonaws.com/graphql"

    client = AppSyncClient(api_key=api_key, endpoint_url=endpoint_url)
    print(client.available_ds)
    print(client.latest_version)
    print(client.available_ds_num)

    client.get_factual(ds=2)
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
