import json
import random
from api.user_api import UserApi
import allure

@allure.feature('Feature 2')
@allure.title('Demo test for REST api')
def test_patch():
    with allure.step('Generate data'):
        api = UserApi()
        # создание строки с рандомным числом для избежания конфликта создания не уникального пользователя
        random_number = str(random.randint(0, 100000))
        allure.attach(random_number, name='generated number')

    # создание пользователя
    user_id, create_status_code = api.create_user()
    assert create_status_code == 201

    # частичное редактирование пользователя
    update_status_code = api.update_user(user_id=user_id, patch_data={'name': f'Mazur Updated {random_number}'})
    assert update_status_code == 200

    with allure.step('Get users data'):
        # чтение данных о пользователе после редактирования
        get_user_data, get_user_status_code = api.get_user(user_id=user_id)
        allure.attach(body=json.dumps(get_user_data), name='Get user data')
    assert get_user_status_code == 200
    assert get_user_data['name'] == f'Mazur Updated {random_number}'

    # удаление пользователя
    remove_status_code = api.remove_user(user_id=user_id)
    assert remove_status_code == 204


    # проверка, что после удаления GET возвращает 404 - NOT FOUND
    get_user_data, get_user_status_code = api.get_user(user_id=user_id)
    assert get_user_status_code == 404
