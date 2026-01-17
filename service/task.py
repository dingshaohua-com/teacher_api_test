from utils.api.teacher_api import teacher_api

def get_report_list(params):
    return teacher_api.get("/task/report/list",data=params)

