import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from Framework.pages.login_page import LoginPage


class LoginTest(unittest.TestCase):

    @pytest.mark.skip
    def test_valid_login(self):
        baseURL = "https://opensource-demo.orangehrmlive.com/"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(3)

        lp = LoginPage(driver)
        lp.login_orange("Admin", "admin123")

        driver.close()

    def test_Invalid_login(self):
        baseURL = "https://opensource-demo.orangehrmlive.com/"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(3)

        lp = LoginPage(driver)
        lp.login_orange("Admin213123", "admin123232")

        driver.close()
