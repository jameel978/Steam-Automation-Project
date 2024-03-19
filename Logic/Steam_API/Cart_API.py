from Utils.Utils import *
import os

class Cart_API:

    def __init__(self,my_api):
        self.my_api = my_api
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        self._config = read_json(os.path.join(cur_dir, "API_Configs", "Cart_API.json"))
        self.URL = self._config['url']

    def prepair_api_url(self,game_id):
        return f'{self.URL}{game_id}?json=1'

    def add_to_cart(self,key,packageid, bundleid):
        url = f'{self.URL}access_token={key}&packageid={packageid}&bundleid={bundleid}&user_country=il'
        result = self.my_api.api_post_request(url)
        return result