from selenium import webdriver


class Launch_firefox():
    def run_firefox(self):
        driver = webdriver.Firefox(
            executable_path="E:\Offline_Batch_07\Projects\AutomationBITM07\Drivers\geckodriver.exe")


test_obj = Launch_firefox()
test_obj.run_firefox()