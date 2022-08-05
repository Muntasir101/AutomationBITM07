import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

@pytest.yield_fixture()
def browser_config():
    global driver

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get('https://opensource-demo.orangehrmlive.com/')
    time.sleep(2)

    yield
    driver.close()

@pytest.mark.order(2)
@pytest.mark.valid
def test_login_001_valid(browser_config):
    username = driver.find_element(By.ID, 'txtUsername')
    password = driver.find_element(By.ID, 'txtPassword')
    login_btn = driver.find_element(By.ID, 'btnLogin')

    username.send_keys("Admin")
    password.send_keys('admin123')
    login_btn.click()

@pytest.mark.order(1)
@pytest.mark.invalid
def test_login_002_invalid(browser_config):
    username = driver.find_element(By.ID, 'txtUsername')
    password = driver.find_element(By.ID, 'txtPassword')
    login_btn = driver.find_element(By.ID, 'btnLogin')

    username.send_keys("Admi324214n")
    password.send_keys('admin123')
    login_btn.click()

@pytest.mark.order(3)
@pytest.mark.skip('System unstable')
@pytest.mark.invalid
def test_login_003_invalid(browser_config):
    username = driver.find_element(By.ID, 'txtUsername')
    password = driver.find_element(By.ID, 'txtPassword')
    login_btn = driver.find_element(By.ID, 'btnLogin')

    username.send_keys("")
    password.send_keys('')
    login_btn.click()

@pytest.mark.order(4)
@pytest.mark.invalid
def test_login_004_invalid(browser_config):
    username = driver.find_element(By.ID, 'txtUsername')
    password = driver.find_element(By.ID, 'txtPassword')
    login_btn = driver.find_element(By.ID, 'btnLogin')

    username.send_keys("")
    password.send_keys('')
    login_btn.click()

def test_home_001_valid(browser_config):
    username = driver.find_element(By.ID, 'txtUsername')
    password = driver.find_element(By.ID, 'txtPassword')
    login_btn = driver.find_element(By.ID, 'btnLogin')

    username.send_keys("Admin")
    password.send_keys('admin123')
    login_btn.click()