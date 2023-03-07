import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest_bdd import scenarios, given, when, then, parsers

scenarios('../features/alert.feature')


@given('Open Page To Delete User')
def open_page(chromedriver):
    url = 'https://demo.guru99.com/test/delete_customer.php'
    chromedriver.get(url)


@when('Click delete button')
def click_button(chromedriver):
    WebDriverWait(chromedriver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="submit"]'))).click()


@when('Accept all alerts')
def accept_alerts(chromedriver):
    alert_message = chromedriver.switch_to.alert
    alert_message.accept()
    alert_message.accept()

@then('Check Url')
def check_url(chromedriver):
    assert 'https://demo.guru99.com/test/delete_customer.php' == chromedriver.current_url
