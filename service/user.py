from utils.api.teacher_api import teacher_api

def get_teacher_detail():
    return teacher_api.get("/teacher/detail")
