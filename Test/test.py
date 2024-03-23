import os
import unittest
import pytest
from concurrent.futures import ThreadPoolExecutor
from io import StringIO
import time
from Infra.Browser_wrapper import BrowserWrapper
from Utils.Utils import get_unittest_classes, prepair_all_tests, read_json
from selenium import webdriver
import random

class SeleniumTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        folder_path = "../Tests/Beta_tests"
        test_classes = get_unittest_classes(folder_path)
        all_test_cases = prepair_all_tests(test_classes)
        # read from config
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        test_config = read_json(os.path.join(cur_dir, "../Tests/Steam_website/Configs/Tests_config.json"))
        browser_caps = BrowserWrapper(test_config).get_caps()
        self.test_cases_with_caps = [(i, j, browser) for i, j in all_test_cases for browser in browser_caps]
        random.shuffle(self.test_cases_with_caps)
        print(self.test_cases_with_caps)

    def test_main(self):
        for test in self.test_cases_with_caps:
            test_name = test[1]
            test_browser = test[2][2]
            with self.subTest(msg=f"'{test_name}' on {test_browser}", test=test):
                print(f"'{test_name}' on {test_browser}")
                suite = unittest.TestSuite()
                suite.addTest(self.init_test(test))
                # Run the test suite
                result = unittest.TextTestRunner().run(suite)
                self.assertTrue(result.wasSuccessful())

    def init_test(self,input_):
        return input_[0](input_[1], cap=input_[2])

    def test_loop(self):
        for i in range(5):
            with self.subTest("Message for this subtest", i=i):
                self.assertEqual(i % 2, 0)

if __name__ == "__main__":
    unittest.main()
