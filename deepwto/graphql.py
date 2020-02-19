import requests
import json

from deepwto.Constants import *


class AppSyncClient:
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


if __name__ == "__main__":
    client = AppSyncClient(api_key=api_key, endpoint_url=endpoint_url)
    ds = 1

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
            """.format(1, "\"1.0.4\"", "\"this-is-version4\"")
    print(type(query))
    print(query)
    res = client.execute_gql(query).json()
    print(res)
