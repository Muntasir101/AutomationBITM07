import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Chrome():

    def chrome_config(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://google.com")
        time.sleep(4)
        driver.close()


obj = Chrome()
obj.chrome_config()
