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
import math
from page_objects.robot_page import RobotPage
from page_objects.potter_page import PotterPage


'''
Тест РоботПейдж:
1. Открыть страницу робота
2. Вписать ответ на задачу
3. Нажать чекбокс "Я робот"
4. Нажать радиобаттом "Роботы рулят"
5. Нажать Сабмит
6. Убедиться, что таймер остановился

'''

def test_robots_new(chromedriver):
    robot_page = RobotPage(chromedriver)
    #======================
    robot_page.open()
    robot_page.resolve_task()
    # input_value = robot_page.get_input_value()
    # result = robot_page.calc(input_value)
    # robot_page.fill_answer_field(result)
    robot_page.select_i_am_robot()
    robot_page.select_robots_rule()
    robot_page.submit_response()
    #robot_page.check_timer_is_frozen



def test_iframe_and_alert(chromedriver):

    name = 'Daniil'
    potter_page = PotterPage(chromedriver)
    #===============================
    potter_page.open()
    potter_page.click_try_it()
    potter_page.fill_and_accept_alert(name)
    potter_page.verify_message(name)
