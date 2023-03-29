import allure

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


@allure.feature('Feature 1')
@allure.title('Demo test for Web alerts')
def test_iframe_and_alert(chromedriver_docker):
    # arrange
    name = 'Daniil'
    with allure.step('Open Potter Page'):
        potter_page = PotterPage(chromedriver_docker)
        potter_page.open()
    # actions
    with allure.step('Potter page: click button'):
        potter_page.click_try_it()
    with allure.step('Potter page: click alerts'):
        potter_page.fill_and_accept_alert(name)
    # assert
    with allure.step('Potter page: verify message'):
        potter_page.verifier.verify_message(name)
