import os
import unittest
from Infra.Browser_wrapper import BrowserWrapper
from Logic.Website.Home_Page import Home_page
from Utils.Utils import check_keyword_in_all_sentences, get_browsers, read_json
from parameterized import parameterized_class


@parameterized_class(get_browsers())
class HomePage_Search_Tests(unittest.TestCase):
    browser = None
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.test_params = read_json(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Configs", f"{os.path.basename(__file__)[:-3]}.json"))

    def setUp(self):
        self.Driver = BrowserWrapper().get_browser(self.browser)
        self.current_page = Home_page(self.Driver)

    def tearDown(self):
        self.current_page.quit()

    def test_search_result(self):
        self.current_page.write_in_search_input(self.test_params['app_name'])
        result = self.current_page.get_search_results()
        self.assertEqual(self.test_params['app_name'], result, "Failed Search Test")

    def test_empty_search(self):
        self.current_page.write_in_search_input("")
        result = self.current_page.get_search_results()
        self.assertEqual("", result, "Failed Search Test")

    def test_search_suggestions(self):
        self.current_page.write_in_search_input(self.test_params['app_name'], press_return=False)
        suggestions = self.current_page.get_search_suggestions()
        result = check_keyword_in_all_sentences(suggestions, self.test_params['app_name'])
        self.assertTrue(result, "Some suggestions are incorrect")
