from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from utils import click_element

url = 'https://www.google.com/'
google_search_bar = 'APjFqb'
search_key_word = 'selenium'
first_search_result_id = 'jZ2SBf'


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def test_implicity_sleep(self):
        driver = self.driver
        driver.implicitly_wait(10)  # wait in background
        driver.find_element(By.ID, google_search_bar).send_keys(search_key_word)
        sleep(1)
        driver.find_element(By.ID, first_search_result_id).click()
        sleep(5)
        driver.quit()

    def test_wait(self):
        wait = WebDriverWait(self.driver, 2)  # wait for web driver to load
        wait.until(EC.title_is('Google'))
        self.driver.find_element(By.ID, google_search_bar).send_keys(search_key_word)
        sleep(1)
        self.driver.find_element(By.ID, first_search_result_id).click()
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test_wait()

# accept/ dismiss, text, send_keys
