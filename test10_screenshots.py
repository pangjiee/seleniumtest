from datetime import datetime
import time

from selenium import webdriver
from time import sleep

# google
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

url = 'https://www.google.com/'
google_search_bar = 'APjFqb'
search_key_word = 'selenium'
first_search_result_id = 'jZ2SBf'


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def test1(self):
        driver = self.driver
        wait = WebDriverWait(driver, 2)
        wait.until(expected_conditions.title_is('Google'))
        driver.find_element(By.ID, google_search_bar).send_keys(search_key_word)
        sleep(1)
        driver.find_element(By.ID, first_search_result_id).click()
        sleep(2)
        current_time = datetime.now()
        # Convert the time to a string
        epoch_time = int(time.time())
        test_name = self.__class__.__name__ + "." + self.__class__.test1.__name__
        driver.save_screenshot(str(epoch_time) + '_' + test_name + '.png')
        driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test1()
