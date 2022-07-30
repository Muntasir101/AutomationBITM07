from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

class BasicAuth_demo():
    def auth_config(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        time.sleep(2)

        # protocol://username:password@url
        driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

        message = driver.find_element(By.XPATH, '//*[@id="content"]/div/p').text
        print(message)

        driver.close()


obj = BasicAuth_demo()
obj.auth_config()