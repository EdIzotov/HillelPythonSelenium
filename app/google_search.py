from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class GoogleSearch:
    @staticmethod
    def get(query):
        driver = webdriver.Chrome('./chromedriver.exe')
        driver.get('http://google.com')
        driver.maximize_window()
        driver.find_element(By.CSS_SELECTOR, 'button#L2AGLb').click()
        driver.find_element(By.CSS_SELECTOR, "input[name = 'q']").send_keys(query)
        driver.find_element(By.CSS_SELECTOR, "input[name = 'q']").send_keys(Keys.ENTER)
        search_result = driver.find_elements(By.CSS_SELECTOR, 'div#search div[data-sokoban-container]')
        return search_result
