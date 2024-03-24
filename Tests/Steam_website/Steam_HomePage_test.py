import unittest
from Infra.Browser_wrapper import BrowserWrapper
from Logic.Website.Home_Page import Home_page
from Utils.Utils import check_keyword_in_all_sentences, get_browser
from parameterized import parameterized_class


#@parameterized_class(**get_browser())
@parameterized_class('browser',[(['chrome']), (['edge']), (['firefox'])])

class HomePage_Search_Tests(unittest.TestCase):
    browser = None
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)

    def setUp(self):
        self.Driver = BrowserWrapper().get_browser(self.browser)
        self.current_page = Home_page(self.Driver)

    def tearDown(self):
        self.current_page.quit()

    def test_search_result(self):
        self.current_page.write_in_search_input("Elden ring")
        self.assertEqual("Eldeng", self.current_page.get_search_results(), "Failed Search Test")

    def test_empty_search(self):
        self.current_page.write_in_search_input("")
        result = self.current_page.get_search_results()
        self.assertEqual("", result, "Failed Search Test")

    def test_search_suggestions(self):
        self.current_page.write_in_search_input("Elden ring", press_return=False)
        suggestions = self.current_page.get_search_suggestions()
        result = check_keyword_in_all_sentences(suggestions, "Elden ring")
        self.assertTrue(result, "Some suggestions are incorrect")
