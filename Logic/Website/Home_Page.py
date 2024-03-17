from Infra.Driver_instance import Driverinstance
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from Logic.Utils import *



class Home_page(Driverinstance):
    PAGE_URL = "https://store.steampowered.com/"
    SEARCH_INPUT = "//input[@id='store_nav_search_term']"

    SEARCH_SUG = "//div[@id='search_suggestion_contents']//a//div[@class='match_name ']"

    #AFTER SEARCH
    SEARCH_RESULT = "//div[@class='page_header_ctn search ']//div[@class='page_content']//div[@class='termcontainer']//div[@class='searchtag tag_dynamic']"

    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_url(self.PAGE_URL)

    def write_in_search_input(self, txt,press_return = True,delay = 0.1):
        self.Find_and_send_input_to_element(self.SEARCH_INPUT, txt,delay)
        #Wait for results to Update
        time.sleep(1)
        if press_return:
            self.Find_and_send_input_to_element(self.SEARCH_INPUT, Keys.RETURN)

    def get_search_results(self):
        try:
            result = self.wait_and_get_element_by_xpath(self.SEARCH_RESULT).text.replace('"',"")
        except:
            result = ""
        return result

    def get_search_suggestions(self):
        elems = self.wait_and_get_elements_by_xpath(self.SEARCH_SUG)
        results = []
        for e in elems:
            results.append(e.text)
        return results

