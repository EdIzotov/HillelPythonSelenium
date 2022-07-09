from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
    time.sleep(5)
    users_after = driver.find_elements(By.CSS_SELECTOR, 'ul#user-list li[data-id]')
    assert len(users_after) == len(users_before) + 1
    time.sleep(5)
