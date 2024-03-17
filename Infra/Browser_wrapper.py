from selenium import webdriver
from Logic.Utils import *

class BrowserWrapper:
    def __init__(self,config_ = None):
        if config_ == None:
            return
        browser_configs = config_['browser_config']
        test_config = config_['test_config']
        self.test_type = test_config["test_type"] # serial/parallel
        self.test_HUB = test_config["HUB"]
        caps_list = []
        for browser in browser_configs:
            tmp_cap = self.get_browser_cap(browser)
            caps_list.append(tmp_cap)
        self.caps_list = caps_list

    def get_browser_cap(self,browser):
        options = None
        browser_webdriver = None
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            browser_webdriver = webdriver.Chrome
        elif browser == "edge":
            options = webdriver.EdgeOptions()
            browser_webdriver = webdriver.Edge
        # Adding argument to disable the AutomationControlled flag
        #options.add_argument("--disable-blink-features=AutomationControlled")
        # Exclude the collection of enable-automation switches
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--headless")
        options.add_argument("window-size=1920,1080")
        #options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # Turn-off userAutomationExtension
        #options.add_experimental_option("useAutomationExtension", False)
        #options.add_argument("--start-maximized")
        browser_webdriver_args = {'options' : options}
        if self.test_type == "parallel":
            #options.capabilities["platformName"] = "Windows 11"
            browser_webdriver = webdriver.Remote
            browser_webdriver_args = {'options' : options, 'command_executor': self.test_HUB}
        return browser_webdriver, browser_webdriver_args, browser

    def get_default_browser_cap(self):
        options = webdriver.ChromeOptions()
        browser_webdriver = webdriver.Chrome
        #options.add_argument("--disable-blink-features=AutomationControlled")
        #options.add_argument("--no-sandbox")
        #options.add_argument("--disable-dev-shm-usage")
        #options.add_argument("--headless")
        options.add_argument("window-size=1920,1080")
        # Exclude the collection of enable-automation switches
        #options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # Turn-off userAutomationExtension
        #options.add_experimental_option("useAutomationExtension", False)
        browser_webdriver_args = {'options': options}
        return browser_webdriver, browser_webdriver_args

    def get_caps(self):
        return self.caps_list