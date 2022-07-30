from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class DragDrop():
    def dragdrop_demo(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://jqueryui.com/droppable/')
        time.sleep(2)
        driver.maximize_window()

        # Switch to iframe by ID
        driver.switch_to.frame(0)

        source = driver.find_element(By.ID, 'draggable')
        target = driver.find_element(By.ID, 'droppable')

        actions = ActionChains(driver)

        actions.drag_and_drop(source, target).perform()
        time.sleep(5)

        driver.close()


obj = DragDrop()
obj.dragdrop_demo()