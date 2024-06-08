import requests


class CompanyApi:
    def __init__(self, url):
        self.url = url

    def get_token(self, user="flora", password="nature-fairy"):
        creds = {
            "username": user,
            "password": password
        }
        resp = requests.post(f'{self.url}/auth/login', json=creds)
        token = resp.json()["userToken"]
        return token

    def create_company(self, name, description=''):
        company = {
            "name": name,
            "description": description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()

        resp = requests.post(f'{self.url}/company',
                             json=company, headers=my_headers)
        return resp.json()
