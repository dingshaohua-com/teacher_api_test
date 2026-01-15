import os
from utils.api_helper.api_client import ApiClient

# 实例化
common_api = ApiClient(host=os.getenv('HOST'), base_url=os.getenv('BASE_URL'))

# 定义请求拦截器：注入 Token
def auth_interceptor(url, kwargs):
    # kwargs.setdefault('headers', {})
    # kwargs['headers']['Authorization'] = 'Bearer YOUR_TOKEN'
    print(f"DEBUG: 发送请求到 {url}")
    return url, kwargs

# 定义响应拦截器：自动解析 JSON 或错误处理
def logging_interceptor(response):
    # print(response.json().get('data'))
    if response.status_code == 200:
        res=response.json().get('data')
        token = res.get('token')
        if token:
            common_api.auth = token
        return res
    else:
        print(f"ERROR: 请求错误 {response.status_code}")
        return response


# 注册拦截器
common_api.interceptors['request'].append(auth_interceptor)
common_api.interceptors['response'].append(logging_interceptor)