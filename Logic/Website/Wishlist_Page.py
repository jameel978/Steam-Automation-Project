import time

from Logic.Website.Website_Page import Website_page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Wishlist_Page(Website_page):

    WISHLIST_GAMES = "//div[@class='wishlist_row']"
    WISHLIST_GAME_NAME = "//div[@class='content']//a[@class='title']"
    REMOVE_GAME_FROM_WISHLIST = "//div[@class='delete']"
    CONFIRM_GAME_REMOVE = "//span[normalize-space()='OK']"

    def __init__(self, cap, login):
        super().__init__(cap, login)
        self.PAGE_URL = self.Website_URLS['Wishlist_Page']
        self.go_to_url(self.PAGE_URL)

    def get_wishlist_games_count(self):
        try:
            items_elems = self.wait_and_get_elements_by_xpath(self.WISHLIST_GAMES)
            return len(items_elems)
        except:
            return 0

    def get_wishlist_games_names(self):
        names = []
        try:
            items_elems = self.wait_and_get_elements_by_xpath(self.WISHLIST_GAMES,sec=1)
            for elem in items_elems:
                names.append(elem.find_element(By.XPATH, self.WISHLIST_GAME_NAME).text)
        except:
            pass
        return names

    def remove_games_from_wish_list(self):
        for i in range(self.get_wishlist_games_count()):
            self.wait_and_get_element_by_xpath(self.REMOVE_GAME_FROM_WISHLIST).click()
            self.wait_and_get_element_by_xpath(self.CONFIRM_GAME_REMOVE).click()
            time.sleep(1)


