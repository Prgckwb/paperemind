import requests

from paperemind.output import SearchOutput


class SemanticScholar():
    def __init__(self):
        self.endpoint = 'http://api.semanticscholar.org/graph/v1/paper'

    def search(self, query: str, get_title=True, get_abstract=True) -> SearchOutput:
        fields = ''

        if get_title:
            fields += 'title'
        if get_abstract:
            fields += ',abstract'

        params = {
            'query': query,
            'fields': fields
        }
        url = f'{self.endpoint}/search'
        print(url)
        response = requests.get(url, params=params, timeout=3)
        output = SearchOutput.from_json(response.json())
        return output

    # IDを指定して論文を取得する
    def get_paper(self, arxiv_id: str):
        url = f'{self.endpoint}/ARXIV:{arxiv_id}'
        params = {
            'fields': 'title,abstract,citationCount,tldr,url'
        }
        response = requests.get(url, params=params, timeout=3)
        return response.json()
