from Infra.Driver_instance import Driverinstance
import os
from Utils.Utils import read_json


class Website_page(Driverinstance):

    LOGIN_BUTTON = "//a[normalize-space()='login']"
    def __init__(self, cap, login=False):
        super().__init__(cap)
        self.token = None
        if login:
            browser = cap[2]
            cur_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            cookies = read_json(os.path.join(cur_dir, "Utils", "tokens.json"))[browser]
            cur_dir = os.path.dirname(os.path.abspath(__file__))
            self.Website_URLS = read_json(os.path.join(cur_dir, "Configs", "Website_URLS.json"))
            self.driver.get(self.Website_URLS['Home_page'])
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.refresh_page()
            try:
                self.wait_and_get_element_by_xpath(self.LOGIN_BUTTON)
                login = False
            except:
                login = True
            if not login:
                self.quit()
                raise Exception("Login cookies expired")
