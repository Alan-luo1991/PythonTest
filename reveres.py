#!/usr/bin/env python
# -*- coding: utf-8 -*-


a = '   hello!        world!     '
b = a.strip()
print(b.split())
c = ' '.join(b.split())
s1 = c.split(' ')
i, j = 0, len(s1) - 1
while i < j:
    s1[i], s1[j] = s1[j], s1[i]
    i += 1
    j -= 1
d = ' '.join(s1)



# class Reveres:
#
#     def __init__(self,s =str):
#         self.s = s  # 初始化字符串
#
#     def killkg(self, s):
#         return ' '.join(s.strip().split())  # 去字符串空格
#
#     def res_danci(self,s):
#         s1 = s.split()  # 单词分成元素
#         i, j = 0, len(s1) - 1
#         while i < j:
#             s1[i], s1[j] = s1[j], s1[i]
#             i += 1
#             j -= 1
#         return ' '.join(s1)
#
#
# if __name__ == '__main__':
#     a = '   the sky    is     blue     '
#     string = Reveres()
#     print(string.res_danci(string.killkg(a)))
