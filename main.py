import json
from dotenv import load_dotenv
load_dotenv('.env.test2')
from service.auth import login
from service.user import get_teacher_detail
from mdutils.mdutils import MdUtils

login()
teacher_detail=get_teacher_detail()

def save_as_md(json_temp):
    mdFile = MdUtils(file_name='老师详情')
    mdFile.new_header(level=1, title='老师详情')
    mdFile.insert_code(json_temp, language='json')
# 在传入之前，先用 json 库把字典“序列化”为字符串
json_str = json.dumps(teacher_detail, indent=4, ensure_ascii=False)
save_as_md(json_str)