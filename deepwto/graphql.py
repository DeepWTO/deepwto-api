from typing import Union, List

import requests
import json

from deepwto.constants import available_ds, available_article, cited_by_ds, gov_tks_dict, art_tks_dict


class AppSyncClient:
    latest_version = "1.0.0"
    available_ds_num = len(available_ds)
    available_ds = available_ds

    available_article_num = len(available_article)
    available_article = available_article

    gov_tks_dict = gov_tks_dict
    art_tks_dict = art_tks_dict

    def __init__(self, api_key, endpoint_url):
        self.api_key = api_key
        self.endpoint_url = endpoint_url
        self.headers = {
            "Content-Type": "application/graphql",
            "x-api-key": api_key,
            "cache-control": "no-cache",
        }

    def execute_gql(self, query):
        payload_obj = {"query": query}
        payload = json.dumps(payload_obj)
        response = requests.request(
            "POST", self.endpoint_url, data=payload, headers=self.headers
        )
        return response

    def get_factual(self, ds: int, version: str = "1.0.0"):
        assert ds in self.available_ds, (
            "Make sure choose ds number from " "available_ds"
        )
        ds = "{}".format(str(ds))
        version = '"{}"'.format(version)

        query = """
                query GetFactual{{
                    getFactual(
                        ds: {0}, 
                        version: {1}) {{
                               factual
                            }}
                        }}
                """.format(
            ds, version
        )

        res = self.execute_gql(query).json()
        return res["data"]["getFactual"]["factual"]

    def get_article(self, article: str, version: str = "1.0.0"):
        assert article in self.available_article, (
            "Make sure choose article " "from available_article "
        )

        article = '"{}"'.format(article)
        version = '"{}"'.format(version)
        query = """
                query GetGATT{{
                    getGATT(
                        article: {0}, 
                        version: {1}) {{
                               content
                            }}
                        }}
                """.format(
            article, version
        )

        res = self.execute_gql(query).json()
        return res["data"]["getGATT"]["content"]

    def get_label(self, ds: int, article: str, version: str = "1.0.0"):
        assert ds in self.available_ds, (
            "Make sure choose ds number from " "available_ds"
        )
        assert article in self.available_article, (
            "Make sure choose article " "from available_article "
        )

        ds_art = '"{}"'.format(str(ds) + "_" + article)
        version = '"{}"'.format(version)
        query = """
                query GetLabel{{
                    getLabel(
                        ds_art: {0}, 
                        version: {1}) {{
                               cited
                            }}
                        }}
                """.format(
            ds_art, version
        )

        res = self.execute_gql(query).json()
        return res["data"]["getLabel"]["cited"]

    def get_cited(self, contains: str = None):
        """
        Retrieve all cited: {eq: true} items or,
        Retrieve all cited: {eq: true} that contains certain string (Article)

        Returns:
            cited: List[dict]
                list of dictionaries where each dict has following format:
                     {
                      "ds_art": "67_Article XXIII:1",
                      "version": "1.0.0",
                      "cited": true,
                      "split": "train"
                    }
        """
        nextToken: Union[None, str] = None
        cited: List[dict] = []

        if contains:
            contains = '"{}"'.format(contains)
            if not nextToken:

                query = """
                       query ListLabels {{
                         listLabels(
                           limit: {0}
                           filter: {{
                             ds_art: {{contains: {1}}}
                             cited: {{eq: true}}
                           }}
                         ) {{
                           items {{
                             ds_art
                             version
                             cited
                             split
                           }}
                           nextToken
                         }}
                       }}
                       """.format(
                    11440, contains
                )
                res = self.execute_gql(query).json()
                cited.extend(res["data"]["listLabels"]["items"])
                nextToken = '"{}"'.format(res["data"]["listLabels"]["nextToken"])

            while nextToken:
                query = """
                       query ListLabels {{
                         listLabels(
                           nextToken: {0}
                           limit: {1}
                           filter: {{
                             ds_art: {{contains: {2}}}
                             cited: {{eq: true}}
                           }}
                         ) {{
                           items {{
                             ds_art
                             version
                             cited
                             split
                           }}
                           nextToken
                         }}
                       }}
                       """.format(
                    nextToken, 11440, contains
                )
                res = self.execute_gql(query).json()
                cited.extend(res["data"]["listLabels"]["items"])
                nextToken = '"{}"'.format(res["data"]["listLabels"]["nextToken"])

                if nextToken == '"None"':
                    break
            return cited

        if not contains:
            if not nextToken:
                query = """
                        query ListLabels {{
                          listLabels(
                            limit: {0}
                            filter: {{
                              cited: {{eq: true}}
                            }}
                          ) {{
                            items {{
                              ds_art
                              version
                              cited
                              split
                            }}
                            nextToken
                          }}
                        }}
                        """.format(
                    11440
                )
                res = self.execute_gql(query).json()
                cited.extend(res["data"]["listLabels"]["items"])
                nextToken = '"{}"'.format(res["data"]["listLabels"]["nextToken"])

            while nextToken:
                query = """
                        query ListLabels {{
                          listLabels(
                            nextToken: {0}
                            limit: {1}
                            filter: {{
                              cited: {{eq: true}}
                            }}
                          ) {{
                            items {{
                              ds_art
                              version
                              cited
                              split
                            }}
                            nextToken
                          }}
                        }}
                        """.format(
                    nextToken, 11440
                )
                res = self.execute_gql(query).json()
                cited.extend(res["data"]["listLabels"]["items"])
                nextToken = '"{}"'.format(res["data"]["listLabels"]["nextToken"])

                if nextToken == '"None"':
                    break
            return cited

    @staticmethod
    def get_cited_by_ds(ds: int):
        return cited_by_ds[ds]

    @staticmethod
    def parse_ds(data: List[dict]):
        ds_nums = []
        for item in data:
            ds = int(item['ds_art'].split('_')[0])
            ds_nums.append(ds)
        data = list(set(ds_nums))
        data.sort()
        return data

    def update_tokenized_factual(self, ds: int, version: str = "1.0.0"):
        assert ds in self.available_ds, (
            "Make sure choose ds number from " "available_ds"
        )
        # tokenzied_factual = "{}".format(self.gov_tks_dict[ds])
        raw_factual_tks = self.gov_tks_dict[ds]
        # factualTokenized = ['"test"', '"test2"']
        factualTokenized_whole = ['"{}"'.format(i) for i in raw_factual_tks]

        res_keys = ['data']
        idx = 0
        while 'data' in res_keys:
            factualTokenized = factualTokenized_whole[0:idx]
            ds = "{}".format(str(ds))
            version = '"{}"'.format(version)

            query = """
                    mutation UpdateFactual{{
                      updateFactual(
                        input: {{
                          ds: {0}
                          version: {1}
                          factualTokenized: {2}
                        }}
                      ) 
                      {{
                        ds
                        version
                        factual
                        factualTokenized
                      }}
                    }}
                    """.format(
                ds, version, factualTokenized
            )

            res = self.execute_gql(query).json()
            res_keys = res.keys()
            print(idx, res_keys, res)
            idx += 1

        return idx #res


if __name__ == "__main__":
    endpoint_url = "https://3oedq5prgveqvdax2xtkc2lv34.appsync-api.us-east-1.amazonaws.com/graphql"
    api_key = "da2-npsbpiuolzcq3nfirg63rmnuoe"
    client = AppSyncClient(api_key=api_key, endpoint_url=endpoint_url)
    res = client.update_tokenized_factual(2)
    print(res.keys)
