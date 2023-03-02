import pytest
from triangle.triangle import Triangle
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# @pytest.fixture(scope='class', autouse=True)
# def printer():
#     print("\nIt is setup\n")
#     yield
#     print("\nTeardown\n")


@pytest.fixture()
def right_triangle():
    right_tr = Triangle(6, 6, 6)
    yield right_tr
    del right_tr


@pytest.fixture(params=[(3, 3, 4), (8, 8, 10), (5, 5, 8)])
def rb_triangle(request):
    rb_tr = Triangle(request.param[0], request.param[1], request.param[2])
    yield rb_tr
    del rb_tr


@pytest.fixture()
def chromedriver():
    chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield chrome
    chrome.close()
