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


def test_iframe_and_alert(chromedriver_docker):
    # arrange
    name = 'Daniil'
    potter_page = PotterPage(chromedriver_docker)
    potter_page.open()
    # actions

    potter_page.click_try_it()
    potter_page.fill_and_accept_alert(name)
    # assert
    potter_page.verifier.verify_message(name)
