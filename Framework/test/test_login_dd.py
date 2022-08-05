import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from Framework.pages import login_page
from Framework.utils import excel_utils


class Login_test(unittest.TestCase):

    def test_valid(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/')
        time.sleep(2)

        # excel implement
        file = "E:\\Offline_Batch_07\\Projects\\AutomationBITM07\\Framework\\data\\login_data.xlsx"
        sheet = 'Sheet1'

        number_of_rows = excel_utils.get_row_count(file, sheet)
        print(int(number_of_rows))

        number_of_column = excel_utils.get_column_count(file, sheet)
        print(int(number_of_column))

        data = excel_utils.read_data(file, sheet, 1, 2)
        print(data)

        for r in range(2, number_of_rows + 1):
            username = excel_utils.read_data(file, sheet, r, 1)
            password = excel_utils.read_data(file, sheet, r, 2)

            login_page.LoginPage.login_orange(username, password)

        driver.close()
