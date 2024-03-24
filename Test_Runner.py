import pytest
import os

from Infra.Jira_wrapper import jira_wrapper
from Utils.Utils import read_json, ErrorCapturingPlugin


def run_tests(test_cases,output_folder,report_name,test_type = 'serial'):
    pytest_args = []
    pytest_args.append("-v")

    #for file_path, test_class, test_method in test_cases:
    #    pytest_args.append(f'{file_path}::{test_class}::{test_method}')

    pytest_args.append(test_cases)
    pytest_args.append(f'--html={output_folder}/{report_name}_report.html')
    if test_type == "parallel":
        pytest_args.append("-n")
        #pytest_args.append("auto")
        pytest_args.append("4")

    pytest_args.append("-q")
    pytest_args.append(f"--alluredir=allure-results")

    plugin = ErrorCapturingPlugin()
    pytest.main(pytest_args,plugins=[plugin])

    # Print captured test names and errors
    jira_instance = jira_wrapper()
    if plugin.errors:
        #print("Errors encountered during testing:")
        for test_name, error_message in plugin.errors.items():
            #print(f"Test: {test_name}\nError: {error_message}\n")
            jira_instance.create_issue(test_name,error_message)
    else:
        pass
        #print("All tests passed!")


if __name__ == "__main__":
    API_Tests = "Tests/Steam_API"
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    test_config = read_json(os.path.join(cur_dir, "Tests/Steam_API/Config/API_Tests_Config.json"))
    test_type = test_config["test_type"]
    run_tests(API_Tests, 'Results',"API",test_type)

    UI_Tests = "Tests/Steam_website"
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    test_config = read_json(os.path.join(cur_dir, "Tests/Steam_website/Configs/UI_Tests_Config.json"))
    test_type = test_config["test_type"]
    run_tests(UI_Tests, 'Results',"UI",test_type)










