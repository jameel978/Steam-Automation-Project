from jira import JIRA
import os
from Utils.Utils import read_json


class jira_wrapper:
    def __init__(self):
        cur_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.config = read_json(os.path.join(cur_dir,"Utils", "tokens.json"))
        self.JIRA_TOKEN = self.config['JIRA_TOKEN']
        self.JIRA_URL = self.config['JIRA_URL']
        self.JIRA_EMAIL = self.config['JIRA_EMAIL']
        self.PROJECT_KEY = self.config['PROJECT_KEY']
        self.auth_jira = JIRA(basic_auth=(self.JIRA_EMAIL, self.JIRA_TOKEN), options={'server': self.JIRA_URL})

    def create_issue(self, summery, description, issue_type="Bug",):
        issue_dict = {
            'project': {'key': self.PROJECT_KEY},
            'summary': summery,
            'description': description,
            'issuetype': {'name': issue_type},
        }
        new_issue = self.auth_jira.create_issue(fields=issue_dict)
        return new_issue.key

    def get_report_url(self):
        REPORT_URL = self.config['REPORT_URL']
        RUN_ID = self.config['RUN_ID']
        BRANCH_NAME = self.config['BRANCH_NAME']
        # Replace the branch name placeholder with the actual branch name
        modified_url = REPORT_URL.replace('BranchNamePlaceholder', BRANCH_NAME)
        # Replace the run ID placeholder with the actual run ID
        modified_url = modified_url.replace('RunIdPlaceholder', RUN_ID)
        return modified_url

import platform
