
import os

from Utils.Utils import read_json


class Store_Search_API:

    def __init__(self,my_api):
        self.my_api = my_api
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        self._config = read_json(os.path.join(cur_dir, "API_Configs", "Store_Search_API.json"))
        self.URL = self._config['url']

    def get_search_result(self, search_term, **extra):
        url = f"{self.URL}?term={search_term}"
        if extra:
            result = self.my_api.api_get_request_with_param(url, extra,self._config)
            return result.json()
        else:
            result = self.my_api.api_get_request(url)
            return result.json()

    def get_names_of_found_serach_apps(self,search_result):
        result = search_result['items']
        ans_ = []
        for app in result:
            ans_.append(app['name'])
        return ans_

    def get_app_id_from_app_details(self,search_result):
        result = search_result['items']
        ans_ = []
        for app in result:
            ans_.append(str(app['id']))
        return ans_



