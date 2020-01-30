import time

import pytest
from selenium import webdriver

from PageObjects.Login import LoginPage


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running oneTimeSetUp")
    browser = webdriver.Firefox(executable_path='/home/loredana/Documents/geckodriver')
    browser.get('https://enterprise.onna.com/test/user/login')
    time.sleep(5)

    lp = LoginPage(browser)
    lp.login()

    request.cls.driver = browser
    yield browser
    # browser.quit()
