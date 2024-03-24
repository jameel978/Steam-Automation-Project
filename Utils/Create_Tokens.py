import json
import sys
import argparse
import os.path
import requests


def create_tokens_file(dictionary, filename='tokens.json'):
    with open(filename, 'w') as file:
        json.dump(dictionary, file)


def get_run_id(data):
    # Check if the data contains 'jobs' key
    if 'jobs' in data:
        # Iterate over each job
        for job in data['jobs']:
            # Check if 'run_id' is present in the job
            if 'run_id' in job:
                return job['run_id']
    # If run_id is not found, return None
    return None

def main():
    env_cookies = json.loads(os.environ['COOKIES'])
    jira_tokens = json.loads(os.environ['JIRA_TOKENS'])

    my_tokens = {
        "chrome": env_cookies['chrome'],
        "firefox": env_cookies['firefox'],
        "edge": env_cookies['edge'],
        "JIRA_EMAIL": jira_tokens['JIRA_EMAIL'],
        "JIRA_TOKEN": jira_tokens['JIRA_TOKEN'],
        "JIRA_URL": jira_tokens['JIRA_URL'],
        "PROJECT_KEY": jira_tokens['PROJECT_KEY'],
        "REPORT_URL": jira_tokens['REPORT_URL'],
        "BRANCH_NAME" :  os.environ['BRANCH_NAME'],
    }
    #GET run_id from workflow because it is not supported from github actions ! YET
    # Define the necessary parameters
    url = f'https://api.github.com/repos/{os.environ["REPO_NAME"]}/actions/runs/{os.environ["RUN_ID"]}/jobs'
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {os.environ["G_TOKEN"]}',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    token_response = requests.get(url, headers=headers).json()
    # Check if the request was successful (status code 200)

    my_tokens['RUN_ID'] = f'{os.environ["RUN_ID"]}_{get_run_id(token_response)}'
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    config = os.path.join(cur_dir, "tokens.json")
    create_tokens_file(my_tokens, config)
    print(url)

if __name__ == "__main__":
    main()




