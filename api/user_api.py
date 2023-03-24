import requests
import random
from conftest import  TOKEN


class UserApi():

    def __init__(self):

        self.baseurl = 'https://gorest.co.in'

        # словарь для заголовков запросов
        self.headers = {
            # 'Authorization': 'Bearer ' + self.__get_token()
            'Authorization': 'Bearer ' + TOKEN
        }

    # def __get_token(self):
    #     requests.get('url_for_token')
    #     return ''

    def generate_user_data(self):
        random_number = random.randint(0, 10000000)
        user_data = {"name": f"Mazur Daniil {random_number}", "gender": "male",
                     "email": f"test-user-{random_number}@15ce.com", "status": "active"}
        return user_data

    def create_user(self, input_data=None):
        user_data = input_data or self.generate_user_data()
        response = requests.post(url=f'{self.baseurl}/public/v2/users/',
                                 headers=self.headers,
                                 json=user_data)
        return response.json()['id'], response.status_code

    def get_all_users(self):
        response = requests.get(url=f'{self.baseurl}/public/v2/users',
                                headers=self.headers)
        return response.json(), response.status_code

    def get_user(self, user_id):
        response = requests.get(url=f'{self.baseurl}/public/v2/users/{user_id}',
                                headers=self.headers)
        return response.json(), response.status_code

    def update_user(self, user_id, patch_data):
        response = requests.patch(url=f'{self.baseurl}/public/v2/users/{user_id}',
                                  headers=self.headers,
                                  json=patch_data)
        return response.status_code

    def rewrite_user(self, user_id, put_data):
        response = requests.put(url=f'{self.baseurl}/public/v2/users/{user_id}',
                                headers=self.headers,
                                json=put_data)
        return response.status_code

    def remove_user(self, user_id):
        response = requests.delete(url=f'{self.baseurl}/public/v2/users/{user_id}',
                                   headers=self.headers)
        return response.status_code
