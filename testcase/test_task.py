from service.task import get_report_list

def test_get_report_list():
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

