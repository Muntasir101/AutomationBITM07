from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class MouseHover():
    def mouse_hover_demo(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://opensource-demo.orangehrmlive.com/')
        time.sleep(2)

        username = driver.find_element(By.ID, 'txtUsername')
        password = driver.find_element(By.ID, 'txtPassword')
        login_btn = driver.find_element(By.ID, 'btnLogin')

        username.send_keys('Admin')
        password.send_keys('admin123')
        login_btn.click()
        time.sleep(5)

        leave_menu = driver.find_element(By.XPATH, '//*[@id="menu_leave_viewLeaveModule"]/b')
        actions = ActionChains(driver)
        actions.move_to_element(leave_menu).perform()
        time.sleep(2)

        my_leave = driver.find_element(By.LINK_TEXT, 'My Leave')
        my_leave.click()
        time.sleep(3)
        print(driver.title)

        driver.close()


obj = MouseHover()
obj.mouse_hover_demo()

