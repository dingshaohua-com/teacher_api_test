import os
from utils.api_helper.api_client import ApiClient
from utils import context
from utils.common import get_teacher_type, get_selected_org

# 实例化
ucenter_api = ApiClient(host=os.getenv('HOST'), base_url=os.getenv('UCENTER_BASE_URL'))

# 定义请求拦截器：注入 Token
def request_interceptor(url, kwargs):
    # 如果 context 里存的是一个对象，可以这样拿
    token = getattr(context, 'token', None)
    if token:
        headers = kwargs.setdefault('headers', {}) # 如果有，就拿来用；如果没有，就初始化一个
        headers['Authorization'] = f"Bearer {token}"
    return url, kwargs

# 定义响应拦截器：自动解析 JSON 或错误处理
def response_interceptor(response):
    if response.status_code == 200:
        res=response.json().get('data')
        if '/login' in response.request.url:
            token = res.get('token')
            if token:
                context.token=token
                context.user=res.get('user')
                teacher_type = get_teacher_type(context.user['userTypes'])
                context.organization = get_selected_org(teacher_type['organizationList'])
                print(f'用户选择了：{context.organization['organizationName']}')
            else:
                raise Exception('登录异常')
        return res
    else:
        print(f"ERROR: 请求错误 {response.status_code}")
        return response

# 注册拦截器
ucenter_api.interceptors['request'].append(request_interceptor)
ucenter_api.interceptors['response'].append(response_interceptor)
