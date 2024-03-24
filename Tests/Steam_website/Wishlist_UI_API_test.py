import os
import unittest

from Infra.Api_wrapper import APIWrapper
from Infra.Browser_wrapper import BrowserWrapper
from Logic.Steam_API.Wishlist_API import Wishlist_API
from Logic.Website.Wishlist_Page import Wishlist_Page
from parameterized import parameterized, parameterized_class
from Utils.Utils import get_browser, read_json


#@parameterized_class(**get_browser())
@parameterized_class('browser',[(['chrome']), (['edge']), (['firefox'])])
class wishlist_api_tests(unittest.TestCase):
    browser = None
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.test_params = read_json(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Configs", f"{os.path.basename(__file__)[:-3]}.json"))

    def setUp(self):
        self.Driver = BrowserWrapper().get_browser(self.browser)
        self.current_page = Wishlist_Page(self.Driver,True)
        self.api_wrapper = APIWrapper(self.current_page.get_cockies())
        self.wishlist_api = Wishlist_API(self.api_wrapper)
        self.wishlist_api.add_to_wishlist(self.test_params['app_id'])
        self.current_page.refresh_page()

    def tearDown(self):
        self.current_page.remove_games_from_wish_list()
        self.current_page.quit()

    def test_add_game_to_wishlist(self):
        result = self.current_page.get_wishlist_games_names()
        self.assertIn(self.test_params['app_name'],result)

    def test_remove_from_wishlist(self):
        self.wishlist_api.remove_from_wishlist(self.test_params['app_id'])
        self.current_page.refresh_page()
        result = self.current_page.get_wishlist_games_count()
        self.assertEqual(result,0)



