from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from utils import click_element
from utils import send_keyword

search_text_field = (By.ID, 'APjFqb')
google_logo_image = (By.CLASS_NAME, 'lnXdpd')
google_search_btn = (By.CLASS_NAME, 'gNO89b')


class TestCase(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.google.com/')

    def test_prop(self):
        print(self.driver.name)
        print(self.driver.current_url)
        print(self.driver.title)
        print(self.driver.window_handles)
        print(self.driver.page_source)
        self.driver.quit()

    def test_method(self):
        driver = self.driver
        send_keyword(driver, *search_text_field, keyword='shopee')
        sleep(1)
        click_element(driver, *google_logo_image)
        sleep(1)
        click_element(driver, *google_search_btn, index=1)
        sleep(1)
        driver.back()
        sleep(1)
        driver.refresh()
        sleep(1)
        driver.forward()
        sleep(1)
        self.driver.close()  # close current tab
        self.driver.quit()  # close window browser


if __name__ == '__main__':
    case = TestCase()
    case.test_method()
