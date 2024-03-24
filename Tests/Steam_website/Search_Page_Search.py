import os
import time
import unittest

from Infra.Api_wrapper import APIWrapper
from Infra.Browser_wrapper import BrowserWrapper
from Logic.Steam_API.Cart_API import Cart_API
from Logic.Steam_API.Steam_token_API import Steam_Token_API
from Logic.Steam_API.Wishlist_API import Wishlist_API
from Logic.Website.Home_Page import Home_page
from Logic.Website.Search_Page import Search_page
from Utils.Utils import check_keyword_in_all_sentences, get_browser, read_json
from parameterized import parameterized_class


#@parameterized_class(**get_browser())
@parameterized_class('browser',[(['chrome']), (['edge']), (['firefox'])])
class HomePage_Search_Tests(unittest.TestCase):
    browser = None
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.test_params = read_json(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Configs", f"{os.path.basename(__file__)[:-3]}.json"))

    def setUp(self):
        self.Driver = BrowserWrapper().get_browser(self.browser)
        self.current_page = Search_page(self.Driver,True)
        self.api_wrapper = APIWrapper(self.current_page.get_cockies())
        self.wishlist_api = Wishlist_API(self.api_wrapper)
        self.access_token = Steam_Token_API(self.api_wrapper).get_token()
        self.cart_api = Cart_API(self.api_wrapper)

    def tearDown(self):
        self.current_page.quit()

    def test_hide_wishlist_from_search(self):
        game_name,game_id = self.current_page.get_random_game()
        self.wishlist_api.add_to_wishlist(game_id)
        self.current_page.refresh_page()
        self.current_page.hide_wishlist_games()
        result = self.current_page.check_if_game_in_page(game_id)
        self.wishlist_api.remove_from_wishlist(game_id)
        self.assertFalse(result,f"{game_name} was found in the result")

    def test_hide_owned_from_search(self):
        self.current_page.hide_owned_games()
        result = self.current_page.check_if_game_in_page(730)
        self.assertFalse(result,f"Counter-Strike 2 was found in the result")

    def test_price_slider(self):
        self.current_page.move_price_slider(-200)
        prices_results = self.current_page.get_games_prices()
        for result in prices_results:
            game_name, game_price = result
            self.assertEqual('Free',game_price,f'{game_name} current price is {game_price}')

