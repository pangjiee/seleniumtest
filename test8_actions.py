from selenium import webdriver
from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from utils import click_element

# sahi test
url = 'https://sahitest.com/demo/clicks.htm'
text_area = 't2'
dbl_click_btn = '/html/body/form/input[2]'
single_click_btn = '/html/body/form/input[3]'
right_click_btn = '/html/body/form/div[2]'
clear_btn = '/html/body/form/input[1]'

# google
url_2 = 'https://www.google.com/'
google_search_bar = 'APjFqb'
search_key_word = 'selenium'
first_search_result_id = 'jZ2SBf'


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def test_mouse(self):
        driver = self.driver
        wait = WebDriverWait(self.driver, 2)  # wait for web driver to load
        wait.until(EC.title_is('Clicks'))
        actions = ActionChains(driver)

        # double click
        dbl_click_ele = driver.find_element(By.XPATH, dbl_click_btn)
        actions.double_click(dbl_click_ele).perform()
        wait.until(EC.text_to_be_present_in_element_value((By.NAME, text_area), '[DOUBLE_CLICK]'))
        text = driver.find_element(By.NAME, text_area).get_attribute('value')
        if text != '[DOUBLE_CLICK]':
            raise NoSuchElementException("Element not found on the page")
        else:
            print('Correct action 1')
        driver.find_element(By.XPATH, clear_btn).click()
        wait.until(EC.text_to_be_present_in_element((By.NAME, text_area), ""))

        # single click
        single_click_ele = driver.find_element(By.XPATH, single_click_btn)
        actions.click(single_click_ele).perform()
        wait.until(EC.text_to_be_present_in_element_value((By.NAME, text_area), '[CLICK]'))
        text = driver.find_element(By.NAME, text_area).get_attribute('value')
        if text != '[CLICK]':
            raise NoSuchElementException("Element not found on the page")
        else:
            print('Correct action 2')
        driver.find_element(By.XPATH, clear_btn).click()

        # right click
        right_click_ele = driver.find_element(By.XPATH, right_click_btn)
        actions.move_to_element(right_click_ele).perform()
        sleep(2)
        actions.context_click(right_click_ele).perform()
        actions.click(right_click_ele).perform()
        wait.until(EC.text_to_be_present_in_element_value((By.NAME, text_area), '[RIGHT_CLICK]'))
        text = driver.find_element(By.NAME, text_area).get_attribute('value')
        if text != '[RIGHT_CLICK]':
            raise NoSuchElementException("Element not found on the page")
        else:
            print('Correct action 3')

        sleep(5)
        driver.quit()

    def test_keys(self):
        driver = self.driver
        wait = WebDriverWait(self.driver, 2)  # wait for web driver to load
        wait.until(EC.title_is('Google'))
        search_text = driver.find_element(By.ID, google_search_bar)
        search_text.send_keys('testing')
        actions = ActionChains(driver)
        search_text.send_keys(Keys.COMMAND, 'a')
        search_text.send_keys(Keys.COMMAND, 'x')
        driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test_mouse()

# accept/ dismiss, text, send_keys
