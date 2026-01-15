
# 从用户登录返回的职业列表中获取老师职业信息(任职那些学校)
def get_teacher_type(user_types):
    teacher_type = {}
    teacher_typeId=2
    for user_type in user_types:
        if user_type['userTypeId'] == teacher_typeId:
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