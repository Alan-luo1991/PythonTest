#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# def jiecheng(n):
#     if n == 1:
#         return 1
#     else:
#         return n*jiecheng(n-1)
# print(jiecheng(3))


def fib(x):
    if x == 1 or x == 2:
        return x
    # 当x > 2时，开始递归调用fib()函数:
    return fib(x - 1) + fib(x - 2)

print(fib(50))  # 打印结果为:8
