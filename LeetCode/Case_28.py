#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1
"""

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         return haystack.find(needle)

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if needle == '':
#             return 0
#         for i in range(len(haystack)):
#             if haystack[i:i + len(needle)] == needle:
#                 return i
#         return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        elif needle in haystack:
            return haystack.index(needle)
        else:
            return -1


a = Solution()
haystack = "asdasd"
needle = "qw"
b = a.strStr(haystack, needle)
print(b)