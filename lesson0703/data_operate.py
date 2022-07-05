# -*- coding:utf-8 -*-
from lesson0703.student import Student


class DataOperate:
    def __init__(self):
        self.file_path = r'./student.txt'

    def read_info(self):
        stu_info = {}
        with open(file=self.file_path, mode='r', encoding='UTF-8') as f:
            lines = f.readlines()
            print(type(lines))  # '1,万五,1235555,90,wx39939,2399999\n'
            for line in lines:
                value = line.split(',')
                id = value[0]
                name = value[1]
                phone = value[2]
                score = value[3]
                wx = value[4]
                qq = value[5].strip()
                stu = Student(id, name, phone, score, wx, qq)
                stu_info[id] = stu
        return stu_info

    def write_info(self, stu_dict):
        with open(file=self.file_path, mode='w', encoding='utf-8') as f:
            for stu in stu_dict.values():
                f.write(str(stu))
                f.write("\n")


if __name__ == '__main__':
    s = DataOperate()
    stu = s.read_info()
    s.file_path = r'./ceshi.txt'
    s.write_info(stu)