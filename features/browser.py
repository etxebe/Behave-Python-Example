from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Browser(object):

    base_url = 'http://www.onet.pl/'
    binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
    fp = webdriver.FirefoxProfile(r'C:\Users\bznk\AppData\Roaming\Mozilla\Firefox\Profiles\9ypijang.Selenium')
    driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp)
    driver.implicitly_wait(10)

    def quit(self):
        self.driver.quit()

    def visit(self):
        self.driver.get(self.base_url)

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def get_current_url(self):
        return self.driver.current_url

    def title(self):
        return self.driver.title

    def is_page_loaded(self, elem):
        delay = 10  # seconds
        try:
            WebDriverWait(self.driver, delay).until(EC.visibility_of_element_located(elem))
        except TimeoutError:
            print('Page is not ready!!')

    def get_text_from_element(self, *elem):
        return self.driver.find_element(*elem).text
