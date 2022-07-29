from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

class Screenshot_demo():
    def capture(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://google.com')
        time.sleep(2)

        # Capture Screenshot
        driver.get_screenshot_as_file('E:\Offline_Batch_07\Projects\AutomationBITM07\Bugs_Screenshots\Google.png')

        driver.close()


obj = Screenshot_demo()
obj.capture()