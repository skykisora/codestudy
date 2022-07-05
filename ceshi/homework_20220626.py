# -*- coding:utf-8 -*-
# 从控制台分别输入年、月、日,通过计算打印出你输入的日期，是该年份的第多少天 比如 2022年2月26 ，打印出2022年2月26日是2022年的第57天
def get_sum_days():
    year = int(input("请输入年："))
    month = int(input("请输入月："))
    day = int(input("请输入日："))
    sum_days = 0
    for i in range(1, month):
        if i in [1,3,5,7,8,10,12]:
            sum_days += 31
        elif i in [4,6,9,11]:
            sum_days += 30
        elif i == 2:
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                sum_days += 29
            else:
                sum_days += 28
    sum_days += day
    return f'{year}年{month}月{day}日是{year}年的第{sum_days}天'


print(get_sum_days())

# 统计下述不及格的学员数量，并打印出不及格的学员姓名
list1 = [{'name':'张三','score':45},{'name':'李四','score':67},{'name':'王五','score':80}]


# 对l列表进行操作，把每个字符串变成小写字母，数字和None保持原样，然后重新返回一个新列表
list2 = ['Hello', 'World', 18, 'Apple', None]



# 按照课件上的学生类图片实现代码，实例化两个对象，每个对象都打印出自己的基本信息


