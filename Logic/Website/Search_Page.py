from Logic.Website.Website_page import Website_page
from selenium.webdriver.common.keys import Keys


class Search_page(Website_page):
    PAGE_URL = "https://store.steampowered.com/"
    SEARCH_INPUT = "//input[@id='store_nav_search_term']"

    SEARCH_SUG = "//div[@id='search_suggestion_contents']//a//div[@class='match_name ']"

    #AFTER SEARCH
    SEARCH_RESULT = "//div[@class='page_header_ctn search ']//div[@class='page_content']//div[@class='termcontainer']//div[@class='searchtag tag_dynamic']"


    SORT_BUTTONS = "//div[@id='sort_by_dselect_container']"
    SORT_BY_NAME = "//a[@id='Name_ASC']"
    SORT_BY_Relevance = "//a[@id='_ASC']"
    SORT_BY_RELEASE_DATE = "//a[@id='Released_DESC']"
    SORT_BY_LOWEST_PRICE = "//a[@id='Price_ASC']"
    SORT_BY_HIGH_PRICE = "//a[@id='Price_DESC']"
    SORT_BY_USER_REVIEW = "//a[@id='Reviews_DESC']"



    #"Narrow by OS"
    WINOWS_GAMES = "//span[@data-value='win']"
    MAC_GAMES =  "//span[contains(text(),'macOS')]"
    LINUX_GAMES = "//span[contains(text(),'SteamOS + Linux')]"

    #Narrow by preferences
    HIDE_FREE_GAMES = "//span[contains(text(),'Hide free to play items')]"
    HIDE_OWNED_GAMES = "//span[@data-value='hide_owned']"
    HIDE_WISHLIST_GAMES = "//span[@data-value='hide_wishlist']"


    #Hover Elements
    HOVER_TITLE = "//h4[@class='hover_title']"
    HOVER_RELEASE = "//div[@class='hover_release']"
    HOVER_REVIEW = "//div[@class='hover_review_summary']"
    HOVER_TAGS = "//div[@class='hover_tag_row']//div"

    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_url(self.PAGE_URL)


