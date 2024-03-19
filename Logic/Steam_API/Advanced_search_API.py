from Utils.Utils import *
import os


class Advanced_search_API:

    def __init__(self,my_api):
        self.my_api = my_api
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        self._config = read_json(os.path.join(cur_dir, "API_Configs", "Advanced_search_API.json"))
        self.URL = self._config['url']

    def prepair_api_url(self, search_term):
        search_term = search_term.replace(" ","+")
        return f'{self.URL}?term={search_term}&json=1'

    def get_search_results(self, term, **extra):
        url = self.prepair_api_url(term)
        if extra:
            result = self.my_api.api_get_request_with_param(url, extra,self._config)
            return result.json()
        else:
            result = self.my_api.api_get_request(url)
            return result.json()


    def get_app_ids_from_search_results(self,result):
        items = result["items"]
        id_list = []
        for app in items:
            id_list.append(extract_idf_from_link(app['logo']))
        return id_list
