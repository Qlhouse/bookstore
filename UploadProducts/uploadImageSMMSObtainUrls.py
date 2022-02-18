'''
Refer to Github 
<https://github.com/XavierJiezou/python-sm.ms-api>
'''
import requests
import json
from pathlib import Path


class SMMS(object):
    # init
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.token = None
        self.profile = None
        self.history = None
        self.upload_history = None
        self.url = None

    # user
    def get_api_token(self):
        data = {
            'username': self.username,
            'password': self.password,
        }
        url = root+'token'
        res = requests.post(url, data=data).json()
        self.token = res['data']['token']
        self.headers = {'Authorization': self.token}
        # print(json.dumps(res, indent=4))

    # user
    def get_user_profile(self):
        url = root+'profile'
        res = requests.post(url, headers=self.headers).json()
        self.profile = res['data']
        print(json.dumps(res, indent=4))

    # image
    def clear_temporary_history(self):
        data = {
            'format': 'json'
        }
        url = root+'clear'
        res = requests.get(url, data=data).json()
        print(json.dumps(res, indent=4))

    # image
    def view_temporary_history(self):
        url = root+'history'
        res = requests.get(url).json()
        self.history = res['data']
        print(json.dumps(res, indent=4))

    # image
    def delete_image(self, hash):
        url = root+'delete/'+hash
        res = requests.get(url).json()
        print(json.dumps(res, indent=4))

    # image
    def view_upload_history(self):
        url = root+'upload_history'
        res = requests.get(url, headers=self.headers).json()
        self.upload_history = res['data']
        print(json.dumps(res, indent=4))

    # image
    def upload_image(self, path):
        try:
            files = {'smfile': open(path, 'rb')}
            url = root+'upload'
            res = requests.post(url, files=files, headers=self.headers).json()
            if res['success']:
                self.url = res['data']['url']
                # print(json.dumps(res, indent=4))
                print(self.url)
            else:
                print(res['message'])
        except Exception as e:
            print(e)


if __name__ == "__main__":
    root = 'https://sm.ms/api/v2/'
    smms = SMMS('qlinpy', 'Ql753286')
    smms.get_api_token()
    path = Path(r'C:\Users\xq127\Pictures\temp\CE9C20A44CDBFD9FEF2C3B71F478A1BB.jpg')
    smms.upload_image(path)
