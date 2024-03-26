
from selenium import webdriver
import os
from Utils.Utils import read_json



class BrowserWrapper:
    def __init__(self):
        cur_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_loca = os.path.join(cur_dir,'Tests/Steam_website/Configs/', "UI_Tests_Config.json")
        test_config = read_json(config_loca)
        self.test_type = test_config["test_type"] # serial/parallel
        self.test_HUB = test_config["HUB"]

    def get_browser(self,browser):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            #browser_webdriver = webdriver.Chrome
        elif browser == "edge":
            options = webdriver.EdgeOptions()
            #browser_webdriver = webdriver.Edge
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            #browser_webdriver = webdriver.Firefox
        else:
            return self.get_debug_driver()
        # Exclude the collection of enable-automation switches
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--headless")
        options.add_argument("window-size=1920,1080")
        browser_webdriver_args = {'options' : options}
        #if self.test_type == "parallel":
        #options.capabilities["platformName"] = "Windows 11"
        browser_webdriver = webdriver.Remote
        browser_webdriver_args = {'options' : options, 'command_executor': self.test_HUB}
        return browser_webdriver,browser_webdriver_args,browser


    def get_debug_driver(self):
            options = webdriver.ChromeOptions()
            browser_webdriver = webdriver.Chrome
            #options.add_argument("window-size=1920,1080")
            options.add_argument("--start-maximized")
            browser_webdriver_args = {'options': options}
            return browser_webdriver,browser_webdriver_args,'chrome'


