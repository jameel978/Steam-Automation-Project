import importlib
import json
import inspect
import types
import os
import unittest
import pytest
import platform

def check_if_list_is_in_order(lst, order):
    if order == "descending":
        for i in range(len(lst) - 1):
            if lst[i] < lst[i + 1]:
                return False
        return True
    elif order == "increasing":
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                return False
        return True
    else:
        return False


def read_json(location):
    with open(location) as f:
        data = json.load(f)
    return data


def get_all_tests(my_class):
    methodList = [v for n, v in inspect.getmembers(my_class, inspect.ismethod) if isinstance(v, types.MethodType)]
    test_list = [test.__name__ for test in methodList if "test_" in test.__name__]
    return test_list


def extract_idf_from_link(link):
    id = link.split("/")[5]
    return id


def is_sorted_descending(nums):
    return all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1))


def is_sorted_ascending(nums):
    return all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))


def is_in_range(lst, lower_bound=None, upper_bound=None):
    if lower_bound is not None and upper_bound is not None:
        for num in lst:
            if not lower_bound <= num <= upper_bound:
                return False
    elif lower_bound is not None:
        for num in lst:
            if num < lower_bound:
                return False
    elif upper_bound is not None:
        for num in lst:
            if num > upper_bound:
                return False
    return True


def check_keyword_in_all_sentences(sentence_list, keyword):
    """
    Check if a keyword is present in all of the sentences in a given list.

    Parameters:
        sentence_list (list): A list of sentences to search within.
        keyword (str): The keyword to search for.

    Returns:
        bool: True if the keyword is found in all of the sentences, False otherwise.
    """
    # Convert the keyword to lowercase for case-insensitive comparison
    keyword_lower = keyword.lower()

    # Iterate over each sentence in the list
    for sentence in sentence_list:
        # Convert the current sentence to lowercase for case-insensitive comparison
        sentence_lower = sentence.lower()

        # Check if the keyword is present in the current sentence
        if keyword_lower not in sentence_lower:
            return False  # Keyword not found in this sentence, return False

    # Keyword found in all sentences
    return True


def get_browser():
    cur_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_loca = os.path.join(cur_dir, 'Tests/Steam_website/Configs/', "UI_Tests_Config.json")
    browser_names = read_json(config_loca)['browser_config']
    input_values = [[[name]] for name in browser_names]
    _args = {'attrs': "browser", "input_values": input_values}
    return _args


def find_test_methods(folder_path):
    test_cases = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                module_name = os.path.splitext(os.path.relpath(file_path, folder_path).replace(os.sep, '.'))[0]
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                for name in dir(module):
                    obj = getattr(module, name)
                    if isinstance(obj, type) and issubclass(obj, unittest.TestCase):
                        test_methods = [method for method in dir(obj) if method.startswith('test_')]
                        if test_methods:
                            test_cases.extend([[file_path, obj.__name__, method] for method in test_methods])
    return test_cases

# Custom plugin to capture output
class ErrorCapturingPlugin:
    def __init__(self):
        self.errors = {}
    def pytest_runtest_logreport(self, report):
        if report.failed:
            test_name = report.nodeid
            error_message = report.longreprtext
            self.errors[test_name] = error_message


def format_test_name(test_name):
    # Split the test name by '::' to extract relevant information
    parts = test_name.split("::")
    # Extract relevant parts from the split test name
    test_case = parts[-1]
    test_suite = parts[-3]  # Extract test suite

    # Construct the formatted string
    if test_name.split("/")[1] == "Steam_website":
        browser = parts[-2].split("_")[-1]  # Extract browser type
        formatted_string = f"{test_case} on {browser} failed in {test_suite}"
    else:
        formatted_string = f"{test_case} failed in {test_suite}"

    return formatted_string

def add_url_to_description(disc,url):
    lines = f"{url} \n\n\n"
    return lines + disc

def save_environment_info(output_file):
    os_platform = platform.platform()
    os_release = platform.release()
    os_version = platform.version()
    python_version = platform.python_version()

    with open(output_file, 'w') as f:
        f.write(f"OS_Platform={os_platform}\n")
        f.write(f"OS_Release={os_release}\n")
        f.write(f"OS_Version={os_version}\n")
        f.write(f"Python_Version={python_version}\n")
