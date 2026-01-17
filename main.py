
from dotenv import load_dotenv
from utils.common import save_as_md
load_dotenv('.env.test2')

from service.auth import login
from service.user import get_teacher_detail
from service.task import get_report_list

login()
teacher_detail=get_teacher_detail()
save_as_md('老师详情',teacher_detail)


params = {
    "taskType": 0,
    "subject": 6,
    "groupId": 0,
    "startDate": "2026-01-11",
    "endDate": "2026-01-17",
    "groupType": 2,
    "keyword": "",
    "page": 1,
    "pageSize": 30
}
report_list=get_report_list(params)
save_as_md('报告列表',report_list)




