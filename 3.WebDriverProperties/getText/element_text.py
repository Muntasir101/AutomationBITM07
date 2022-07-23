# get element visible text

from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class GetText():

    def text(self):
        driver = webdriver.Firefox(
            executable_path="E:\Offline_Batch_07\Projects\AutomationBITM07\Drivers\geckodriver.exe")

        driver.get('https://opensource-demo.orangehrmlive.com/')
        time.sleep(2)

        login_panel = driver.find_element(By.ID, 'logInPanelHeading')
        login_panel_text = login_panel.text
        print(login_panel_text)

        username_password = driver.find_element(By.CSS_SELECTOR, '#content > div:nth-child(3) > span')
        username_password_text = username_password.text
        print(username_password_text)

        driver.close()


obj = GetText()
obj.text()
