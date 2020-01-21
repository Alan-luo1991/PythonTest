#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2019/08/01 下午 15:10
# @Author   : Alanluo
# @Site     :
# @File     : study_class.py
# @Purpose  :
# @Software : PyCharm
# @Copyright: (c)  2019
# @Licence  : <your licence>
import sys,collections

class Person(object):
    """
    返回一个具有名称，年龄的Person对象
    """
    def __init__(self, name, year):
        """
        初始化属性
        :param name:名称
        :param yaer: 年龄
        """
        self.name = name
        self.year = year
    def get_details(self):
        """
        返回包含人的名称和年龄的字符串
        :return:
        """
        return self.name, self.year

    def get_grade(self):
        """
        :return:
        """
        return 0

class Student(Person):
    """
    返回Student对象，具有名称 ，年龄，学校
    """
    def __init__(self, name, year, school, grade):
        Person.__init__(self, name, year)
        self.school = school
        self.grade = grade
    def get_details(self):
        """
        返回包含学生具体信息的字符串
        :return:
        """
        return "姓名：{} 年龄：{} 学校：{}".format(self.name, self.year, self.school)
    def get_grade(self):
        common = collections.Counter(self.grade).most_common(4)
        n1 = 0
        n2 = 0
        for item in common:
            if item[0] != "D":
                n1 += item[1]
            else:
                n2 += item[1]
        return "Pass:{}, Fail:{}".format(n1, n2)


class Teacher(Person):
    """
    返回Teacher对象，具有年龄，名称，科目
    """
    def __init__(self, name, year, subject, grade):
        Person.__init__(self, name, year)
        self.subject = subject
        self.grade = grade
    def get_details(self):
        """
        返回包含教师具体信息的字符串
        :return:
        """
        return "姓名：{} 年龄：{} 科目：{}".format(self.name, self.year, self.subject)
    def get_grade(self):
        s = []
        common = collections.Counter(self.grade).most_common(4)
        for i, j in common:
            s.append("{}:{}".format(i, j))
        return ",".join(s)

person_1 = Person("张三", "20")
student_1 = Student("李四", "16", "山东蓝翔技术学院","AAAAAAAAA")
teacher_1 = Teacher("王五", "35", "挖掘机专业","AaaaaaaSDQWEASD")
student_2 = Student("","","","AAABBBCCDDDD")

# print(person_1.get_details())
# print(student_1.get_details())
# print(teacher_1.get_details())
print(student_1.get_grade())
# print(teacher_1.get_grade())



