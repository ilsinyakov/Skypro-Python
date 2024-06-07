import requests


class CompanyApi:
    def __init__(self, url):
        self.url = url

    def get_company_list(self, params_to_add=None):
        resp = requests.get(f'{self.url}/company', params=params_to_add)
        return resp.json()

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

    def get_company(self, id):
        resp = requests.get(f'{self.url}/company/{id}')
        return resp.json()

    def edit(self, new_id, new_name, new_description):
        company = {
            "name": new_name,
            "description": new_description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(f'{self.url}/company/{new_id}',
                              headers=my_headers, json=company)
        return resp.json()

    def delete(self, id):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.get(f'{self.url}/company/delete/{id}',
                            headers=my_headers)
        return resp.json()

    def set_active_state(self, id, isActive):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        body = {}
        body["isActive"] = isActive
        resp = requests.patch(f'{self.url}/company/status/{id}',
                              headers=my_headers, json=body)
        return resp.json()
