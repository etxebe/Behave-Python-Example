from features.browser import Browser
from features.pages.locators import *
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(Browser):
    url = "http://www.onet.pl/"

    def select_city(self, city_name):
        try:
            self.driver.find_element(*HomePageLocators.SELECT_CITY_MENU).click()
            self.driver.find_element(*HomePageLocators.CITIES_TO_SELECT).find_element(By.PARTIAL_LINK_TEXT, city_name).click()
        except NoSuchElementException:
            print('Podane miasto nie znajduje się na liście do wyboru!!')
            raise

    def search_for_city(self, city_name):
        self.driver.find_element(*HomePageLocators.SELECT_CITY_MENU).click()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(HomePageLocators.CITY_TYPE))
        self.driver.find_element(*HomePageLocators.CITY_TYPE).click()
        self.driver.find_element(*HomePageLocators.CITY_TYPE).send_keys(city_name)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(HomePageLocators.CITY_OK_BUTTON))
        self.driver.find_element(*HomePageLocators.CITY_OK_BUTTON).click()

    def city_name_has_changed(self, city_name):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(HomePageLocators.SELECTED_CITY, city_name))