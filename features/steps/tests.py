# -*- coding: utf-8 -*-

from nose.tools import *
from behave import *
from features.pages.locators import HomePageLocators
from compare import expect


@when('we visit onet homepage')
def step_impl(context):
    context.browser.visit()
    context.browser.is_page_loaded(HomePageLocators.CHECK_PAGE_LOADED)


@then('we should see correct url address and correct title')
def step_impl(context):
    current_url = context.browser.get_current_url()
    title = context.browser.title()
    eq_(current_url, "http://www.onet.pl/")
    eq_(title, 'Onet.pl')


@when('we visit onet site')
def step_impl(context):
    context.browser.visit()
    context.browser.is_page_loaded(HomePageLocators.CHECK_PAGE_LOADED)


@step('we select Poznan from cities list')
def step_impl(context):
    context.homepage.select_city('Pozna')


@then('we should check the temperatures')
def step_impl(context):
    temperature_now = context.browser.get_text_from_element(*HomePageLocators.WEATHER_NOW)
    temperature_tomorrow = context.browser.get_text_from_element(*HomePageLocators.WEATHER_TOMORROW)
    city_name = context.browser.get_text_from_element(*HomePageLocators.SELECTED_CITY)
    expect(temperature_now).to_contain('7')
    expect(temperature_now).to_contain('C')
    expect(temperature_tomorrow).to_contain('5')
    expect(temperature_tomorrow).to_contain('C')
    expect(city_name).to_contain('Pozna')
    # eq_(temperature_now, "9°C")
    # eq_(temperature_tomorrow, '10°C')


@when('we type Tczew other than from list')
def step_impl(context):
    context.browser.visit()
    context.browser.is_page_loaded(HomePageLocators.CHECK_PAGE_LOADED)
    context.homepage.search_for_city('Tczew')
    context.homepage.city_name_has_changed('Tczew')


@then('we should check the temperatures in Tczew')
def step_impl(context):
    temperature_now = context.browser.get_text_from_element(*HomePageLocators.WEATHER_NOW)
    temperature_tomorrow = context.browser.get_text_from_element(*HomePageLocators.WEATHER_TOMORROW)
    city_name = context.browser.get_text_from_element(*HomePageLocators.SELECTED_CITY)
    expect(temperature_now).to_contain('6')
    expect(temperature_now).to_contain('C')
    expect(temperature_tomorrow).to_contain('4')
    expect(temperature_tomorrow).to_contain('C')
    expect(city_name).to_contain('Tczew')


@when('we type Gdynia other than from list')
def step_impl(context):
    context.browser.visit()
    context.browser.is_page_loaded(HomePageLocators.CHECK_PAGE_LOADED)
    context.homepage.search_for_city('Gdynia')
    context.homepage.city_name_has_changed('Gdynia')


@then('we should check the temperatures in Gdynia')
def step_impl(context):
    temperature_now = context.browser.get_text_from_element(*HomePageLocators.WEATHER_NOW)
    temperature_tomorrow = context.browser.get_text_from_element(*HomePageLocators.WEATHER_TOMORROW)
    city_name = context.browser.get_text_from_element(*HomePageLocators.SELECTED_CITY)
    expect(temperature_now).to_contain('6')
    expect(temperature_now).to_contain('C')
    expect(temperature_tomorrow).to_contain('4')
    expect(temperature_tomorrow).to_contain('C')
    expect(city_name).to_contain('Gdynia')