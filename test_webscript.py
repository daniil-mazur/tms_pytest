import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import math


def test_run_web(chromedriver):
    chrome = chromedriver
    chrome.implicitly_wait(10)
    url = 'https://demoqa.com/select-menu'
    chrome.get(url=url)
    search_box = chrome.find_element(By.XPATH, '//div[@id="selectOne"]//input')
    search_box.send_keys('Ms.')
    search_box.submit()
    time.sleep(20)

def test_run_web_2(chromedriver):
    chrome = chromedriver
    chrome.implicitly_wait(10)
    url = 'https://demoqa.com/select-menu'
    chrome.get(url=url)
    search_box = chrome.find_element(By.XPATH, '//div[@id="selectOne"]//input')
    search_box.send_keys('Ms.')
    search_box.submit()
    time.sleep(20)


def test_short_css(chromedriver):
    chrome = chromedriver
    chrome.implicitly_wait(10)
    url = 'https://ultimateqa.com/simple-html-elements-for-automation/'
    chrome.get(url=url)
    chrome.implicitly_wait()
    search_box = chrome.find_element(By.ID, 'idExample')
    search_box.click()
    time.sleep(20)


def test_no_wait(chromedriver):
    chrome = chromedriver
    url = 'https://suninjuly.github.io/wait2.html'
    chrome.get(url)
    button_locator = (By.ID, 'verify')
    button = chrome.find_element(button_locator[0], button_locator[1])
    button.click()
    message_locator = (By.ID, 'verify_message')
    message = chrome.find_element(message_locator[0], message_locator[1])
    assert message.text == 'Verification was successful!'


def test_wait_implicity(chromedriver):
    chrome = chromedriver
    chrome.implicitly_wait(10)
    url = 'https://suninjuly.github.io/wait2.html'
    chrome.get(url)
    button_locator = (By.ID, 'verify')
    button = chrome.find_element(button_locator[0], button_locator[1])
    button.click()
    message_locator = (By.ID, 'verify_message')
    message = chrome.find_element(message_locator[0], message_locator[1])
    assert message.text == 'Verification was successful!'


def test_wait_explicity(chromedriver):
    chrome = chromedriver
    url = 'https://suninjuly.github.io/wait2.html'
    chrome.get(url)
    button_locator = (By.ID, 'verify')
    button = WebDriverWait(chrome, 10).until(EC.element_to_be_clickable(button_locator))
    button.click()
    message_locator = (By.ID, 'verify_message')
    message = WebDriverWait(chrome, 10).until(EC.presence_of_element_located(message_locator))
    assert message.text == 'Verification was successful!'


def test_radiobuttons(chromedriver):
    chrome = chromedriver
    url = 'https://ultimateqa.com/sample-application-lifecycle-sprint-3/'
    chrome.get(url)
    male_locator = (By.CSS_SELECTOR, '[name=gender][value=male]')
    female_locator = (By.CSS_SELECTOR, '[name=gender][value=female]')
    male_button = WebDriverWait(chrome, 10).until(EC.presence_of_element_located(male_locator))
    female_button = WebDriverWait(chrome, 10).until(EC.presence_of_element_located(female_locator))
    assert male_button.is_selected()
    assert not female_button.is_selected()
    female_button.click()
    assert not male_button.is_selected()
    assert female_button.is_selected()
    print('finish')


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def test_robots(chromedriver):
    chrome = chromedriver
    url = 'http://suninjuly.github.io/math.html'
    chrome.get(url)
    input_value_locator = (By.CSS_SELECTOR, '[id=input_value]')
    input_value = WebDriverWait(chrome, 10).until(EC.presence_of_element_located(input_value_locator))
    res = calc(input_value.text)
    answer_field_locator = (By.CSS_SELECTOR, '[id=answer]')
    answer_field = WebDriverWait(chrome, 10).until(EC.presence_of_element_located(answer_field_locator))
    answer_field.send_keys(res)
    WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                '[id="robotCheckbox"]'))).click()
    WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                '[id="robotsRule"]'))).click()
    button = WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                         '[type=submit]')))
    button.click()


def test_alert_simple(chromedriver):
    chrome = chromedriver
    url = 'https://demo.guru99.com/test/delete_customer.php'
    chrome.get(url)
    WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                '[type="submit"]'))).click()
    # webel = chrome.find_element(By.CSS_SELECTOR,'[type="submit"]')

    # chrome.execute_script("arguments[0].click();", webel)
    # actions = ActionChains(chromedriver)
    # actions.context_click(on_element=webel)
    # actions.perform()
    alert_message = chrome.switch_to.alert
    alert_message.accept()
    alert_message.accept()
    print('i')


def test_iframe(chromedriver):
    chrome = chromedriver
    url = 'https://demo.guru99.com/test/guru99home/'
    chrome.get(url)
    youtube_loc = (By.XPATH, "//*[text()='writeEmbed();']")
    frame_locator = (By.XPATH, "//iframe[@wmode='transparent']")
    # frame_obj = WebDriverWait(chrome, 10).until(EC.presence_of_element_located(frame_locator))
    WebDriverWait(chrome, 10).until(EC.frame_to_be_available_and_switch_to_it(frame_locator))
    youtube_el = WebDriverWait(chrome, 10).until(EC.presence_of_element_located(youtube_loc))
    chrome.switch_to.default_content()
    print('i')

def test_iframe_and_alert(chromedriver):
    chrome = chromedriver
    url = 'https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt'
    chrome.get(url)
    button_locator = (By.CSS_SELECTOR, 'button[onclick="myFunction()"]')
    frame_locator = (By.CSS_SELECTOR, 'iframe[id="iframeResult"]')
    WebDriverWait(chrome, 10).until(EC.frame_to_be_available_and_switch_to_it(frame_locator))
    youtube_el = WebDriverWait(chrome, 10).until(EC.presence_of_element_located(button_locator))
    youtube_el.click()
    prompt = chrome.switch_to.alert
    prompt.send_keys('Daniil')
    prompt.accept()

# def test_actions(chromedriver):
#     driver = chromedriver
#     # get geeksforgeeks.org
#     driver.get("https://www.geeksforgeeks.org/")
#
#     # get element
#     element = driver.find_element(By.PARTIAL_LINK_TEXT, "Courses")
#
#     # create action chain object
#     action = ActionChains(driver)
#
#     # click the item
#     action.click(on_element=element)
#
#     # perform the operation
#     action.perform()
#
#     print('lol')