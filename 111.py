#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
冒泡
"""


class Bubble:
    def sort_list(self, nums: list[int]) -> list[int]:
        length = len(nums)
        for i in range(length - 1):
            p = length - 1
            for j in range(p):
                if nums[p - 1] > nums[p]:
                    nums[p], nums[p - 1] = nums[p - 1], nums[p]
                p -= 1
        return nums


# a = [9, 2, 1, 3, 6, 2, 4, 5]
#
# length = len(a) - 1
# b = 0
# while b < len(a):
#     if a[length - 1] > a[length]:
#         a[length], a[length - 1] = a[length - 1], a[length]
#     elif length == 1:
#         length = len(a) - 1
#         b += 1
#     else:
#         length -= 1
# print(a)


# left = 0
# right = len(a)-1
# while True:
#     if a[left] > a[right]:
#         a[left], a[right] = a[right], a[left]
#     elif left == right:
#         left = 0
#         right -= 1
#     elif right == 1:
#         break
#     else:
#         left += 1
# print(a)