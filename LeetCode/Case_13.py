#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        dict_roman = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        a = 0
        x, y, z = 0, 0, 0
        lenth = len(s)
        for i in range(0, lenth):
            a = a + dict_roman[s[i]]
            # print(dict_roman[s[i]])
            try:
                if s[i] == 'I' and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                    x += 1
                elif s[i] == 'X' and (s[i + 1] == 'L' or s[i + 1] == 'C'):
                    y += 1
                elif s[i] == 'C' and (s[i + 1] == 'D' or s[i + 1] == 'M'):
                    z += 1
                else:
                    continue
            except:
                pass
        print(a, x, y, z)
        return a - x * 2 - y * 20 - z * 200


s = Solution()
print(s.romanToInt("MCMXCIV"))
