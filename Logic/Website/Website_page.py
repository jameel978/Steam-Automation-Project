from Infra.Driver_instance import Driverinstance
from selenium.webdriver.common.by import By
import json
from Utils.Utils import *
import os
import time


class Website_page(Driverinstance):
    def __init__(self, cap, login=False):
        super().__init__(cap)
        self.token = None
        self.steam_key = None
        if login:
            browser = cap[2]
            cur_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            cookies = read_json(os.path.join(cur_dir, "Utils", "tokens.json"))[browser]
            self.steam_key = read_json(os.path.join(cur_dir, "Utils", "steam_key.json"))['Key']
            self.driver.get("https://store.steampowered.com/")
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.token = self.get_access_token()
            if self.token is None:
                self.quit()
                raise Exception("Filed to get token")
    def get_access_token(self):
        # Open a new tab
        self.driver.execute_script("window.open('about:blank', '_blank');")
        # Switch to the newly opened tab
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # Navigate to a webpage (replace URL with your desired webpage)
        self.driver.get("https://store.steampowered.com/pointssummary/ajaxgetasyncconfig")
        # Extract text from the body of the new tab
        body_text = json.loads(self.driver.find_element(By.TAG_NAME, "body").text)
        try:
            token = body_text['data']['webapi_token']
        except:
            token = None
        # Close the new tab
        self.driver.close()
        # Switch back to the original tab
        self.driver.switch_to.window(self.driver.window_handles[0])
        return token

    def get_token(self):
        return self.token

    def get_steam_key(self):
        return self.steam_key

