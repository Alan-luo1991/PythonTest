"""
寻找两个有序数组的中位数
"""
import time


# 暴力解法


class Solution:

    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        for i in nums2:
            nums1.append(i)
            nums1.sort()
        if len(nums1) % 2 == 0:
            s = (nums1[int(len(nums1) / 2 - 1)] + nums1[int(len(nums1) / 2)]) / 2
        else:
            s = nums1[int((len(nums1) - 1) / 2)]
        print(s)


s = Solution()
nums1 = [1, 2, 4, 6, 8]
nums2 = [3]
s.findMedianSortedArrays(nums1, nums2)
print("当前耗时为：%ss" % time.clock())
