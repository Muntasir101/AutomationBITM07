from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

class FileUpload():
    def uplaod_file(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://the-internet.herokuapp.com/upload')
        driver.maximize_window()
        time.sleep(2)

        try:
            choose_file_btn = driver.find_element(By.ID, 'file-upload')
            choose_file_btn.send_keys("E:\\Offline_Batch_07\\Projects\\AutomationBITM07\\requirements.txt")

            submit = driver.find_element(By.ID, 'file-submit')
            submit.click()
            time.sleep(5)

            success_message = driver.find_element(By.XPATH, '//*[@id="content"]/div/h3').text
            print(success_message)

        except:
            print("File uploading error")

        driver.close()


obj = FileUpload()
obj.uplaod_file()
