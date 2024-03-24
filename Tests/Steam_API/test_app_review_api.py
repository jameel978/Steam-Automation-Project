import unittest
from Logic.Steam_API.APP_Reviews_API import *
from Infra.Api_wrapper import *
from Utils.Utils import is_in_range


class app_review_api_tests(unittest.TestCase):
    def setUp(self) -> None:
        self.api_wrapper = APIWrapper()
        self.app_review_api = App_Reviews_Api(self.api_wrapper)
    def test_get_app_review(self):
        app_review = self.app_review_api.get_app_review("1245620")
        result = app_review["success"]
        self.assertTrue(result,"failed to get app review")

    def test_default_app_review_number(self):
        app_review = self.app_review_api.get_app_review("1245620")
        result = self.app_review_api.get_review_numbers(app_review)
        self.assertEqual(result,20,"default review numbers should be 20!")

    def test_changing_default_app_review_number(self):
        app_review = self.app_review_api.get_app_review("1245620",review_num = 100)
        result = self.app_review_api.get_review_numbers(app_review)
        self.assertEqual(result,100,"review numbers should be 100!")

    def test_changing_app_review_language(self):
        app_review = self.app_review_api.get_app_review("1245620",language = "russian")
        result = self.app_review_api.check_review_languages(app_review,"russian")
        self.assertTrue(result,"The language of the review is not russian")

    def test_filtering_review_by_min_play_time(self):
        app_review = self.app_review_api.get_app_review("1245620",min_play_time = 999)
        play_time_list = self.app_review_api.get_play_time_of_reviews(app_review)
        result = is_in_range(play_time_list,lower_bound= 999)
        self.assertTrue(result,"Review play time not in range")

    def test_filtering_review_by_max_play_time(self):
        app_review = self.app_review_api.get_app_review("1245620",max_play_time = 100)
        play_time_list = self.app_review_api.get_play_time_of_reviews(app_review)
        result = is_in_range(play_time_list,upper_bound=100)
        self.assertTrue(result,"Review play time not in range")

    def test_filtering_review_range_of_play_time(self):
        app_review = self.app_review_api.get_app_review("1245620",min_play_time = 100,max_play_time = 200)
        play_time_list = self.app_review_api.get_play_time_of_reviews(app_review)
        result = is_in_range(play_time_list,lower_bound=100,upper_bound=200)
        self.assertTrue(result,"Review play time not in range")