import pytest
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

TOKEN = '3e738ded8190faa0d6082cedd4dbf5d8c6fb8d52b109712eaaf36880a4750e22'


@pytest.fixture()
def chromedriver():
    chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield chrome
    chrome.close()


@pytest.fixture()
def browser():
    chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield chrome
    chrome.close()


@pytest.fixture()
def chromedriver_headless():
    chromeopt = Options()
    chromeopt.add_argument("--headless")
    chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chromeopt)
    yield chrome
    chrome.close()


@pytest.fixture()
def chromedriver_docker() -> Options:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
