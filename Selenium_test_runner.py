from concurrent.futures import ThreadPoolExecutor
from html_testRunner import HTMLTestRunner
from io import StringIO
import time
import os
import importlib.util
import inspect
import unittest
from Infra.Browser_wrapper import *
from Utils.Utils import *


def run_test(_current_test):
    test_name = _current_test[1]
    test_browser = _current_test[2][2]
    suite = unittest.TestSuite()
    suite.addTest(init_test(_current_test))
    # Run the test suite
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    report_filename = os.path.join(cur_dir,"Reports", f'{test_name}_{test_browser}_report.html')
    # Open the file to write the HTML report
    with open(report_filename, 'w') as report_file:
        # Use HTMLTestRunner to run the test suite and generate the HTML report
        runner = HTMLTestRunner(
            stream=report_file,
            verbosity=2
        )
        _result = runner.run(suite)
    if _result.wasSuccessful():
            print(f"'{test_name}' passed! on {test_browser}")
    else:
        # Print the error details
        for test, error in _result.errors:
            print(f"'{test_name}' Failed! on {test_browser}")
            print(f"Error in test '{test.id()}':")
            print(error)
    return _result

def init_test(input_):
    return input_[0](input_[1],cap = input_[2])

def run_tests_in_parallel(test_cases):
    #with ThreadPoolExecutor(max_workers=4) as executor:
    with ThreadPoolExecutor(max_workers=len(test_cases)) as executor:
        _results = list(executor.map(run_test, test_cases))
    return _results


def run_tests_in_serrial(_test_classes):
    _results = []
    for test in _test_classes:
        _result = run_test(test)
        _results.append(_result)
    return _results

def get_unittest_classes(_folder_path):
    unittest_classes = []
    # Iterate through files in the folder
    for file_name in os.listdir(_folder_path):
        if file_name.endswith('.py'):
            module_name = os.path.splitext(file_name)[0]
            module_path = os.path.join(_folder_path, file_name)
            # Load the module
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Inspect the module for classes that subclass unittest.TestCase
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, unittest.TestCase) and obj != unittest.TestCase:
                    unittest_classes.append(obj)
    return unittest_classes


if __name__ == '__main__':
    folder_path = "Tests/Steam_website"
    test_classes = get_unittest_classes(folder_path)
    all_test_cases = prepair_all_tests(test_classes)
    # read from config
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    test_config = read_json(os.path.join(cur_dir, "Tests/Steam_website/Configs/Tests_config.json"))
    browser_caps = BrowserWrapper(test_config).get_caps()
    test_cases_with_caps = [(i,j,(browser)) for i,j in all_test_cases for browser in browser_caps]
    random.shuffle(test_cases_with_caps)
    test_type = test_config['test_config']["test_type"]
    start_time = time.time()
    results = None
    if test_type == 'serial':
        print("running test in serial")
        print("")
        results = run_tests_in_serrial(test_cases_with_caps)
    elif test_type == 'parallel':
        print("running test in parallel")
        print("")
        results = run_tests_in_parallel(test_cases_with_caps)
    elapsed_time = time.time() - start_time
    if results == None:
        raise Exception("Tests Failed to Run")
    else:
        test_pass = 0
        test_fail = 0
        for result in results:
            if result.wasSuccessful():
                test_pass += 1
            else:
                test_fail += 1
        if test_fail == 0:
            print(f"All tests Passed,number of tests {test_pass}")
        else:
            print(f"Some tests Failed,number of failed tests {test_fail}, number of passed tests {test_pass}")
    print("")
    print(f"Total Run time: {elapsed_time:.2f} seconds")
