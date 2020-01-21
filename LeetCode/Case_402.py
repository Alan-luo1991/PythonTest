#!/usr/env/bin python3
# -*- coding: utf-8 -*-
"""
给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
注意:
num 的长度小于 10002 且 ≥ k。
num 不会包含任何前导零。
示例 1 :
输入: num = "1432219", k = 3
输出: "1219"
解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
示例 2 :
输入: num = "10200", k = 1
输出: "200"
解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
示例 3 :
输入: num = "10", k = 2
输出: "0"
解释: 从原数字移除所有的数字，剩余为空就是0。
"""


class Solution:
    def removeKdigits(self, num: str, k: int):
        num = list(num)
        if len(num) == k:
            return '0'
        elif k == 1 and '0' not in num:
            b = [0]
            for i in num:
                if int(i) > int(b[-1]):
                    b = []
                    b.append(i)
            c = num.index(b[0])
            num.pop(c)
            num = ''.join(num)
            return num
        elif len(set(num)) == 1 and k != 0:
            num = num[:-k]
            num = ''.join(num)
            return num
        elif k == 0:
            num = ''.join(num)
            print(num)
            return num
        a = 0
        aa = 0
        aaa = 1
        while a < k:
            if num[aa] == num[aaa]:
                aa += 1
                aaa += 1
                continue
            if num[aa] < num[aaa]:
                num.pop(aaa)
            else:
                num.pop(aa)
            a += 1
        if num[0] == '0' and len(num) == 1:
            return '0'
        elif num[0] == '0':
            num = num[1:]
        num = ''.join(num)
        return num


# class Solution:
#     def removeKdigits(self, num: str, k: int):
#         num = list(num)
#         length = len(num)
#         if length <= k:
#             return '0'
#         if k == 1 and int(num[1]) == 0:
#             num = num[2:]
#             if num == []:
#                 return '0'
#             num = ''.join(num)
#             return num
#         elif k == 1 and '0' not in num:
#             b = [0]
#             for i in num:
#                 if int(i) > int(b[-1]):
#                     b = []
#                     b.append(i)
#             c = num.index(b[0])
#             num.pop(c)
#             num = ''.join(num)
#             return num
#         del_num = 0
#         new_num = []
#         new_num.append(num[0])
#         while del_num < length - 1:
#             if int(new_num[-1]) > int(num[del_num + 1]):
#                 new_num.pop(-1)
#                 new_num.append(num[del_num + 1])
#                 k -= 1
#             elif int(num[del_num + 1]) == 0:
#                 new_num.append(num[del_num + 1])
#                 k -= 1
#             else:
#                 new_num.append(num[del_num + 1])
#                 k -= 1
#             del_num += 1
#         if len(num) - len(new_num) < k:
#             a = len(new_num) - (len(num) - k)
#             new_num = new_num[:-a]
#         if len(num) - len(new_num) > k:
#             return ''.join(num[k:])
#         num = ''.join(new_num)
#         return num


# class Solution:
#     def removeKdigits(self, num: str, k: int) -> str:
#         nums = list(num)
#         stack = []
#         for num in nums:
#             while stack and num < stack[-1] and k > 0:
#                 k -= 1
#                 stack.pop()
#             stack.append(num)
#         while k > 0:
#             stack.pop()
#             k -= 1
#
#         res = ''.join(stack).lstrip('0')
#         return res if res != '' else '0'


a = Solution()
num = '43214321'
k = 4
b = a.removeKdigits(num, k)
print(b)