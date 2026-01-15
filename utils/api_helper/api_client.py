import urllib3
import requests
from urllib.parse import urljoin

# Charles 代理设置
# 1. 禁用 SSL 警告（针对 Charles 代理）
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'http://127.0.0.1:8888'
}

class ApiClient(requests.Session):
    def __init__(self, host=None, base_url=None):
        super().__init__()
        self.host = host.rstrip('/')
        self.base_url = base_url.rstrip('/')

        # 模拟 axios 的拦截器结构
        self.interceptors = {
            'request': [],
            'response': []
        }

    def request(self, method, url, **kwargs):
        # 1. 处理 url
        if self.host and not url.startswith(('http://', 'https://')):
            url = urljoin(self.host, self.base_url+url)

        # 2. 执行请求拦截器 (Request Interceptors)：可以在这里统一添加 Token、修改 Headers 等
        for interceptor in self.interceptors['request']:
            url, kwargs = interceptor(url, kwargs)

        # 3. 发送真实请求
        # response = super().request(method, url, **kwargs)
        response = super().request(method, url, proxies=proxies, verify=False, **kwargs)   # 禁用 SSL 验证（因为用了 Charles 证书）

        # 4. 执行响应拦截器 (Response Interceptors)：可以在这里统一处理 401 状态码、提取 data 字段等
        for interceptor in self.interceptors['response']:
            response = interceptor(response)

        return response

