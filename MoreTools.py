#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/12/10 下午 16:23
# @Author   : Alan_luo
# @Site     :
# @File     : MoreTools.py
# @Purpose  :
# @Software : PyCharm
# @Copyright:   (c)  2019
# @Licence  :     <your licence>


from tkinter import *
from tkinter import ttk

MyGUI = Tk(className="多开工具")
MyGUI.geometry("240x480")
# 选择浏览器类型
browser = ttk.Combobox()
browser_text = Message(text='浏览器')
browser['values'] = ('谷歌浏览器', 'QQ浏览器', '火狐浏览器')
browser.grid(column=2, row=1)   # 设置其在界面中出现的位置 column代表列 row 代表行
browser_text.grid(column=1, row=1)
browser.current(0)  # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
# 选择游戏
games = ttk.Combobox()
games['values'] = ('血战到底', '斗地主')
games.grid(column=2, row=2)   # 设置其在界面中出现的位置 column代表列 row 代表行
games.current(0)  # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
# 运行按钮
run = Button(text='运行', command=None)
run.grid(column=2, row=3)

mainloop()
