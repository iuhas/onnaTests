import time
from selenium.webdriver.common.keys import Keys


class SearchBarBox:

    def __init__(self, browser):
        self.browser = browser

    def get_search_box(self):
        search_box_input = self.browser.find_element_by_xpath("//div[@id='search-bar-input']")
        return search_box_input

    def input_search_text(self, find_text: str):
        self.get_search_box().send_keys(find_text)
        time.sleep(2)

    def clear_search_box(self):
        self.get_search_box().send_keys(Keys.CLEAR)
        time.sleep(1)