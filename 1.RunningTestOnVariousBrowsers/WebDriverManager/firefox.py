import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class Firefox():

    def firefox_config(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get("https://google.com")
        time.sleep(4)
        driver.close()


obj = Firefox()
obj.firefox_config()