import unittest
from Logic.Steam_API.APP_Reviews_API import *
from Infra.Api_wrapper import *
from Utils.Utils import is_in_range


class app_review_api_tests(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.test_params = read_json(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Config",
                                                  f"{os.path.basename(__file__)[:-3]}.json"))

    def setUp(self) -> None:
        self.api_wrapper = APIWrapper()
        self.app_review_api = App_Reviews_Api(self.api_wrapper)
    def test_get_app_review(self):
        app_review = self.app_review_api.get_app_review(self.test_params["app"])
        result = app_review["success"]
        self.assertTrue(result,"failed to get app review")

    def test_default_app_review_number(self):
        app_review = self.app_review_api.get_app_review(self.test_params["app"])
        result = self.app_review_api.get_review_numbers(app_review)
        self.assertEqual(result,20,"default review numbers should be 20!")

    def test_changing_default_app_review_number(self):
        app_review = self.app_review_api.get_app_review(self.test_params["app"],review_num = self.test_params['max_play_time'])
        result = self.app_review_api.get_review_numbers(app_review)
        self.assertEqual(result,self.test_params['max_play_time'],"review numbers should be self.test_params['max_play_time']!")

    def test_changing_app_review_language(self):
        app_review = self.app_review_api.get_app_review(self.test_params["app"],language = self.test_params["language"])
        result = self.app_review_api.check_review_languages(app_review,self.test_params["language"])
        self.assertTrue(result,f"The language of the review is not {self.test_params['language']}")

    def test_filtering_review_by_min_play_time(self):
        app_review = self.app_review_api.get_app_review(self.test_params["app"],min_play_time = self.test_params['min_play_time'])
        play_time_list = self.app_review_api.get_play_time_of_reviews(app_review)
        result = is_in_range(play_time_list,lower_bound= self.test_params['min_play_time'])
        self.assertTrue(result,"Review play time not in range")

    def test_filtering_review_by_max_play_time(self):
        app_review = self.app_review_api.get_app_review(self.test_params["app"],max_play_time = self.test_params['max_play_time'])
        play_time_list = self.app_review_api.get_play_time_of_reviews(app_review)
        result = is_in_range(play_time_list,upper_bound=self.test_params['max_play_time'])
        self.assertTrue(result,"Review play time not in range")

    def test_filtering_review_range_of_play_time(self):
        app_review = self.app_review_api.get_app_review(self.test_params["app"],min_play_time = self.test_params['max_play_time'],max_play_time = self.test_params['min_play_time_with_max'])
        play_time_list = self.app_review_api.get_play_time_of_reviews(app_review)
        result = is_in_range(play_time_list,lower_bound=self.test_params['max_play_time'],upper_bound=self.test_params['min_play_time_with_max'])
        self.assertTrue(result,"Review play time not in range")