from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Dropdown():
    def select_dropdown(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://www.orangehrm.com/orangehrm-30-day-trial')
        time.sleep(2)

        countries = driver.find_element(By.ID, 'Form_submitForm_Country')

        all_countries = Select(countries)

        for all_values in all_countries.options:
            print(all_values.text)

        #all_countries.select_by_value('Bangladesh')
       # all_countries.select_by_index(20)
        all_countries.select_by_visible_text("Bangladesh")
        time.sleep(5)

        driver.close()


obj = Dropdown()
obj.select_dropdown()