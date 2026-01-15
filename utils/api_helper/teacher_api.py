import os
from utils.api_helper.api_client import ApiClient
from utils import context
from utils.common import get_teacher_type, get_selected_org

# 实例化
teacher_api = ApiClient(host=os.getenv('HOST'), base_url=os.getenv('TEACHER_BASE_URL'))

# 定义请求拦截器：注入 Token
def request_interceptor(url, kwargs):
    # kwargs.setdefault('headers', {})
    # kwargs['headers']['Authorization'] = 'Bearer YOUR_TOKEN'
    # print(f"DEBUG: 发送请求到 {url}")

    token = getattr(context, 'token', None)

    if token:
        headers = kwargs.setdefault('headers', {})  # 如果有，就拿来用；如果没有，就初始化一个
        headers['Authorization'] = f"Bearer {token}"
        headers['organizationid'] = str(context.organization['organizationId'])
    return url, kwargs

# 定义响应拦截器：自动解析 JSON 或错误处理
def response_interceptor(response):
    if response.status_code == 200:
        res=response.json().get('data')
        return res
    else:
        print(f"ERROR: 请求错误 {response.status_code}")
        return response


# 注册拦截器
teacher_api.interceptors['request'].append(request_interceptor)
teacher_api.interceptors['response'].append(response_interceptor)