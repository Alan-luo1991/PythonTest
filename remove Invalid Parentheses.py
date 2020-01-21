#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = "(a)())()"


def is_complete(s):
    res = 0
    for x in s:
        if x == '(':
            res += 1
        if x == ')':
            res -= 1
        if res < 0:
            return False
    return res == 0


print(is_complete("()()()"))
