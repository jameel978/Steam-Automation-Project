import unittest
from Logic.Website.Home_Page import *
from Infra.Browser_wrapper import *
from Utils.Utils import *
@pytest.fixture(params=['chrome','edge','firefox'])
def get_driver(request):
    browser = request.param
    print(browser)
    return BrowserWrapper().get_browser_cap(browser)

class building_pc_tests(unittest.TestCase):
    def __init__(self, methodName='runTest', cap=None):
        super().__init__(methodName)
        if cap == None:
            cap = BrowserWrapper().get_default_browser_cap()
        self.cap = cap

    def setUp(self):
        self.current_page = Home_page(self.cap)

    def tearDown(self):
        self.current_page.quit()

    def test_search_result(self):
        self.current_page.write_in_search_input("Elden ring")
        result = self.current_page.get_search_results()
        self.assertEqual("Elden ring",result,"Failed Search Test")

    def test_empty_search(self):
        self.current_page.write_in_search_input("")
        result = self.current_page.get_search_results()
        self.assertEqual("",result,"Failed Search Test")

    def test_search_suggestions(self):
        self.current_page.write_in_search_input("Elden ring",press_return=False)
        suggestions = self.current_page.get_search_suggestions()
        result = check_keyword_in_all_sentences(suggestions,"Elden ring")
        self.assertTrue(result,"Some suggestions are incorrect")
