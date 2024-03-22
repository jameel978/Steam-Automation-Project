import unittest

from Infra.Api_wrapper import *
from Logic.Website.Wishlist_Page import *
from Logic.Steam_API.Steam_token_API import *
from Logic.Steam_API.Wishlist_API import *
from Infra.Browser_wrapper import *
from Utils.Utils import *

class whishlist_api_tests(unittest.TestCase):
    def __init__(self, methodName='runTest', cap=None):
        super().__init__(methodName)
        if cap == None:
            cap = BrowserWrapper().get_default_browser_cap()
        self.cap = cap

    def setUp(self):
        self.current_page = Wishlist_Page(self.cap,True)
        self.api_wrapper = APIWrapper(self.current_page.get_cockies())
        #self.current_token = Steam_Token_API(self.api_wrapper).get_token()
        self.wishlist_api = Wishlist_API(self.api_wrapper)
        self.wishlist_api.add_to_wishlist("1174180")
        self.current_page.refresh_page()

    def tearDown(self):
        self.current_page.remove_games_from_wish_list()
        self.current_page.quit()

    def test_add_game_to_wishlist(self):
        result = self.current_page.get_wishlist_games_names()
        self.assertIn("Red Dead Redemption 2",result)

    def test_remove_from_wishlist(self):
        self.wishlist_api.remove_from_wishlist("1174180")
        self.current_page.refresh_page()
        result = self.current_page.get_wishlist_games_count()
        self.assertEqual(result,0)