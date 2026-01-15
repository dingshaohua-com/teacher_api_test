from utils.api_helper.ucenter_api import ucenter_api
import os


def login():
    json_data = {
        "userPhone": os.getenv('ACCOUNT'),
        "verifyCode": os.getenv('VERIFYCODE'),
        "clientTypeId":1,
        "loginTypeId":1,
        "platformId":2
    }
    return ucenter_api.post("/access/login", json=json_data)
