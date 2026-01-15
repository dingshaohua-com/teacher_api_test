from utils.api_helper.common_api import common_api
import os


def login():
    data = {
        "userPhone": os.getenv('ACCOUNT'),
        "verifyCode": os.getenv('VERIFYCODE'),
        "clientTypeId":1,
        "loginTypeId":1,
        "platformId":2
    }
    return common_api.post("/access/login", json=data)
