
import base64
from logging import exception
import time
import json
import requests


class Token:

    def __init__(self, value: str) -> None:
        self.header, self.body, self.signature = value.split('.')
        self.__value = value

    def is_valid(self) -> bool:
        access_bytes = self.get_padded_string(self.body).encode('UTF-8')
        message_bytes = base64.b64decode(access_bytes)
        a = message_bytes.decode()
        x = json.loads(a)
        expire_token = x['exp']
        if expire_token>time.time():
            return True
        return False

    def __str__(self) -> str:
        return self.__value

    def __repr__(self) -> str:
        return self.__value
    
    @staticmethod
    def get_padded_string(value):
        filler = 4-value.__len__()%4
        if filler == 4:
            filler=0
        return value+'='*filler

class WarehouseClient:
    
    base_url = 'http://172.16.10.26:8001'

    def __init__(self) -> None:
        value = self.login('admin@ewebsign.com', 'admin123`$')
        self.access_tok: Token  = Token(value['access'])
        self.refresh_tok: Token = Token(value['refresh'])
        self.logged_in: bool = False

    def login(self, email: str, password: str):
        url = f"{self.base_url}/api/user/login/"

        data = {
          "email": email,
          "password": password
        }

        response = requests.post(url, json = data)
        if response.status_code == 200:
            self.logged_in = True
            return response.json()
        raise Exception('Login Error')

    def refresh_token(self):
        url = f"{self.base_url}/api/user/token/refresh/"
        data = {
            'refresh': self.refresh_tok.__str__()
        }
        response = requests.post(url, json = data)
        if response.status_code == 200:
            res = response.json()
            self.access_tok: Token  = Token(res['access'])
            self.refresh_tok: Token = Token(res['refresh'])
        

    def list_job(self):
        url = f"{self.base_url}/api/jobs/hrog/?limit=1"
        res = requests.get(url, headers={'Authorization': f'Bearer {self.access_tok}'})
        if res.status_code == 200:
            return res.json()
        raise requests.HTTPError

client = WarehouseClient()
while True:
    if client.access_tok.is_valid():
        print(client.list_job())
        time.sleep(10)
    elif client.refresh_tok.is_valid():
        client.refresh_token()
    else:
        exit()
