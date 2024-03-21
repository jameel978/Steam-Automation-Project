import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils.Utils import *
import os



class Driverinstance:
    def __init__(self,cap):
        driver = cap[0](**cap[1])
        self.driver = driver
        #self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    def print_html_page(self):
        # Get the page source (HTML)
        html = self.driver.page_source
        # Print the HTML
        print(html)
        self.driver.save_screenshot('test.png')
    def get_page_title(self):
        return self.driver.title

    def refresh_page(self):
        self.driver.refresh()

    def close_page(self):
        self.driver.close()

    def get_element_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def wait_and_get_element_by_xpath(self, xpath, sec=2):
        return WebDriverWait(self.driver, sec).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def wait_and_get_elements_by_xpath(self, xpath, sec=2):
        return WebDriverWait(self.driver, sec).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    def Find_and_click_on_element(self, element, click_using_javescript=False):
        if click_using_javescript:
            self.driver.execute_script("arguments[0].click();", self.wait_and_get_element_by_xpath(element))
        else:
            self.get_element_by_xpath(element).click()
        # self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, element))).click()

    def Find_and_send_input_to_element(self, element, txt , delay = None):
        if delay:
            elem = self.wait_and_get_element_by_xpath(element)
            for i in txt:
                elem.send_keys(i)
                time.sleep(delay)
        else:
            self.wait_and_get_element_by_xpath(element).send_keys(txt)

    def is_element_found(self, elem, sec):
        try:
            self.wait_and_get_element_by_xpath(elem, sec=sec)
            return True
        except:
            return False

    def click_on_elem(self, elem):
        #self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        self.driver.execute_script("arguments[0].click();", elem)

    def quit(self):
        self.driver.quit()

    def go_to_url(self,url):
        self.driver.get(url)

    def get_cockies(self):
        return self.driver.get_cookies()