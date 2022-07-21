
import base64
from email import message
import json
import time
import requests
import csv


class Token:

    def __init__(self, value: str) -> None:
        self.header, self.body, self.signature = value.split('.')
        self.__value = value

    def is_valid(self) -> bool:
        access_bytes = self.get_padded_string(self.body).encode('UTF-8')
        message_bytes = base64.b64decode(access_bytes)
        my_dict = json.loads(message_bytes.decode())
        expire_token = my_dict['exp']
        if expire_token > time.time():
            return True
        return False

    def __str__(self) -> str:
        return self.__value

    def __repr__(self) -> str:
        return self.__value

    @staticmethod
    def get_padded_string(value):
        filler = 4-value.__len__() % 4
        if filler == 4:
            filler = 0
        return value+'='*filler


class ShiftManagement:

    base_url = 'http://172.16.10.10:8000'

    def __init__(self) -> None:
        value = self.login('admin@admin.com', 'password')
        # value = self.login('ritudhakal5@gmail.com', 'password')
        self.token: Token = Token(value['result']['token'])
        permission = []

    def login(self, email: str, password: str):
        url = f"{self.base_url}/api/auth/login"

        data = {
            'email': email,
            'password': password
        }

        response = requests.post(url, json=data)
        if response.status_code == 200:
            self.logged_in = True
            return response.json()
        raise Exception('Login Error')

    def me(self):
        url = f"{self.base_url}/api/auth/me"
        res = requests.get(
            url, headers={'Authorization': f'Bearer {self.token}'})
        if res.status_code == 200:
            self.permission = res.json()['result']['message']['permission']
            self.detail = res.json()['result']['message']['detail']
            return (self.permission, self.detail)
        raise requests.HTTPError

    def list_of_roles(self):
        # print(self.permission)
        if 'assign_role' in self.permission:
            url = f"{self.base_url}/api/auth/roles"
            response = requests.get(
                url, headers={'Authorization': f'Bearer {self.token}'})
            if response.status_code == 200:
                return response.json()
            raise requests.HTTPError
        raise Exception('No Permission')

    def create_availability(self, from_date: str, to_date: str, availability_type: int, start_time: int, end_time: int, comments: str, custom_date: list):
        if 'create_availability' in self.permission:
            url = f"{self.base_url}/api/auth/availability/create-availability"
            data = {
                'from_date': from_date,
                'to_date': to_date,
                'availability_type': availability_type,
                'start_time': start_time,
                'end_time': end_time,
                'comments': comments,
                'custom_date': custom_date,
            }
            response = requests.post(
                url, headers={'Authorization': f'Bearer {self.token}'}, json=data)
            if response.status_code == 200:
                return response.json()
            else:
                error = response.json()
                error['message']['from_date'] = from_date
                error['message']['to_date'] = to_date
                error['success'] = False
                return error
        raise Exception('No Permission')

    def get_availability(self):
        if 'view_availability' in self.permission:
            url = f"{self.base_url}/api/auth/availability/get-availability"
            response = requests.get(url, headers={'Authorization': f'Bearer {self.token}'})
            # print(response)
            if response.status_code == 200:
                return response.json()
            raise requests.HTTPError
        raise Exception('No Permission')

    def register(self):
        if 'user_create' in self.permission:
            url = f"{self.base_url}/api/auth/register"
            with open('users.json', 'r') as f:
                list_data = json.load(f)
            for data in list_data:
                # print(data)
                response = requests.post(url, headers={'Authorization': f'Bearer {self.token}'}, json=data)
                print(response.json()) 
        else: Exception('No Permission')

    def delete_user(self):
        if 'user_delete' in self.permission:
            url = f"{self.base_url}/api/auth/user/delete-user"
            with open('users.json', 'r') as f:
                list_data = json.load(f)
            for data in list_data:
                response = requests.post(url, headers={'Authorization': f'Bearer {self.token}'}, json={'email': data['email']})
                print(response.json()) 
        else: Exception('No Permission')


staff = ShiftManagement()
staff.me()
# print(staff.list_of_roles())
# print(staff.create_availability('2022-06-21','2022-06-22', 0, 10, 16, 'i will work as full time (office time) for specified dates 1', ['2022-6-23']))
# print(staff.create_availability('','', 0, 10, 16, 'i will work as full time (office time) for specified dates 1', ['2022-6-23']))
# print(staff.get_availability())
staff.register()
# print(staff.delete_user())
