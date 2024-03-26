import os
import random
import time


from selenium.webdriver.common.by import By

from Logic.Website.Website_Page import Website_page
from selenium.webdriver.common.keys import Keys

from Utils.Utils import read_json


class Search_page(Website_page):

    SEARCH_INPUT = "//input[@id='store_nav_search_term']"
    SEARCH_SUG = "//div[@id='search_suggestion_contents']//a//div[@class='match_name ']"

    #AFTER SEARCH
    APP_ELEM = "//div[@id='search_resultsRows']//a"
    APP_NAME = ".//div[@class='responsive_search_name_combined']//div[@class='col search_name ellipsis']"
    GAME_PRICE = ".//div[@class='responsive_search_name_combined']//div[@class='col search_price_discount_combined responsive_secondrow']/div/div/div"

    FIND_GAME_BY_NAME = "(//span[normalize-space()='GAME_NAME'])"
    FIND_BY_ID = "//a[@data-ds-appid='APP_ID']"


    SORT_BUTTONS = "//div[@id='sort_by_dselect_container']"
    SORT_BY_NAME = "//a[@id='Name_ASC']"
    SORT_BY_Relevance = "//a[@id='_ASC']"
    SORT_BY_RELEASE_DATE = "//a[@id='Released_DESC']"
    SORT_BY_LOWEST_PRICE = "//a[@id='Price_ASC']"
    SORT_BY_HIGH_PRICE = "//a[@id='Price_DESC']"
    SORT_BY_USER_REVIEW = "//a[@id='Reviews_DESC']"

    OWNED_GAME_ELEM = "//div[@class='ds_flag ds_owned_flag']"

    PRICE_SLIDER = "//input[@id='price_range']"

    #"Narrow by OS"
    WINOWS_GAMES = "//span[@data-value='win']"
    MAC_GAMES =  "//span[contains(text(),'macOS')]"
    LINUX_GAMES = "//span[contains(text(),'SteamOS + Linux')]"

    #Narrow by preferences
    HIDE_FREE_GAMES = "//span[@class='tab_filter_control tab_filter_control_include']"
    HIDE_OWNED_GAMES = "//span[@data-value='hide_owned']"
    HIDE_WISHLIST_GAMES = "//span[@data-value='hide_wishlist']"



    def __init__(self, cap, login = False):
        super().__init__(cap, login)
        self.PAGE_URL = self.Website_URLS['Search_page']
        self.go_to_url(self.PAGE_URL)

    def hide_free_to_play_games(self):
        self.wait_and_get_element_by_xpath(self.HIDE_FREE_GAMES).click()
        time.sleep(1)

    def hide_owned_games(self):
        self.click_on_elem(self.wait_and_get_element_by_xpath(self.HIDE_OWNED_GAMES))
        time.sleep(1)

    def hide_wishlist_games(self):
        self.click_on_elem(self.wait_and_get_element_by_xpath(self.HIDE_WISHLIST_GAMES))
        time.sleep(1)

    def get_random_game(self):
        elems = self.wait_and_get_elements_by_xpath(self.APP_ELEM)
        random_game = random.choice(elems)
        game_name = random_game.find_element(By.XPATH, self.APP_NAME).text
        game_id = random_game.get_attribute("data-ds-appid")
        return game_name,int(game_id)

    def check_if_game_in_page(self,game_name):
        try:
            return self.wait_and_get_element_by_xpath(self.FIND_BY_ID.replace("APP_ID", game_name)).is_displayed()
        except:
            return False


    def move_price_slider(self,lim):
        price_slider = self.wait_and_get_element_by_xpath(self.PRICE_SLIDER)
        self.move_by_offset(price_slider,lim)
        time.sleep(1)

    def get_games_prices(self):
        price_list = []
        elems = self.wait_and_get_elements_by_xpath(self.APP_ELEM)
        for game in elems:
                game_name = game.find_element(By.XPATH, self.APP_NAME).text
                try:
                    game_price = game.find_element(By.XPATH, self.GAME_PRICE).text
                except:
                    game_price = ""
                price_list.append([game_name,game_price])

        return price_list

