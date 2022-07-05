# -*- coding:utf-8 -*-
class Student:

    def __init__(self, id, name, phone, score, wx='', qq=''):
        self.id = id
        self.name = name
        self.phone = phone
        self.score = score
        self.wx = wx
        self.qq = qq

    def __str__(self):
        return f'{self.id},{self.name},{self.phone},{self.score},{self.wx},{self.qq}'

    def show_name(self):
        return self.name

    def show_phone(self):
        return self.phone

    def show_score(self):
        return self.score

    def show_wx(self):
        return self.wx

    def show_qq(self):
        return self.qq

    def set_name(self, name):
        self.name = name

    def set_phone(self, phone):
        self.phone = phone

    def set_score(self, score):
        self.score = score

    def set_wx(self, wx):
        self.wx = wx

    def set_qq(self, qq):
        self.qq = qq

