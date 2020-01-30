import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class SourceData:

    def __init__(self, browser):
        self.browser = browser

    def input_text_in_search_box(self, text_to_find):
        search_box_input = self.browser.find_element_by_xpath("//div[@id='search-bar-input']")
        search_box_input.send_keys(text_to_find)  # "file00"
        search_box_input.send_keys(Keys.ENTER)
        time.sleep(4)
        results = self.browser.find_elements_by_class_name("o-list-results-item-container")
        return len(results)

    def click_on_share_option_by_item_index(self, chosen_index:str):
        result_file_option_button = self.browser.find_element_by_xpath(
            "//onna-result-li[1]//li[1]//div[1]//div[1]//div[2]//div[1]//pa-button["+ chosen_index+"]") # 1
        result_file_option_button.click()
        time.sleep(4)
        options = self.browser.find_element_by_partial_link_text("Share")
        options.click()  # clicked on share

    def fill_in_share_form(self, user_email: str, permission_index: str):
        # wait for screen to appear
        try:
            WebDriverWait(self.browser, 6).until(EC.presence_of_element_located((By.XPATH,
                                                                    "//header[contains(@class,'o-dialog-header')]")))
        except TimeoutException:
            print("Loading took too much time!")

        no_yes = self.browser.find_element_by_id("field-toggle-0")
        no_yes.click()
        insert_email = self.browser.find_element_by_xpath("//input[contains(@placeholder,'Add people…')]")
        insert_email.send_keys(user_email)
        time.sleep(2)

        expand_select = self.browser.find_element_by_name("down-key")
        expand_select.click()
        self.browser.find_element_by_xpath(
            "//onna-suggestion-dropdown/div/div/section/ul/onna-dropdown-item["+permission_index+"]/li/a/span/div").click()
        time.sleep(2)
        click_share_button = self.browser.find_element_by_xpath("//ng-component//pa-button[2]")
        click_share_button.click()

    def is_toast_message_displayed(self):
        # wait for screen to appear
        try:
            WebDriverWait(self.browser, 6).until(EC.presence_of_element_located((By.CLASS_NAME, "onna-toasts-container")))
            return True
        except TimeoutException:
            print("Loading took too much time!")
            return False



