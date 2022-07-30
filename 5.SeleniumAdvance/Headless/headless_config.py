from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class Headless():
    def chrome_headless(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.headless = True
        driver = webdriver.Chrome(ChromeDriverManager().install(), options = chrome_options)

        driver.get("https://google.com")
        print("Title on Headless Chrome: " + driver.title)

        driver.close()


    def firefox_headless(self):
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.headless = True
        driver = webdriver.Firefox(GeckoDriverManager().install(), options= firefox_options)

        driver.get('https://apple.com')
        print("Title on Headless Firefox: " + driver.title)

        driver.close()


obj = Headless()
#obj.chrome_headless()
obj.firefox_headless()