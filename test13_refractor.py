import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import click_element, get_element
from utils import send_keyword

search_text_field = (By.ID, 'APjFqb')
google_logo_image = (By.CLASS_NAME, 'lnXdpd')
google_search_btn = (By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[4]/div[6]/center/input[1]')


class test4(unittest.TestCase):

    @classmethod
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.google.com/')
        self.driver.maximize_window()
        print('Setting up WebDriver')

    def test_prop(self):
        driver = self.driver
        print(driver.name)
        click_element(driver, *google_logo_image)
        sleep(3)
        print(1)
        # print(self.driver.current_url)
        # print(self.driver.title)
        # print(self.driver.window_handles)
        # print(self.driver.page_source)

    def test_method(self):
        driver = self.driver
        send_keyword(driver, *search_text_field, keyword='shopee')
        sleep(1)
        # click_element(driver, *google_logo_image)
        # sleep(1)
        click_element(driver, *google_search_btn, index=0)
        # sleep(1)
        # driver.back()
        # sleep(1)
        # driver.refresh()
        # sleep(1)
        # driver.forward()
        # sleep(1)
        print(2)

    @classmethod
    def tearDown(self) -> None:
        print('Quitting the WebDriver...')
        self.driver.quit()


if __name__ == '__main__':
    # unittest.main()
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(test4))
    # suite = unittest.TestLoader().loadTestsFromTestCase(test4)
    unittest.TextTestRunner(verbosity=2).run(suite)
