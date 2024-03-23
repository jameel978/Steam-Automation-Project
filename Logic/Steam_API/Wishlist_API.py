
import os

from Utils.Utils import read_json


class Wishlist_API:
    def __init__(self,my_api):
        self.my_api = my_api
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        self._config = read_json(os.path.join(cur_dir, "API_Configs", "Wishlist_API.json"))
        self.URL_Add = self._config['url_add']
        self.URL_Remove = self._config['url_remove']

    def add_to_wishlist(self,appid):
        form_data = {
            "appid": appid,
            "sessionid": self.my_api.get_sessionid()
        }
        result = self.my_api.api_post_request(self.URL_Add, form_data=form_data)
        return result.json()

    def remove_from_wishlist(self,appid):
        form_data = {
            "appid": appid,
            "sessionid": self.my_api.get_sessionid()
        }
        result = self.my_api.api_post_request(self.URL_Remove, form_data=form_data)
        return result.json()