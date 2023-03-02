from selenium.webdriver.common.by import By
from selenium import webdriver
import math
from page_objects.base_page import BasePage


class RobotPageLocators:
    input_value_locator = (By.CSS_SELECTOR, '[id=input_value]')
    answer_field_locator = (By.CSS_SELECTOR, '[id=answer]')
    i_am_robot_locator = (By.CSS_SELECTOR, '[id="robotCheckbox"]')
    robots_rule_locator = (By.CSS_SELECTOR, '[id="robotsRule"]')
    submit_response_locator = (By.CSS_SELECTOR, '[type=submit]')


class RobotPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'http://suninjuly.github.io/math.html'

    def calc(self, x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    def get_input_value(self):
        input_value = self.get_text_from_element(RobotPageLocators.input_value_locator)
        return input_value

    def fill_answer_field(self, content):
        self.send_keys(locator=RobotPageLocators.answer_field_locator, content=content)

    def resolve_task(self):
        input_value = self.get_input_value()
        result = self.calc(input_value)
        self.fill_answer_field(result)

    def select_i_am_robot(self):
        self.click_element(RobotPageLocators.i_am_robot_locator)

    def select_robots_rule(self):
        self.click_element(RobotPageLocators.robots_rule_locator)

    def submit_response(self):
        self.click_element(RobotPageLocators.submit_response_locator)
