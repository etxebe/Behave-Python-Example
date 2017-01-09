from features.browser import Browser
from features.pages.homepage import HomePage


def before_all(context):
    context.browser = Browser()
    context.homepage = HomePage()


def after_all(context):
    context.browser.quit()