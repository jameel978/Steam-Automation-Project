import json
import os.path



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
        "RUN_ID":  os.environ['RUN_ID'],
    }

    cur_dir = os.path.dirname(os.path.abspath(__file__))
    config = os.path.join(cur_dir, "tokens.json")
    create_tokens_file(my_tokens, config)


if __name__ == "__main__":
    main()




