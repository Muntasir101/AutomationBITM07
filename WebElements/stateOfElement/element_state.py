from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


class State():

    def elements_state(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://opensource-demo.orangehrmlive.com/')
        time.sleep(2)

        loginBtn = driver.find_element(By.NAME, 'Submit')
        loginBtn_state = loginBtn.is_displayed()
        loginBtn_state_en = loginBtn.is_enabled()
        print(loginBtn_state)
        print(loginBtn_state_en)

        driver.close()


obj = State()
obj.elements_state()
