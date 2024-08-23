from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3)


def name_forms(driver):
    input_text = 'Amirchik'
    driver.get('https://practice-automation.com/form-fields/')
    name_string = driver.find_element(By.ID, 'name')
    name_string.send_keys(input_text)

