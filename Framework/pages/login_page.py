import time

from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def login_orange(self, username, password):
        username_field = self.driver.find_element(By.NAME, "username")
        password_field = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

        username_field.clear()
        username_field.send_keys(username)
        time.sleep(2)

        password_field.clear()
        password_field.send_keys(password)
        time.sleep(2)

        login_button.click()
