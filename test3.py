from time import sleep

from selenium import webdriver

from selenium.webdriver.common.by import By

from utils import send_keyword
from utils import click_element

url = 'https://www.google.com/'


class TestCase(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.get(url)
        sleep(2)

    def test_id(self):
        driver = self.driver
        # driver.find_element(By.ID, 'APjFqb').send_keys('test')
        search_text_field = (By.ID, 'APjFqb')
        search_button = (By.CLASS_NAME, 'lnXdpd')
        first_search_result = (By.CLASS_NAME, 'gNO89b')
        send_keyword(driver, *search_text_field, keyword='test')
        sleep(1)
        # driver.find_element(By.CLASS_NAME, 'lnXdpd').click()
        click_element(driver, *search_button)
        sleep(2)
        driver.find_elements(By.CLASS_NAME, 'gNO89b')[1].click()
        # first search result
        click_element(driver, )
        driver.find_element(By.ID, 'jZ2SBf').click()
        sleep(2)

    def test_name(self):
        driver = self.driver
        driver.find_element(By.NAME, 'q').send_keys('test')
        sleep(1)
        driver.find_element(By.CLASS_NAME, 'lnXdpd').click()
        sleep(1)
        driver.find_elements(By.CLASS_NAME, 'gNO89b')[1].click()
        sleep(2)

    def test_link_test(self):
        self.test_name()
        self.driver.find_element(By.LINK_TEXT, 'Images').click()
        sleep(3)

    def test_partial_link_test(self):
        self.test_name()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Shop').click()
        sleep(3)

    def test_xpath(self):
        self.test_name()
        self.driver.find_element(By.XPATH, '//*[@id="tsuid_35"]/span/div/div/div[9]/g-more-link/a/div').click()
        sleep(2)

    def test_tag_name(self):
        driver = self.driver
        driver.find_element(By.TAG_NAME, 'textarea').send_keys('test')
        sleep(1)
        driver.find_element(By.CLASS_NAME, 'lnXdpd').click()
        sleep(1)
        driver.find_elements(By.CLASS_NAME, 'gNO89b')[1].click()
        sleep(2)


if __name__ == '__main__':
    case = TestCase()
    case.test_id()
