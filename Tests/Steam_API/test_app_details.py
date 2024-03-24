import unittest
from Infra.Api_wrapper import APIWrapper
from Logic.Steam_API.APP_Details_API import APP_Details_API


class app_details_api_tests(unittest.TestCase):
    def setUp(self) -> None:
        self.api_wrapper = APIWrapper()
        self.app_details_api = APP_Details_API(self.api_wrapper)

    def test_get_app_details(self):
        app_details = self.app_details_api.get_app_details("1245620")
        result = app_details["success"]
        self.assertTrue(result,"failed to get app detail")

    def test_get_app_name(self):
        app_details = self.app_details_api.get_app_details("1245620")
        app_name = self.app_details_api.get_app_name_from_app_details(app_details)
        self.assertEqual(app_name,"ELDEN RING","Incorrect App Name")

    def test_get_app_details_currency_us(self):
        app_details = self.app_details_api.get_app_details("1245620",country_code = "US")
        price_currency = self.app_details_api.get_app_price_currency(app_details)
        self.assertEqual(price_currency, "USD", "Incorrect App Price Currency")

    def test_get_app_details_currency_uk(self):
        app_details = self.app_details_api.get_app_details("1245620",country_code = "UK")
        price_currency = self.app_details_api.get_app_price_currency(app_details)
        self.assertEqual(price_currency, "GBP", "Incorrect App Price Currency")

    def test_get_app_details_currency_IL(self):
        app_details = self.app_details_api.get_app_details("1245620",country_code = "IL")
        price_currency = self.app_details_api.get_app_price_currency(app_details)
        #self.assertEqual(price_currency, "ILS", "Incorrect App Price Currency")
        self.assertEqual(price_currency, "USD", "Incorrect App Price Currency")
        

