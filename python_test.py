import uuid

import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_something():
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get('http://151.80.70.42:3000/')
    driver.maximize_window()
    users_before = driver.find_elements(By.CSS_SELECTOR, 'ul#user-list li[data-id]')
    driver.find_element(By.CSS_SELECTOR, 'i.mdi-content-add').click()
    driver.find_element(By.CSS_SELECTOR, 'div.main-content #icon_prefix').clear()
    driver.find_element(By.CSS_SELECTOR, 'div.main-content #icon_prefix').send_keys('Vasya')
    driver.find_element(By.CSS_SELECTOR, 'div.main-content #icon_telephone').clear()
    driver.find_element(By.CSS_SELECTOR, 'div.main-content #icon_telephone').send_keys('123456')
    driver.find_element(By.CSS_SELECTOR, 'div.main-content a.save-btn').click()
    time.sleep(2)
    users_after = driver.find_elements(By.CSS_SELECTOR, 'ul#user-list li[data-id]')
    assert len(users_after) == len(users_before) + 1


def test_api_create_user():
    username = uuid.uuid4()
    userphone = int(time.time())
    response = requests.get('http://151.80.70.42:3000/api/users')
    print(response.status_code)
    print(response.content)

