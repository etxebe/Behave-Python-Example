from selenium.webdriver.common.by import By


class HomePageLocators(object):

    CHECK_PAGE_LOADED = (By.XPATH, '//*[@id="mainPageBody"]/div[3]/div[1]/article/div[1]/a/img')

    # WEATHER SECTION
    WEATHER_NOW = (By.CSS_SELECTOR, '.temperature.temperatureNow')
    WEATHER_TOMORROW = (By.CSS_SELECTOR, '.temperature.temperatureTomorrow')
    SELECTED_CITY = (By.CSS_SELECTOR, '.selectedCityWrapper .cityName')
    SELECT_CITY_MENU = (By.CLASS_NAME, 'selectedCityWrapper')
    CITIES_TO_SELECT = (By.CLASS_NAME, 'cityList')
    CITY_TYPE = (By.CLASS_NAME, 'citySearchField')
    CITY_OK_BUTTON = (By.CLASS_NAME, 'citySearchSubmit')