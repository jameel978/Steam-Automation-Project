import json
import time
from selenium import webdriver
import os

def save_cookies(cookies,filename):
    with open(filename, 'a') as f:
        json.dump(cookies, f)

def main():
    browsers = ['chrome', 'edge', 'firefox']
    dict_ = {}
    for browser in browsers:
        if browser == 'chrome':
            driver = webdriver.Chrome()
        elif browser == 'edge':
            driver = webdriver.Edge()
        else:
            driver = webdriver.Firefox()
        try:
            driver.get('https://store.steampowered.com/')  # Change the URL to your login page

            input(f"Please log in to {browser}, then press Enter in the terminal...")
            dict_[browser] = driver.get_cookies()

            print(f"Cookies for {browser} saved successfully.")
        except Exception as e:
            print(f"An error occurred with {browser}: {str(e)}")
        finally:
            driver.quit()
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    config = os.path.join(cur_dir, "tokens.json")
    save_cookies(dict_,config)

if __name__ == "__main__":
    main()
