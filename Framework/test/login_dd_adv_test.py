import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from Framework.pages.login_page import LoginPage
from Framework.utils import excel_utils


class LoginTest(unittest.TestCase):

    def test_login(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)

        # Excel implementation
        file = 'E:\Offline_Batch_07\Projects\AutomationBITM07\Framework\data\login_data.xlsx'
        sheet = 'Sheet1'

        number_of_rows = excel_utils.get_row_count(file, sheet)

        for r in range(2, number_of_rows + 1):
            username = excel_utils.read_data(file, sheet, r, 1)
            password = excel_utils.read_data(file, sheet, r, 2)

            lp = LoginPage(driver)
            lp.login_orange(username, password)

            if driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList':
                excel_utils.write_data(file, sheet, r, 4, "Login Successfully")
            else:
                excel_utils.write_data(file, sheet, r, 4, "Not Login")

        driver.close()
