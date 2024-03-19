from Logic.Website.Website_page import Website_page
from selenium.webdriver.common.keys import Keys


class Home_page(Website_page):
    PAGE_URL = "https://store.steampowered.com/"
    SEARCH_INPUT = "//input[@id='store_nav_search_term']"

    SEARCH_SUG = "//div[@id='search_suggestion_contents']//a//div[@class='match_name ']"

    #AFTER SEARCH
    SEARCH_RESULT = "//div[@class='page_header_ctn search ']//div[@class='page_content']//div[@class='termcontainer']//div[@class='searchtag tag_dynamic']"

    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_url(self.PAGE_URL)

    def write_in_search_input(self, txt,press_return = True):
        self.Find_and_send_input_to_element(self.SEARCH_INPUT, txt)
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

