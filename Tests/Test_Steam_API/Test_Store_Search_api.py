import unittest
from Infra.Api_wrapper import APIWrapper
from Logic.Steam_API.Store_Search_API import *
from Logic.Steam_API.APP_Details_API import *
from Logic.Utils import *


class store_search_tests(unittest.TestCase):
    def setUp(self) -> None:
        self.api_wrapper = APIWrapper()
        self.store_search = Store_Search_API(self.api_wrapper)
        self.search_result = self.store_search.get_search_result("Elden Ring", country_code="US")
        self.app_names = self.store_search.get_names_of_found_serach_apps(self.search_result)

    def test_store_search(self):
        for app in self.app_names:
            self.assertIn("Elden ring".lower(), app.lower(),f"Elden ring not found in {app.lower()}")

    def test_store_search_found_apps(self):
        app_ids = self.store_search.get_app_id_from_app_details(self.search_result)
        for name, id in zip(self.app_names, app_ids):
            details_api = APP_Details_API(self.api_wrapper)
            app_details = details_api.get_app_details(id)
            app_name = details_api.get_app_name_from_app_details(app_details)
            self.assertEqual(app_name, name,f"Found app name {app_name}, Expected app name {name}")


