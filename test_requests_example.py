import requests
import random

# токен, необходимый на сайте для POST/PUT/PATCH/DELETE
TOKEN = '3e738ded8190faa0d6082cedd4dbf5d8c6fb8d52b109712eaaf36880a4750e22'

baseurl = 'https://gorest.co.in'

# словарь для заголовков запросов
headers = {
    'Authorization': 'Bearer ' + TOKEN
}


def test_get():
    user_id = 10
    response = requests.get(url=f'{baseurl}/public/v2/users/{user_id}',
                            headers=headers)
    response_json = response.json()
    assert response.status_code == 200
    for key in ['name', 'email', 'gender', 'id', 'status']:
        assert key in response_json


def test_patch():
    # создание строки с рандомным числом для избежания конфликта создания не уникального пользователя
    random_number = str(random.randint(0, 100000))
    # создание пользователя
    user_data = {"name": f"Mazur Daniil {random_number}", "gender": "male",
                 "email": f"test-user-{random_number}@15ce.com", "status": "active"}
    response = requests.post(url=f'{baseurl}/public/v2/users/',
                             headers=headers,
                             json=user_data)
    assert response.status_code == 201

    response_data = response.json()
    user_id = response_data['id']
    # частичное редактирование пользователя
    response = requests.patch(url=f'{baseurl}/public/v2/users/{user_id}',
                              headers=headers,
                              json={'name': f'Mazur Updated {random_number}'})
    assert response.status_code == 200

    # чтение данных о пользователе после редактирования
    response = requests.get(url=f'{baseurl}/public/v2/users/{user_id}',
                            headers=headers)
    assert response.status_code == 200
    assert response.json()['name'] == f'Mazur Updated {random_number}'

    # удаление пользователя
    response = requests.delete(url=f'{baseurl}/public/v2/users/{user_id}',
                               headers=headers)
    assert response.status_code == 204
    # проверка, что после удаления GET возвращает 404 - NOT FOUND
    response = requests.get(url=f'{baseurl}/public/v2/users/{user_id}',
                            headers=headers)

    assert response.status_code == 404


def test_token():
    response = requests.get(url='https://gorest.co.in/my-account/access-tokens/new')
    print(response)



1.