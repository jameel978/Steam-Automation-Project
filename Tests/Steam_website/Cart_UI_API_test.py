import os
import unittest
from Infra.Api_wrapper import APIWrapper
from Infra.Browser_wrapper import BrowserWrapper
from Logic.Steam_API.Cart_API import Cart_API
from Logic.Steam_API.Steam_token_API import Steam_Token_API
from Logic.Website.Cart_page import Cart_page
from parameterized import parameterized_class
from Utils.Utils import get_browser, read_json


#@parameterized_class(**get_browser())
@parameterized_class('browser',[(['chrome']), (['edge']), (['firefox'])])
class steam_cart_tests(unittest.TestCase):
    browser = None
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.test_params = read_json(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Config", f"{os.path.basename(__file__)[:-3]}.json"))

    def setUp(self):
        self.Driver = BrowserWrapper().get_browser(self.browser)
        self.current_page = Cart_page(self.Driver,True)
        self.api_wrapper = APIWrapper(self.current_page.get_cockies())
        self.access_token = Steam_Token_API(self.api_wrapper).get_token()
        self.api_wrapper = APIWrapper()
        self.cart_api = Cart_API(self.api_wrapper)

    def tearDown(self):
        self.current_page.remove_all_items_from_cart()
        self.current_page.quit()

    def test_add_to_cart(self):
        self.current_page.remove_all_items_from_cart()
        self.cart_api.add_to_cart(self.access_token,self.test_params['app_id'],self.test_params['bundle_id'])
        self.current_page.refresh_page()
        title_result = self.current_page.get_items_in_carts_names()
        self.assertIn(self.test_params['app_name'],title_result)


