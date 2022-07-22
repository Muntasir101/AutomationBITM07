from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class Launch_firefox():
    def run_firefox(self):
        driver = webdriver.Firefox(
            executable_path="E:\Offline_Batch_07\Projects\AutomationBITM07\Drivers\geckodriver.exe")

        driver.get('http://localhost/orangehrm/web/index.php/auth/login')
        time.sleep(2)

        username = driver.find_element(By.NAME, 'username')
        password = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        loginBtn = driver.find_element(By.CSS_SELECTOR, '#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.oxd-form-actions.orangehrm-login-action > button')

        username.send_keys("Admin")
        password.send_keys('Admin@123')
        loginBtn.click()

        time.sleep(3)

        driver.close()


test_obj = Launch_firefox()
test_obj.run_firefox()