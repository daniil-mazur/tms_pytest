import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest import fixture
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



@fixture()
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@fixture
def get_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.close()


def test_thedemoosite(get_driver):
    chrome = get_driver
    url = 'https://thedemosite.co.uk/addauser.php'
    chrome.get(url=url)
    chrome.maximize_window()
    username_input = chrome.find_element(By.NAME, 'username')
    username_input.send_keys('TestUser')
    password_input = chrome.find_element(By.NAME, 'password')
    password_input.send_keys('TestPass')
    save_input = chrome.find_element(By.NAME, 'FormsButton2')
    save_input.click()
    time.sleep(10)


def test_demoqa(get_driver):
    chrome = get_driver
    url = 'https://demoqa.com/text-box'
    chrome.get(url=url)
    chrome.maximize_window()
    full_name_input = chrome.find_element(By.ID, 'userName')
    full_name_input.send_keys('UserName')
    email_input = chrome.find_element(By.ID, 'userEmail')
    email_input.send_keys('email@example.com')
    current_address = chrome.find_element(By.ID, 'currentAddress')
    current_address.send_keys('User current address')
    permanent_address = chrome.find_element(By.ID, 'permanentAddress')
    permanent_address.send_keys('User permanent address')
    submit_button = chrome.find_element(By.ID, 'submit')
    submit_button.click()

    list_of_data = chrome.find_elements(By.CLASS_NAME, 'mb-1')
    assert 'UserName' in list_of_data[0].text
    assert 'email@example.com' in list_of_data[1].text
    assert 'User current address' in list_of_data[2].text
    assert 'User permanent address' in list_of_data[3].text
    time.sleep(10)

def test_google(get_driver):
    chrome = get_driver
    url = 'http://google.com/'
    chrome.get(url=url)
    chrome.maximize_window()
    search_box = chrome.find_element(By.NAME, 'q')
    search_box.send_keys('python 3.10')
    search_box.submit()
    assert 'python 3.10' in chrome.title
    chrome.close()


