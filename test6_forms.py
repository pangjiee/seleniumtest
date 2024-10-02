from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import os

from selenium.webdriver.support.select import Select

from utils import click_element


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///' + path + '/form1.html'
        self.driver.get(file_path)

    def test_checkbox(self):
        driver = self.driver
        swim_btn = driver.find_element(By.NAME, 'swimming')
        read_btn = driver.find_element(By.NAME, 'reading')
        if not swim_btn.is_selected():
            swim_btn.click()

        if not read_btn.is_selected():
            read_btn.click()
        sleep(3)
        driver.quit()

    def test_radio_btn(self):
        driver = self.driver
        lst = driver.find_elements(By.NAME, 'gender')
        # can use this to get the list of elements under same name
        lst[1].click()
        sleep(3)
        driver.quit()

    def test_option_btn(self):
        driver = self.driver
        ele = driver.find_element(By.ID, 'provide')
        # can use this to get the  list of elements under same name
        select = Select(ele)
        select.select_by_index(2)
        sleep(3)
        select.select_by_value("bj")
        sleep(3)
        select.select_by_visible_text("Shanghai")
        sleep(3)
        select.deselect_all()
        sleep(3)
        driver.quit()

    def test_alert(self):
        driver = self.driver
        driver.find_element(By.ID, 'alert').click()
        alert_ele = driver.switch_to.alert
        print(alert_ele.text)
        sleep(3)
        alert_ele.accept()
        sleep(3)
        driver.quit()

    def test_confirm(self):
        driver = self.driver
        driver.find_element(By.ID, 'confirm').click()
        confirm_ele = driver.switch_to.alert
        print(confirm_ele.text)
        confirm_ele.accept()
        confirm_ele.dismiss()
        sleep(3)
        driver.quit()

    def test_prompt(self):
        driver = self.driver
        driver.find_element(By.ID, 'prompt').click()
        prompt = driver.switch_to.alert
        print(prompt.text)
        sleep(3)
        prompt.send_keys('20')
        sleep(3)
        prompt.accept()
        sleep(3)
        driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test_prompt()

# accept/ dismiss, text, send_keys
