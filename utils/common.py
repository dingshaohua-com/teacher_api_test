import os
import json
from mdutils import MdUtils

# 从用户登录返回的职业列表中获取老师职业信息(任职那些学校)
def get_teacher_type(user_types):
    teacher_type = {}
    teacher_type_id=2
    for user_type in user_types:
        if user_type['userTypeId'] == teacher_type_id:
            teacher_type=user_type
    return teacher_type

def get_selected_org(org_list):
    # 1. 打印选项
    for i, org in enumerate(org_list):
        print(f"[{i}] {org['organizationName']}")

    # 2. 获取输入（加个简单的异常处理防止输错崩溃）
    try:
        idx = int(input("\n请选择学校序号: "))
        return org_list[idx]
    except (ValueError, IndexError):
        print("❌ 输入无效，未选择任何学校")
        return None

def save_as_md(title,json_temp):
    file_path = os.path.join("report", title) # 在传入之前，先用 json 库把字典“序列化”为字符串
    json_str = json.dumps(json_temp, indent=4, ensure_ascii=False)
    md_file = MdUtils(file_name=file_path)
    md_file.new_header(level=1, title=title)
    md_file.insert_code(json_str, language='json')
    md_file.create_md_file()