from selenium import webdriver


class Launch_chrome():
    def run_chrome(self):
        driver = webdriver.Chrome(
            executable_path="E:\Offline_Batch_07\Projects\AutomationBITM07\Drivers\chromedriver.exe")

        driver.maximize_window()

        driver.get("https://google.com")
        driver.get('https://apple.com')


test_obj = Launch_chrome()
test_obj.run_chrome()
