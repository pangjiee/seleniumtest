from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from utils import click_element, send_keyword, get_element

# url = 'https://sahitest.com/demo/'
url = 'https://www.baidu.com/'
link_test_element = (By.LINK_TEXT, 'Link Test')
search_text_field = (By.ID, 't1')
xpath_form = (By.XPATH, '/html/body/form[1]')
bd_news_tab = (By.XPATH, '//*[@id="s-top-left"]/a[1]')


class TestCase(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def test_webelement_prop(self):
        driver = self.driver
        click_element(driver, *link_test_element)
        sleep(1)
        e = driver.find_element(*xpath_form)
        e.find_element(*search_text_field).send_keys('wenjie')
        # send_keyword(driver, *search_text_field, keyword='hello world')
        sleep(1)
        print(get_element(driver, *search_text_field).get_attribute('value'))
        print(get_element(driver, *search_text_field).value_of_css_property('font'))

        get_element(driver, *search_text_field).clear()
        sleep(2)
        driver.quit()

    def test_window_tab(self):
        driver = self.driver
        sleep(2)
        windows = self.driver.window_handles
        click_element(driver,   *bd_news_tab)
        print(driver.title)
        for window_handle in windows:
            if window_handle != windows:
                print(driver.title)
                driver.switch_to.window(window_handle)
                break
        sleep(5)
        driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test_window_tab()


# for forms alert can use self.driver.switch_to_alert.accept() to click ok