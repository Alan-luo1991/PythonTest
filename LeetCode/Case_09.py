#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        mystr = str(x)
        if mystr == ''.join(reversed(mystr)):
            return True
        else:
            return False


a = Solution()
print(a.isPalindrome(10))


x = 12321
m, n = x, 0

while m:
    n = n * 10 + m % 10
    m = m // 10
    print(n,m)
