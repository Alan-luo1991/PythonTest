#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
字符串数组中的最长公共前缀
"""


class Solution:
    def longestCommonPrefix(self, strs):
        # list_num = 0
        # list_lenth = len(strs)  # 获取列表长度
        common_str = ''
        for i in zip(*strs):
            if len(set(i)) == 1:
                common_str += i[0]
            else:
                break

        return common_str


s = Solution()
strs = ["aca", "cba"]
a = s.longestCommonPrefix(strs)
print(a)
