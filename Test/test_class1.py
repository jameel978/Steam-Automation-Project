# test_class2.py
import unittest
from selenium import webdriver
from parameterized import parameterized, parameterized_class

def get_browser():
    browser = {'attrs': "browser","input_values":[(['chrome']), (['edge']), (['firefox'])]}
    return browser

@parameterized_class(**get_browser())
class TestClass2(unittest.TestCase):
    browser = None
    def __init__(self, methodName='runTest', browser=None):
        super(TestClass2, self).__init__(methodName)
    def setUp(self):
        if self.browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif self.browser == 'edge':
            self.driver = webdriver.Edge()
        elif self.browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            print(self.browser)
            raise ValueError(f"Unsupported browser")

    def tearDown(self):
        self.driver.quit()

    def test_class2_example_1(self):
        pass
