#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isValid(self, s: str) -> bool:
        bracket = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                bracket.append(i)
            elif len(bracket) == 0:
                return False
            elif i == ')' and bracket[-1] == '(':
                bracket = bracket[:-1]
            elif i == ']' and bracket[-1] == '[':
                bracket = bracket[:-1]
            elif i == '}' and bracket[-1] == '{':
                bracket = bracket[:-1]
            else:
                return False
        return len(bracket) == 0


# class Solution:
#     def isValid(self, s: str) -> bool:
#         dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
#         stack = ['?']
#         for c in s:
#             if c in dic: stack.append(c)
#             elif dic[stack.pop()] != c: return False
#         return len(stack) == 1


# class Solution:
#     def isValid(self, s: str) -> bool:
#         bracket = []
#         left_num = 0
#         right_num = len(s)-1
#         while left_num < right_num:
#             bracket.append(s[left_num])
#             if (bracket[0] == '(' and s[right_num] == ')') or (bracket[0] == '[' and s[right_num] == ']') or (bracket[0] == '{' and s[right_num] == '}'):
#                 bracket = []
#                 left_num += 1
#                 right_num -= 1
#             else:
#                 left_num += 1
#                 right_num -= 1
#         return len(bracket) == 0


# class Solution_1(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         if s == '':
#             return True
#         while True:
#             length = len(s)
#             bracket = []
#             for index, i in enumerate(s):
#                 try:
#                     if length % 2 == 1:
#                         return False
#                     if (i == "(" and s[index + 1] == ")") or (i == "[" and s[index + 1] == "]") or (i == "{" and s[index + 1] == "}"):
#                         s = s[:index] + s[index+2:]
#                         break
#                 except:
#                     pass
#
#             if s == '':
#                 return True
#             if length == len(s):
#                 return False


f = Solution()
s = "[({(())}[()])]"
a = f.isValid(s)
print(a)