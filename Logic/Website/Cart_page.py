import os
import time

from Logic.Website.Website_Page import Website_page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Utils.Utils import read_json


class Cart_page(Website_page):

    CART_ITEMS = "//div//div//div//div//div//div//div[@class='Panel Focusable']"
    REMOVE_BUTTON = "//*[contains(text(),'Remove')]"
    REMOVE_ALL_ITEMS = "//div[contains(text(),'Remove all items')]"
    TITLE = "//div[@class='pVXX8Pzc4JbT40TP4RwRG']"
    EMPTY_CART = "//div[normalize-space()='Your cart is empty.']"

    def __init__(self, cap, login = False):
        super().__init__(cap, login)
        self.PAGE_URL = self.Website_URLS['Cart_page']
        self.go_to_url(self.PAGE_URL)


    def get_items_in_carts_names(self):
        names=[]
        items_elems = self.wait_and_get_elements_by_xpath(self.CART_ITEMS,sec=5)
        for elem in items_elems:
            names.append(elem.find_element(By.XPATH,self.TITLE).text)
        return names

    def remove_all_items_from_cart(self):
        try:
            elem = self.wait_and_get_element_by_xpath(self.REMOVE_ALL_ITEMS,sec=5)
            self.click_on_elem(elem)
            time.sleep(3) # wait fo items to be removed
        except:
            #no items in cart
            return

    def remove_item_from_cart(self,elem):
        remove_button = elem.find_element(By.XPATH,self.REMOVE_BUTTON,sec=5)
        remove_button.click()

    def check_if_cart_is_empty(self):
        try:
            self.wait_and_get_element_by_xpath(self.EMPTY_CART,sec=5)
            return True
        except:
            return False