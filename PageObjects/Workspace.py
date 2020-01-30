import time
from selenium.webdriver import ActionChains


class WorkspacePage:

    def __init__(self, browser):
        self.browser = browser

    def goTo_workspace(self):
        workspace = self.browser.find_element_by_xpath("//table/tbody/tr/th/div/onna-ellipsis/span")
        ActionChains(self.browser).move_to_element(workspace).click(workspace).perform()

    def goTo__connected_source_byName(self, source_name):
        time.sleep(8)
        gmail2 = self.browser.find_element_by_xpath("//span[@class='o-ellipsis-text'][contains(text(),'"+source_name+"')]")
        gmail2.click()