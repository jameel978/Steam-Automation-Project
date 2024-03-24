import unittest
from Infra.Api_wrapper import *
from Logic.Steam_API.Advanced_search_API import *
from Logic.Steam_API.APP_Details_API import *
from Utils.Utils import is_sorted_descending, is_sorted_ascending


class app_review_api_tests(unittest.TestCase):
    def setUp(self) -> None:
        self.api_wrapper = APIWrapper()
        self.advanced_search_api = Advanced_search_API(self.api_wrapper)
    def test_advanced_search(self):
        search_results = self.advanced_search_api.get_search_results("elden ring")
        result = search_results['items']
        self.assertTrue(len(result) != 0,"Results are Empty")

    def test_sorting_by_ACS_price_advanced_search(self):
        search_results = self.advanced_search_api.get_search_results("elden ring", sort_by_high_price=True,games_only=True)
        id_list_of_search = self.advanced_search_api.get_app_ids_from_search_results(search_results)[:6]
        price_list = APP_Details_API(self.api_wrapper).get_app_prices_using_ids_from_app_details(id_list_of_search)
        result = is_sorted_descending(price_list)
        self.assertTrue(result,"prices are not in ascending order")

    def test_sorting_by_DESC_price_advanced_search(self):
        search_results = self.advanced_search_api.get_search_results("elden ring", sort_by_low_price=True,games_only=True,hide_free_games = True)
        id_list_of_search = self.advanced_search_api.get_app_ids_from_search_results(search_results)[:6]
        price_list = APP_Details_API(self.api_wrapper).get_app_prices_using_ids_from_app_details(id_list_of_search)
        result = is_sorted_ascending(price_list)
        self.assertTrue(result,"prices are not in descending order in the search")