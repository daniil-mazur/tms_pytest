

from retrying import retry
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait



class Locators:
    iframe = (By.XPATH, "//iframe")


class BasePage:
    def __init__(self, webdriver: Chrome):
        self.webdriver = webdriver

    def find_element(self, locator, timer=10):
        return WebDriverWait(self.webdriver, timer).until(
            expected_conditions.presence_of_element_located(locator), message=f"Can't find element by locator {locator}"
        )

    def element_click(self, locator, timer=30):
        return (
            WebDriverWait(self.webdriver, timer).until(
                expected_conditions.element_to_be_clickable(locator),
                message=f"Can't click or check 'is clickable'" f" by locator {locator}",
            )
        ).click()

    @retry(stop_max_delay=10000)
    def element_click_with_retry(self, locator, timer=30):
        """
        Workaround for Chrome: last versions of Chrome webdriver have difficults with clicker.
        Alternative WA: Expected Conditions (passed, doesn't help)
        Retrying (implemented), JS_execute (doesn't work), Action scroll (doesn't work)
        """
        return (
            WebDriverWait(self.webdriver, timer).until(
                expected_conditions.element_to_be_clickable(locator), message=f"Can't find element by locator {locator}"
            )
        ).click()

    def find_elements(self, locator, timer=10):
        return WebDriverWait(self.webdriver, timer).until(
            expected_conditions.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )

    def wait_until_element_is_not_presented(self, locator, timer):
        WebDriverWait(self.webdriver, timer).until(
            expected_conditions.invisibility_of_element_located(locator),
            message=f"Element is still presented {locator}",
        )

    def open_url(self, url: str):
        return self.webdriver.get(url)

    def fill_field(self, locator, value: str, timer=10):
        input_field = WebDriverWait(self.webdriver, timer).until(
            expected_conditions.element_to_be_clickable(locator), message=f"Can't find element by locator {locator}"
        )
        input_field.clear()
        input_field.send_keys(value)

    def switch_to_iframe(self, iframe=Locators.iframe, depth=1):
        for frame in range(0, depth):
            if self.webdriver.switch_to.active_element.tag_name.lower() in ["body", "iframe"]:
                try:
                    WebDriverWait(self.webdriver, 20).until(
                        expected_conditions.frame_to_be_available_and_switch_to_it(iframe)
                    )
                except TimeoutException as e:
                    raise TimeoutException(e) from e

    def switch_to_default_content(self):
        self.webdriver.switch_to.default_content()

    def find_element_by_visible_text(self, visible_text, element_type):
        locator = (By.XPATH, f'//{element_type}[contains(text(), "{visible_text}")]')
        return self.find_element(locator)

    def is_element_present(self, method: str, value: str) -> None:
        try:
            self.webdriver.find_element(method, value)
        except NoSuchElementException as e:
            print(f"Element ({method}, {value}) is not presented on the screen or in iframe.")
            raise e

    def element_by_visible_text_is_present(self, visible_text: str):
        locator = f'//*[contains(text(), "{visible_text}")]'
        self.is_element_present(By.XPATH, locator)

    def wait_until_page_is_loaded(self):
        WebDriverWait(self.webdriver, 60).until(expected_conditions.presence_of_element_located((By.TAG_NAME, "html")))

    def select_dropdown_option(self, locator, value: str):
        select = Select(self.find_element(locator))
        return select.select_by_value(value)
