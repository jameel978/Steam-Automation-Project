import importlib
import inspect
import os
import time
from concurrent.futures import ThreadPoolExecutor

import pytest
import unittest
from Utils.Utils import *
import unittest
import inspect

import os
import subprocess
import unittest
import importlib.util

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


def run_tests(test_cases,output_folder,run_type = 'serial'):
    pytest_args = []
    for file_path, test_class, test_method in test_cases:
        pytest_args.append(f'{file_path}::{test_class}::{test_method}')
    pytest_args.append(f'--html={output_folder}/report.html')
    pytest_args.append("-n")
    pytest_args.append("auto")
    pytest.main(pytest_args)



if __name__ == "__main__":
    folder_path = "Tests/Steam_website"
    output_folder = "Reports"
    #run_tests(test_folder, output_folder)
    test_methods = find_test_methods(folder_path)
    run_tests(test_methods,output_folder)

