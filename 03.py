#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time


class GiveChange:
    def min_set(self, coins: list, amount: int) -> int:
        # monetary_value = [25, 21, 10, 5, 1]
        lenth = len(coins)     # 计算出列表长度
        b = amount    # 把目标值保存 留做计算使用
        a = 0   # 初始化组合目标值的计数
        set = []    # 初始化列表，用于存放所有能够组合目标值的计数
        for y in range(lenth):  # 用于控制循环次数，且用于排除每次计算中已经计算过的最大面值货币
            amount = b    # 重新赋值用于运算的目标值
            for j in range(y, lenth):   # 循环查找能够组合目标值的货币面值
                if amount // coins[j] > 0:
                    a += amount // coins[j]  # 目标值除以货币面值后的商 用于计数
                    amount = amount % coins[j]     # 取余数，用于之后货币面值计算商
                if lenth == 1 and amount != 0:
                    return -1
                if amount % coins[j] == 0:   # 如果目标值能够整除货币面值
                    a += amount // coins[j]  # 把整除的商用于计数
            set.append(a)   # 把每次计数结果存放进列表中
            a = 0   # 重置循环计数
        return min(set)  # 返回最小计数值


a = GiveChange()
coins = [100, 50, 25, 21, 10, 5, 1]
print(a.min_set(coins, 6249))
print(time.perf_counter())