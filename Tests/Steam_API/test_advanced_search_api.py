import os
import unittest

from Infra.Api_wrapper import APIWrapper
from Logic.Steam_API.APP_Details_API import APP_Details_API
from Logic.Steam_API.Advanced_search_API import Advanced_search_API
from Utils.Utils import is_sorted_descending, is_sorted_ascending, read_json


class app_review_api_tests(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.test_params = read_json(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Config",
                                              f"{os.path.basename(__file__)[:-3]}.json"))
    
    def setUp(self) -> None:
        self.api_wrapper = APIWrapper()
        self.advanced_search_api = Advanced_search_API(self.api_wrapper)
    def test_advanced_search(self):
        search_results = self.advanced_search_api.get_search_results(self.test_params['app_name'])
        result = search_results['items']
        self.assertTrue(len(result) != 0,"Results are Empty")

    def test_sorting_by_ACS_price_advanced_search(self):
        search_results = self.advanced_search_api.get_search_results(self.test_params['app_name'], sort_by_high_price=True,games_only=True)
        id_list_of_search = self.advanced_search_api.get_app_ids_from_search_results(search_results)[:6]
        price_list = APP_Details_API(self.api_wrapper).get_app_prices_using_ids_from_app_details(id_list_of_search)
        result = is_sorted_descending(price_list)
        self.assertTrue(result,"prices are not in ascending order")

    def test_sorting_by_DESC_price_advanced_search(self):
        search_results = self.advanced_search_api.get_search_results(self.test_params['app_name'], sort_by_low_price=True,games_only=True,hide_free_games = True)
        id_list_of_search = self.advanced_search_api.get_app_ids_from_search_results(search_results)[:6]
        price_list = APP_Details_API(self.api_wrapper).get_app_prices_using_ids_from_app_details(id_list_of_search)
        result = is_sorted_ascending(price_list)
        self.assertTrue(result,"prices are not in descending order in the search")