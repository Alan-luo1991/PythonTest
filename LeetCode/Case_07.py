#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        while x % 10 == 0:
            x = x / 10
            x = int(x)
        b = str(x)
        ls = []
        lenth = len(ls) - 1
        for i in b:
            if i == '-':
                continue
            else:
                ls += i
        start = 0
        end = len(ls) - 1
        while start < end:
            ls[start], ls[end] = ls[end], ls[start]
            start += 1
            end -= 1

        if b[0] == '-':
            ls.insert(0, '-')

        s = ''.join(ls)
        if int(s) > pow(2,31) - 1 or int(s) <pow(-2,31):
            return 0
        return int(s)















# a = -100990000
# while a % 10 ==0:
#     a = a / 10
#     a = int(a)
# b = str(a)
# ls = []
# lenth = len(ls)
# for i in b:
#     if i == '-':
#         continue
#     else:
#         ls += i
# start = 0
# end = len(ls) - 1
# while start < end:
#     ls[start], ls[end] = ls[end], ls[start]
#     start += 1
#     end -= 1
#
# if b[0] == '-':
#     ls.insert(0, '-')
#
# s = ''.join(ls)
# print(int(s))