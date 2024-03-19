from Utils.Utils import *
import os

class APP_Details_API:

    def __init__(self,my_api):
        self.my_api = my_api
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        self._config = read_json(os.path.join(cur_dir, "API_Configs", "APP_Details_API.json"))
        self.URL = self._config['url']


    def get_app_details(self, game_id, **extra):
        url = f"{self.URL}?appids={game_id}"
        if extra:
            result = self.my_api.api_get_request_with_param(url, extra,self._config)
            return result.json()[game_id]
        else:
            result = self.my_api.api_get_request(url)
            return result.json()[game_id]

    def get_app_price_currency(self, result):
        return result["data"]["price_overview"]["currency"]

    def get_app_name_from_app_details(self,result):
        return result["data"]["name"]

    def get_app_price_using_id_from_app_details(self,id):
        result = self.get_app_details(id)
        if result["data"]["is_free"]:
            # game is free
            return 0
        else:
            return result["data"]["price_overview"]["final"]


    def get_app_prices_using_ids_from_app_details(self,id_list_of_search):
        price_list = []
        for id in id_list_of_search:
            price = self.get_app_price_using_id_from_app_details(id)
            price_list.append(price)
        return price_list


