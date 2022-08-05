import time
from selenium.webdriver.common.by import By


class LoginPage():

    def __int__(self, driver):
        self.driver = driver

    def login_orange(self, username, password):

        username_field = self.driver.find_element(By.ID, 'txtUsername')
        password_field = self.driver.find_element(By.ID, 'txtPassword')
        login_btn = self.driver.find_element(By.ID, 'btnLogin')

        username_field.clear()
        username_field.send_keys(username)

        password_field.clear()
        password_field.send_keys(password)

        login_btn.click()
