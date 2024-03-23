import importlib
import inspect
import os
import time
from concurrent.futures import ThreadPoolExecutor

import pytest
import unittest
import unittest
import inspect

import os
import subprocess
import unittest
import importlib.util

from Utils.Utils import read_json, ErrorCapturingPlugin, find_test_methods


def run_tests(test_cases,output_folder,report_name,test_type = 'serial'):
    pytest_args = []
    for file_path, test_class, test_method in test_cases:
        pytest_args.append(f'{file_path}::{test_class}::{test_method}')

    pytest_args.append(f'--html={output_folder}/{report_name}_report.html')
    if test_type == "parallel":
        pytest_args.append("-n")
        #pytest_args.append("auto")
        pytest_args.append("4")
    pytest_args.append("-q")
    plugin = ErrorCapturingPlugin()
    pytest.main(pytest_args,plugins=[plugin])

    # Print captured test names and errors
    if plugin.errors:
        print("Errors encountered during testing:")
        for test_name, error_message in plugin.errors.items():
            print(f"Test: {test_name}\nError: {error_message}\n")
    else:
        print("All tests passed!")


if __name__ == "__main__":
    UI_Tests = "Tests/Steam_API"
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    test_config = read_json(os.path.join(cur_dir, "Tests/Steam_API/Config/API_Tests_Config.json"))
    test_type = test_config["test_type"]
    test_methods = find_test_methods(UI_Tests)
    run_tests(test_methods, 'Results',"API",test_type)


    UI_Tests = "Tests/Steam_website"
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    test_config = read_json(os.path.join(cur_dir, "Tests/Steam_website/Configs/UI_Tests_Config.json"))
    test_type = test_config["test_type"]
    test_methods = find_test_methods(UI_Tests)
    run_tests(test_methods, 'Results',"UI",test_type)










