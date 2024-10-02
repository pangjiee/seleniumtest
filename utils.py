from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def get_element(driver, *loc):
    return driver.find_element(*loc)


def send_keyword(driver, *element, keyword):
    return driver.find_element(*element).send_keys(keyword)


def click_element(driver, *element, index=0):
    if index > 0:
        return driver.find_elements(*element)[index].click()
    else:
        return driver.find_element(*element).click()


def by_data_test_id(value):
    locator = (By.CSS_SELECTOR, f"[data-testid='{value}']")
    return locator


def by_data_cy(value):
    locator = (By.CSS_SELECTOR, f"[data-cy='{value}']")
    return locator


def verify(locator, text):
    locator_text = locator.text
    return locator_text == text


def print_red(text):
    print("\033[91m" + text + "\033[0m")


def print_check_expected(expected, on_screen):
    print('expected: ' + expected.text + ', on screen: ' + on_screen)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    url = 'https://www.google.com/'
    driver.get(url)
    loc = (By.ID, 'APjFqb')
    get_element(driver, *loc).send_keys('test')
    sleep(3)
