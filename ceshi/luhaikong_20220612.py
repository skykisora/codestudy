# -*- coding:utf-8 -*-
# @author: sky lu

# 从控制台分别输入年、月、日,通过计算打印出你输入的日期，是该年份的第多少天 比如 2022年2月26 ，打印出2022年2月26日是2022年的第57天
year = int(input("请输入年："))
month = int(input("请输入月："))
data = int(input("请输入日："))
days_all = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
days = data

if 0 < month < 13 and 0 < data < 32:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        # 闰年
        for i in range(1, month):
            days_all[2] = 29
            days = days + days_all[i]
    else:
        for i in range(1, month):
            days = days + days_all[i]
    print(f'{year}年{month}月{data}日是{year}年的第{days}天')
else:
    print("你输入的日期不正确")
