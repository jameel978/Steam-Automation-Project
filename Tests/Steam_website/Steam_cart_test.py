import time
import unittest
from Logic.Steam_API.Steam_token_API import *
from Logic.Website.Cart_page import *
from Logic.Steam_API.Cart_API import *
from Infra.Browser_wrapper import *
from Infra.Api_wrapper import *

class steam_cart_tests(unittest.TestCase):
    def __init__(self, methodName='runTest', cap=None):
        super().__init__(methodName)
        if cap == None:
            cap = BrowserWrapper().get_default_browser_cap()
        self.cap = cap
    def setUp(self):
        self.current_page = Cart_page(self.cap,True)
        self.api_wrapper = APIWrapper(self.current_page.get_cockies())
        self.access_token = Steam_Token_API(self.api_wrapper).get_token()
        self.api_wrapper = APIWrapper()
        self.cart_api = Cart_API(self.api_wrapper)

    def tearDown(self):
        self.current_page.remove_all_items_from_cart()
        self.current_page.quit()

    def test_add_to_cart(self):
        self.current_page.remove_all_items_from_cart()
        self.cart_api.add_to_cart(self.access_token,48700,12397)
        self.current_page.refresh_page()
        title_result = self.current_page.get_items_in_carts_names()
        self.assertIn("Mount & Blade Legacy Collection",title_result)
