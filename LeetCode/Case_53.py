#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
"""


class Solution:
    def maxSubArray(self, nums: list) -> int:
        maxlist = []
        lenth = len(nums)
        for i in range(lenth):
            for y in range(i, lenth):
                maxlist.append(nums[y] + self.maxSubArray(nums))



a = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(a.maxSubArray(nums))