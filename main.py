from dotenv import load_dotenv
load_dotenv('.env.test2')
from service.auth import login

res=login()
print(res)