from selenium import webdriver
from time import sleep

# google
from selenium.webdriver.common.by import By

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
        driver.execute_script("alert('test')")
        sleep(2)
        driver.switch_to.alert.accept()
        sleep(2)
        driver.quit()

    def test2(self):
        js = 'return document.title'
        title = self.driver.execute_script(js)
        print(title)
        self.driver.quit()

    def test3(self):
        js = 'var q = document.getElementById("APjFqb"); q.style.border="2px solid red"'
        self.driver.execute_script(js)
        sleep(5)
        self.driver.quit()

    def test4(self):
        sleep(2)
        self.driver.find_element(By.ID, google_search_bar).send_keys('test')
        sleep(2)
        self.driver.find_element(By.ID, first_search_result_id).click()
        sleep(2)
        js = 'window.scrollTo(0, document.body.scrollHeight);'
        self.driver.execute_script(js)
        sleep(5)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test4()
