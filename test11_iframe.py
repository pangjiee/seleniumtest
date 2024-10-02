from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://sahitest.com/demo/framesTest.htm')

    def test1(self):
        driver = self.driver
        WebDriverWait(driver, 2)
        driver.switch_to.frame(driver.find_element(By.NAME, 'top'))
        driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td[1]/a[1]').click()
        sleep(3)
        driver.switch_to.default_content()
        sleep(3)
        driver.switch_to.frame(driver.find_element(By.XPATH, '/html/frameset/frame[2]'))
        driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td[1]/a[1]').click()
        sleep(3)
        driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test1()
