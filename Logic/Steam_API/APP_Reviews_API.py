from Infra.Api_wrapper import APIWrapper
from Logic.Utils import *
import os

class App_Reviews_Api:

    def __init__(self,my_api):
        self.my_api = my_api
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        self._config = read_json(os.path.join(cur_dir, "API_Configs", "APP_Reviews_API.json"))
        self.URL = self._config['url']

    def prepair_api_url(self,game_id):
        return f'{self.URL}{game_id}?json=1'

    def get_app_review(self,game_id,**extra):
        url = self.prepair_api_url(game_id)
        if extra:
            result = self.my_api.api_get_request_with_param(url, extra,self._config)
            return result.json()
        else:
            result = self.my_api.api_get_request(url)
            return result.json()

    def check_review_languages(self,app_review,lang):
        result = app_review['reviews']
        for review in result:
            if review['language'] != lang:
                return False
        return True


    def get_review_numbers(self,result):
        return result["query_summary"]['num_reviews']

    def get_play_time_of_reviews(self,app_review):
        result = app_review['reviews']
        review_play_time = []
        for review in result:
            play_time = review['author']['playtime_at_review']/60 #its in minues
            review_play_time.append(play_time)
        return review_play_time

