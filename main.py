
from dotenv import load_dotenv
from utils.common import save_as_md
load_dotenv('.env.test2')

from service.auth import login
from service.user import get_teacher_detail
from service.task import get_report_list

login()
teacher_detail=get_teacher_detail()
save_as_md('老师详情',teacher_detail)





