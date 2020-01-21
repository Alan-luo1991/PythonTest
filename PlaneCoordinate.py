#!/usr/bin/env python
# -*- coding: utf-8 -*-


x1, y1, x2, y2 = 100, 0, 0, 1

bian1 = x1 - x2
bian2 = y1 - y2
sum = bian1 * bian1 + bian2 * bian2
distance = sum ** 0.5
print("%.2f" % distance)

# class Plane:
#s
#     def __init__(self):
#         return
#
#     def distance(self, x1, y1, x2, y2):
#         bian1 = x1 - x2
#         bian2 = y1 - y2
#         return (bian1 * bian1 + bian2 * bian2) ** 0.5
#
#
# if __name__ == '__main__':
#     num = Plane()
#     print('%.2f' % num.distance(-10, 0, 0, 1))
