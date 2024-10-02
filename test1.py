from time import sleep

from selenium import webdriver

# define which browser
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# which url
url = 'https://www.google.com/'

# run
#driver.get(url)

# get web pag e tile
print(driver.title)

# use this to find element by their web element ID
google_search_bar = 'APjFqb'
search_key_word = 'selenium'
# driver.find_element(By.ID, google_search_bar).send_keys(search_key_word)

# sleep(1)

first_search_result_id = 'jZ2SBf'


# driver.find_element(By.ID, first_search_result_id).click()
# sleep(2)

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def test(self):
        driver = self.driver
        driver.get(url)
        driver.find_element(By.ID, google_search_bar).send_keys(search_key_word)
        sleep(2)
        driver.find_element(By.ID, first_search_result_id).click()
        sleep(2)


if __name__ == '__main__':
    case = TestCase()
    case.test()
