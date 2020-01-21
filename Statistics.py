#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jieba


class Statistics:

    def __init__(self, dict_1=None):
        """

        :type dict_1: object
        """
        if dict_1 is None:
            dict_1 = {}
        self.dict_1 = dict_1   # 初始化参数

    def opentxt(self, url):
        self.url = url   # 初始化参数地址
        with open(url, 'r', encoding='utf-8') as f:    # 读 取文本
            fenci = jieba.lcut(str(f.read()), cut_all=False)  # 用结巴分词转化成列表
        return fenci

    def initdict(self, fenci):
        self.fenci = fenci
        dict_1 = self.dict_1   # 继承参数
        for i in fenci:
            if len(i) > 1:      # 把长度大于1的单词和数量存入数组
                dict_1[i] = dict_1.get(i, 0) + 1
        dict_2 = sorted(dict_1, key=dict_1.__getitem__, reverse=True) # 针对数组中的值进行排序赋值给新的数组
        return dict_2

    def Topten(self, dict_2):
        dict_1 = self.dict_1  # 继承参数
        a = 1
        for i in dict_2:
            if a < 11:     # 取前10
                print("NO_{} {} {}".format(a, i, dict_1[i]))
                a += 1
        return


a = Statistics()
b = a.opentxt('D:\Mytest\恶魔法则.txt')
c = a.initdict(b)
d = a.Topten(c)


# dict_1 = {}
# a = 1
# with open('D:\Mytest\恶魔法则.txt', 'r',encoding='utf-8') as f:
#     fenci = jieba.lcut(str(f.read()), cut_all=False)
# for i in fenci:
#     if len(i) > 1:
#         dict_1[i] = dict_1.get(i, 0) + 1
# dict_2 = sorted(dict_1, key=dict_1.__getitem__, reverse=True)
# for i in dict_2:
#     if a < 11:
#         print("NO_{} {} {}".format(a,i,dict_1[i]))
#         a += 1
