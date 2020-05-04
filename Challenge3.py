import py as py
from selenium.webdriver.common.keys import Keys



def test_challenge3(copart):
    for car in copart.find("[ng-repeat*='popularSearch'] > a"):
        href = car.get_attribute('href')
        print(f'{car.text} - {href}')


def test_challenge4_copart(py):
    py.visit('https://copart.com')
    popular_models = py.find("li[ng-repeat*='popularSearch'] > a")
    for model in popular_models:
        print(f'{model.text} - {model.get_attribute("href")}')
    assert popular_models.length == 20













