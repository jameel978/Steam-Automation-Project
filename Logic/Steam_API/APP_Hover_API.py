from Utils.utils import *
import os

class APP_Hover_API:

    def __init__(self,my_api):
        self.my_api = my_api
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        self._config = read_json(os.path.join(cur_dir, "API_Configs", "APP_Hover_API.json"))
        self.URL = self._config['url']


    def get_app_hover(self, game_id):
        url = f"{self.URL}{game_id}?json=1"
        result = self.my_api.api_get_request(url)
        return result.json()

    def get_app_categories(self,result):
        cat_list = []
        for cat in result['rgCategories']:
            cat_list.append(cat['strDisplayName'])

    def get_app_genres(self,result):
        return result['strGenres']

    def get_app_review_summary(self,result):
        return result['strReviewSummary']
