from concurrent.futures import ThreadPoolExecutor
import pytest
from io import StringIO
import time
from Infra.Browser_wrapper import *
from Utils.Utils import *

def run_test(_current_test):
    test_name = _current_test[1]
    test_browser = _current_test[2][2]
    suite = unittest.TestSuite()
    suite.addTest(init_test(_current_test))
    # Run the test suite
    _result = unittest.TextTestRunner(stream=StringIO(), verbosity=2).run(suite)
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
    with ThreadPoolExecutor(max_workers=len(test_cases)) as executor:
        _results = list(executor.map(run_test, test_cases))
    return _results


if __name__ == "__main__":
    folder_path = "Tests/Beta_tests"
    test_classes = get_unittest_classes(folder_path)
    all_test_cases = prepair_all_tests(test_classes)
    print(all_test_cases)
    # read from config
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    test_config = read_json(os.path.join(cur_dir, "Tests/Steam_website/Configs/Tests_config.json"))
    browser_caps = BrowserWrapper(test_config).get_caps()
    test_cases_with_caps = [(i,j,(browser)) for i,j in all_test_cases for browser in browser_caps]
    random.shuffle(test_cases_with_caps)
    test_type = test_config['test_config']["test_type"]
    start_time = time.time()
    results = None
    if test_type == 'parallel':
        print("running tests in parallel")
        results = run_tests_in_parallel(test_cases_with_caps)
    else:
        print("running tests in serial")
        results = [run_test(test) for test in test_cases_with_caps]

    elapsed_time = time.time() - start_time
    if results is None:
        raise Exception("Tests Failed to Run")
    else:
        test_pass = sum(1 for result in results if result.wasSuccessful())
        test_fail = len(results) - test_pass
        if test_fail == 0:
            print(f"All tests Passed, number of tests {test_pass}")
        else:
            print(f"Some tests Failed, number of failed tests {test_fail}, number of passed tests {test_pass}")
    print("")
    print(f"Total Run time: {elapsed_time:.2f} seconds")

