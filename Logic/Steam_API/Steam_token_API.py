
import os

from Utils.Utils import read_json


class Steam_Token_API:

    def __init__(self,my_api):
        self.my_api = my_api
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        self._config = read_json(os.path.join(cur_dir, "API_Configs", "Steam_token_API.json"))
        self.URL = self._config['url']

    def get_token(self):
        url = self.URL
        result = self.my_api.api_get_request(url).json()
        if len(result['data']) == 0:
            raise Exception("Login to steam Website Failed")
        else:
            return result['data']['webapi_token']
