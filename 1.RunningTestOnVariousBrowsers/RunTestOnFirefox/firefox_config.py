from selenium import webdriver
import time


class Launch_firefox():
    def run_firefox(self):
        driver = webdriver.Firefox(
            executable_path="E:\Offline_Batch_07\Projects\AutomationBITM07\Drivers\geckodriver.exe")

        driver.get('http://localhost/orangehrm/web/index.php/auth/login')
        time.sleep(5)

        driver.close()


test_obj = Launch_firefox()
test_obj.run_firefox()