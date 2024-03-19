from Logic.Website.Website_page import Website_page
from selenium.webdriver.common.keys import Keys


class Search_page(Website_page):
    PAGE_URL = "https://store.steampowered.com/"
    SEARCH_INPUT = "//input[@id='store_nav_search_term']"

    SEARCH_SUG = "//div[@id='search_suggestion_contents']//a//div[@class='match_name ']"

    #AFTER SEARCH
    SEARCH_RESULT = "//div[@class='page_header_ctn search ']//div[@class='page_content']//div[@class='termcontainer']//div[@class='searchtag tag_dynamic']"

    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_url(self.PAGE_URL)


