#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql




def update_sql():
    change_num = 0
    db = pymysql.connect('10.0.0.32', 'root', '123456', 'game', 3306)
    cursor = db.cursor()
    sql = "UPDATE xuezhandaodi SET exchange={change_num} WHERE id between 1 and 5".format(change_num=change_num)
    cursor.execute(sql)
    db.commit()
    db.close()


update_sql()


# dict_ddz = dict(方块A='0x01,', 方块2='0x02,', 方块3='0x03,', 方块4='0x04,', 方块5='0x05,', 方块6='0x06,', 方块7='0x07,',
#                 方块8='0x08,', 方块9='0x09,', 方块10='0x0A,', 方块J='0x0B,', 方块Q='0x0C,', 方块K='0x0D,', 梅花A='0x11,',
#                 梅花2='0x12,', 梅花3='0x13,', 梅花4='0x14,', 梅花5='0x15,', 梅花6='0x16,', 梅花7='0x17,', 梅花8='0x18,',
#                 梅花9='0x19,', 梅花10='0x1A,', 梅花J='0x1B,', 梅花Q='0x1C,', 梅花K='0x1D,', 红桃A='0x21,', 红桃2='0x22,',
#                 红桃3='0x23,', 红桃4='0x24,', 红桃5='0x25,', 红桃6='0x26,', 红桃7='0x27,', 红桃8='0x28,', 红桃9='0x29,',
#                 红桃10='0x2A,', 红桃J='0x2B,', 红桃Q='0x2C,', 红桃K='0x2D,', 黑桃A='0x31,', 黑桃2='0x32,', 黑桃3='0x33,',
#                 黑桃4='0x34,', 黑桃5='0x35,', 黑桃6='0x36,', 黑桃7='0x37,', 黑桃8='0x38,', 黑桃9='0x39,', 黑桃10='0x3A,',
#                 黑桃J='0x3B,', 黑桃Q='0x3C,', 黑桃K='0x3D,', 小王='0x4E,', 大王='0x4F,')
#
# a = 4
# if a > 3:
#     print('相同牌不能超过4张')
# else:
#     print('通过')
#
# buttons = dict_ddz.keys()
# logger.debug(buttons)


# class Desk():
#     def create_buttons(self):
#         root = Tk()
#         t = Text(root, width=20, height=15)
#         t.pack()
#         for index, button in enumerate(buttons):
#             buttonX = Button(text=button, activebackground="green", bd=3, padx=2,
#                              command=lambda name=button: t.insert(END, dict_ddz[name]))
#             buttonX.grid(row=int(index / 13 + 1), column=index % 13 + 1)
#
#     def create_tool(self):
#         MyGUI = Tk(className="斗地主配牌")
#         MyGUI.geometry("610x400")
#         # logger.debug("画布绘制成功")
#         self.create_buttons()
#         # logger.debug("消息循环中")
#         MyGUI.mainloop()
#
#
# d = Desk()
# d.create_tool()
# a = '11,11,11,12,12,12,13,13,13,14,14,14,15'
# b = a[:-1].split(',')
# print(len(a))

# a = Tk()
# Button(a, text='血战麻将配牌', width=9, height=2, bd=4).grid(row=1, column=1, columnspan=2)
# Button(a, text='斗地主配牌', width=9, height=2, bd=4).grid(row=5, column=1, columnspan=2)
# Button(a, text='二人麻将配牌', width=9, height=2, bd=4).grid(row=9, column=1, columnspan=2)
#
# a.mainloop()
