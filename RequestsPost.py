import sys,os,re,collections
# from functools import reduce
# print(reduce(lambda x,y: x+[sum(x[-2:])],range(20-2), [1,1]))
# for i in range(10):
#     print(i)
# list = [0, 1, 'python']
# print(list[1])
# while True:
#     n = str(input("请输入你想要输入的数字： "))
#     if n < '0':
#         continue
#     elif n == '0':
#         break
#     else:
#         pass
#     print(n)
# print("再见")
#!/usr/bin/env python3
from typing import List

"""
创建一个列表
squares 正方形 
"""
# squares = []
# for x in range(10):
#     squares.append(x**2)
# print(squares)
# squares =[x ** 2 for x in range(11)]
# print(squares)
# squares = list(map(lambda x: x**2, range(10)))
# print(squares)
"""
创建一个学生成绩查询系统，
要求下输学生数量，以及各个学生物理，数学，历史成绩，
总成绩小于120，输出failed,否则passed
"""
# stu_number = int(input("请输入你想存入的学生数量： "))
# # stu_data = {} #创建学生信息字典
# # subjects = ("物理", "数学", "历史") #创建所需要存入的科目名称 元祖
# # for name in range(0, stu_number):
# #     stu_name = str(input("请输入学生({})姓名： ".format(name + 1)))
# #     marks = []  # 创建一个列表，存放学生成绩
# #     for mark in subjects:
# #         marks.append(int(input("请输入学生成绩{}：".format(mark))))
# #     stu_data[stu_name] = marks #在学生信息字典里面 存入key:学生名字 value:学生成绩
# # for name, mask in stu_data.items(): #用学生名称和成绩去遍历学生信息字典
# #     total = sum(mask)
# #     print(total)
# #     print("{}的总成绩是{}".format(name, total))
# #     if total < 120:
# #         print(name,"没有及格，还需要再努力!")
# #     else:
# #         print(name,"恭喜你，你可以度过一个愉快的假期!")
"""
高阶函数练习
"""
# def high(l):
#     return [sum_01(i) for i in l]
# def sum(h,l):
#     return h(l)
# def sum_01(x):
#     return x * x
# lst = [1, 2]
# print(list(sum(high, lst)))
"""
打开某个文件，并提取数字
"""
# with open("d:/Mytest/QA-TOOL/test_11.txt", "r") as string:
#     line = str(string.readlines())
#     print(re.findall("\d+", line))
"""
冒泡排序
# """
# list = [5, 4, 11, 6, 9]
# for i in range(0, len(list) - 1):
#     for f in  range(0, len(list) -1 -i):
#         if list[i] > list[i + 1]:
#             temp = ""
#             temp = list[i]
# print(temp)
"""
输入分钟数，转化为小时和分钟
"""
# def hours(minute):
#     if minute < 0:
#         print("请输入正确的时间！")
#     else:
#         print("{}小时 {}分钟".format(int(minute / 60), minute % 60))
# try:
#     hours(int(sys.argv[1]))
# except:
#     print("请输入正确的时间！")

"""
两数之和
"""
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for num_1, num_2 in nums:
# nums = [2, 4, 7, 15]
# target = 9
# count = 0
# # 用字典模拟哈希求解
# hashmap ={}
# for key, value in enumerate(nums):
#     if hashmap.get(target - value) is not None:
#          print(key, hashmap.get(target - value))
#     hashmap[value] = key
#     print(hashmap)


# 暴力解法 enumerate方法返回序列下标和值
# for i, a in enumerate(nums):
#     for j, b in enumerate(nums):
#         count += 1
#         if a + b == target and i < j:
#             print(i, j)
#         else:
#             print(count)

# 暴力解法 range值返回序列长度下标值
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         count += 1
#         if nums[i] + nums[j] == target and i < j:
#             print(i, j)
#             print(count)


# for idx, item in enumerate(nums):
#     print(idx)
#     #count +=1
#     #if count % 10 == 0:
#     if (idx+1) % 10 == 0:
#         print('did ten')
"""
统计序列相同元素
"""
# a = 'sadsadsaddasda'
# b = set(a)
# _k = {}
# print(b)
# for i in b:
#     _k[i] = a.count(i)
# print(_k)
# print(sorted(_k))
# print(collections.Counter(a).most_common(4))
"""

以%格式化输出

"""
# a = "abcdefg"
# b = len(a)
# print(a[::-1])

"""
统计字符串
"""
#
# a = "ASDASDASDADDffeefggfhhhhh"
# common = collections.Counter(a).most_common(8)
# n1 = 0
# n2 = 0
# for item in common:
#     if item[0] != "D":
#         n1 += item[1]
#     else:
#         n2 += item[1]
# print("Pass:{}, Fail:{}".format(n1, n2))


aList = ['Google', 'Runoob', 'Taobao', 'Facebook']

aList.sort()
print("List : ", aList)
