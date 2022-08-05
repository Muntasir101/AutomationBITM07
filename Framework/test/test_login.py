import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from Framework.pages.login_page import LoginPage


class Login_test(unittest.TestCase):

    def test_valid(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/')
        time.sleep(2)

        login_page_obj = LoginPage(driver)
        login_page_obj.login_orange('Admin', 'admin123')

        driver.close()
