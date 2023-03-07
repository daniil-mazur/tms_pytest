import math
from selenium.webdriver.common.by import By
from selenium import webdriver
from page_objects.base_page import BasePage


class PotterPageLocators:
    iframe_locator = (By.CSS_SELECTOR, 'iframe[id="iframeResult"]')
    button_locator = (By.CSS_SELECTOR, 'button[onclick="myFunction()"]')
    success_message_locator = (By.CSS_SELECTOR, 'p#demo')


class PotterPageVerifier:
    def __init__(self, page):
        self.page = page

    def verify_message(self, name):
        self.page.switch_to_default_context()
        self.page.switch_to_iframe(PotterPageLocators.iframe_locator)
        message = self.page.get_text_from_element(PotterPageLocators.success_message_locator)
        assert message == f'Hello {name}! How are you today?'


class PotterPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt'
        self.verifier = PotterPageVerifier(self)

    def click_try_it(self):
        self.switch_to_default_context()
        self.switch_to_iframe(PotterPageLocators.iframe_locator)
        self.click_element(PotterPageLocators.button_locator)

    def fill_name(self, name):
        self.fill_and_accept_alert(name)

    #
    # def click_run_button(self):
    #     self.switch_to_default_context()

    # def verify_message(self, name):
    #     self.switch_to_default_context()
    #     self.switch_to_iframe(PotterPageLocators.iframe_locator)
    #     message = self.get_text_from_element(PotterPageLocators.success_message_locator)
    #     assert message == f'Hello {name}! How are you today?'
