from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


class Alert():
    def all_type_alert(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://the-internet.herokuapp.com/javascript_alerts')
        time.sleep(2)

        normal_alert = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button')
        normal_alert.click()

        driver.switch_to.alert.accept()

        confirm_alert = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')
        confirm_alert.click()
        driver.switch_to.alert.dismiss()
        time.sleep(5)

        prompt_alert = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button')
        prompt_alert.click()
        driver.switch_to.alert.send_keys('Test Automation By Selenium')
        driver.switch_to.alert.accept()
        time.sleep(5)

        driver.close()


obj = Alert()
obj.all_type_alert()
