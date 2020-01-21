#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/12/11 9:21
# @Author   : StephenZ
# @Site     : 
# @File     : make_card.py
# @Purpose  :
# @Software : PyCharm
# @Copyright:   (c) StephenZ 2019
# @Licence  :     <@2019>

from tkinter import *
from logzero import logger
import logzero, logging

logzero.loglevel(logging.DEBUG)


class Card(object):
    def __init__(self):
        self.card_dic = dict(方块A='0x01,', 方块2='0x02,', 方块3='0x03,', 方块4='0x04,', 方块5='0x05,', 方块6='0x06,', 方块7='0x07,',
                             方块8='0x08,', 方块9='0x09,', 方块10='0x0A,', 方块J='0x0B,', 方块Q='0x0C,', 方块K='0x0D,', 梅花A='0x11,',
                             梅花2='0x12,', 梅花3='0x13,', 梅花4='0x14,', 梅花5='0x15,', 梅花6='0x16,', 梅花7='0x17,', 梅花8='0x18,',
                             梅花9='0x19,', 梅花10='0x1A,', 梅花J='0x1B,', 梅花Q='0x1C,', 梅花K='0x1D,', 红桃A='0x21,', 红桃2='0x22,',
                             红桃3='0x23,', 红桃4='0x24,', 红桃5='0x25,', 红桃6='0x26,', 红桃7='0x27,', 红桃8='0x28,', 红桃9='0x29,',
                             红桃10='0x2A,', 红桃J='0x2B,', 红桃Q='0x2C,', 红桃K='0x2D,', 黑桃A='0x31,', 黑桃2='0x32,', 黑桃3='0x33,',
                             黑桃4='0x34,', 黑桃5='0x35,', 黑桃6='0x36,', 黑桃7='0x37,', 黑桃8='0x38,', 黑桃9='0x39,', 黑桃10='0x3A,',
                             黑桃J='0x3B,', 黑桃Q='0x3C,', 黑桃K='0x3D,', 小王='0x4E,', 大王='0x4F,')

    def create(self):
        window = Tk()
        screen_height = window.winfo_screenheight()  # 获取屏幕分辨率
        screen_width = window.winfo_screenwidth()
        window_width = 610
        window_height = 400

        # logger.debug("height = %s, width = %s" % (screen_height, screen_width))
        window.title("斗地主配牌")
        window.geometry("%sx%s+%s+%s" % (
            window_width, window_height, int((screen_width - window_width) / 2),
            int((screen_height - window_height) / 2)))
        output = Label(window, text="已输入：", bg="gray", height=2, width=100, font=('Arial', 12))
        output.pack(side="bottom")

        frame_buttons = Frame(window)
        frame_buttons.pack()

        for index, button in enumerate(self.card_dic.keys()):
            # new_button = Button(frame_buttons, text=button, activebackground="green", bd=3, padx=2,
            #                     command=lambda name=button: output.config(
            #                         text=(output.cget("text") + self.card_dic[name])))

            new_button = Button(frame_buttons, text=button, activebackground="green", bd=3, padx=2,
                                command=lambda name=button: output.config(
                                    text=(output.cget("text") + name + ",")))

            new_button.grid(row=int(index / 13 + 1), column=index % 13 + 1)

        def confirm_fun():
            a = output.cget("text")
            output.config(text="已输入:")
            input_list = a[4:-1].split(",")
            need_str = "".join(self.card_dic[x] for x in input_list)
            logger.debug("need_str = %s" % need_str)
            #  这里是发送a的post函数

        def cancel_fun():
            output.config(text="已输入:")
            logger.debug(output.cget("text"))

        confirm = Button(window, text="确定", command=confirm_fun)
        confirm.pack()

        cancel = Button(window, text="取消", command=cancel_fun)
        cancel.pack()

        window.mainloop()


c = Card()
c.create()
