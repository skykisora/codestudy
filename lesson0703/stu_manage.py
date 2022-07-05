# -*- coding:utf-8 -*-
from lesson0703.student import Student
from lesson0703.data_operate import DataOperate


def run():
    data = DataOperate()
    stu_dict = data.read_info()
    print("欢迎使用学员管理系统")
    while True:
        select_type = int(input("请选择业务类型：1：新增 2：修改 3：查询 4：删除 5：退出 >> "))
        if select_type == 1:
            id = input("请输入学员id：")
            name = input("请输入学员姓名：")
            phone = input("请输入学员手机号：")
            score = input("请输入学员成绩：")
            stu = Student(id, name, phone, score)
            stu_dict[stu.id] = stu
            data.write_info(stu_dict)
        elif select_type == 2:
            
            print("2没有写")
        elif select_type == 3:
            print("3没有写")
        elif select_type == 4:
            print("4没有写")
        elif select_type == 5:
            print("退出学员管理系统")
            break
        elif select_type not in [1,2,3,4,5]:
            print("超出业务范围，即将关闭系统")
            break


if __name__ == '__main__':
    run()
