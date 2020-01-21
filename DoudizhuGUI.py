#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/12/09 下午 15:23
# @Author   : Alan_luo
# @Site     :
# @File     : DoudizhuGUI.py
# @Purpose  :
# @Software : PyCharm
# @Copyright:   (c)  2019
# @Licence  :     <your licence>
# @Version  :   V1.3 2019/12/13 10:49
from tkinter import *
from functools import partial
import requests
import tkinter.messagebox
import pymysql

# 初始化选牌窗口

MyGUI = Tk(className="斗地主配牌")
# 自定义窗口大小
MyGUI.geometry("620x450")
# 初始化配牌字典
dict_ddz = dict(方块A='0x01,', 方块2='0x02,', 方块3='0x03,', 方块4='0x04,', 方块5='0x05,', 方块6='0x06,', 方块7='0x07,', 方块8='0x08,',
                方块9='0x09,', 方块10='0x0A,', 方块J='0x0B,', 方块Q='0x0C,', 方块K='0x0D,', 梅花A='0x11,', 梅花2='0x12,', 梅花3='0x13,',
                梅花4='0x14,', 梅花5='0x15,', 梅花6='0x16,', 梅花7='0x17,', 梅花8='0x18,', 梅花9='0x19,', 梅花10='0x1A,', 梅花J='0x1B,',
                梅花Q='0x1C,', 梅花K='0x1D,', 红桃A='0x21,', 红桃2='0x22,', 红桃3='0x23,', 红桃4='0x24,', 红桃5='0x25,', 红桃6='0x26,',
                红桃7='0x27,', 红桃8='0x28,', 红桃9='0x29,', 红桃10='0x2A,', 红桃J='0x2B,', 红桃Q='0x2C,', 红桃K='0x2D,', 黑桃A='0x31,',
                黑桃2='0x32,', 黑桃3='0x33,', 黑桃4='0x34,', 黑桃5='0x35,', 黑桃6='0x36,', 黑桃7='0x37,', 黑桃8='0x38,', 黑桃9='0x39,',
                黑桃10='0x3A,', 黑桃J='0x3B,', 黑桃Q='0x3C,', 黑桃K='0x3D,', 小王='0x4E,', 大王='0x4F,')
# 取出所有的key
name_list = dict_ddz.keys()

# 初始化发送窗口
text_card = Text(MyGUI, width=87, height=5)
text_card.grid(row=0, column=1, columnspan=13)
placeholder_1 = Label(MyGUI, text='说明：目前改金币只支持32测试服').grid(row=6, column=1, columnspan=10)
placeholder_2 = Label(MyGUI, text='').grid(row=7, column=1)
user_text = Label(MyGUI, text='游戏ID：').grid(row=8, column=1)
text_id = Entry(MyGUI, width=30, bd=1)
text_id.grid(row=8, column=1, columnspan=7)
url_test = Label(MyGUI, text='服务器：').grid(row=9, column=1)
text_url = Entry(MyGUI, width=30, bd=1)
text_url.insert(END, 'http://10.0.0.32:6800/config')
text_url.grid(row=9, column=1, columnspan=7)
sql_jb = Entry(MyGUI, width=30, bd=1)
sql_jb.insert(END, '0')
sql_jb.grid(row=10, column=1, columnspan=7)
text_jb = Label(MyGUI, text='金币数：', height=2).grid(row=10, column=1)


# 创建所有扑克按钮
def button_re():
    for button_index, button_name in enumerate(name_list):
        button_card = Button(text=button_name, command=lambda name=button_name: text_card.insert(END, name + ','), bd=3, padx=2)
        button_card.grid(row=int(button_index / 13 + 1), column=button_index % 13 + 1)


# 发送get请求
def gettxt():
    card_str = text_card.get('0.0', 'end')
    card_list = card_str[:-2].split(',')
    card_ID = ''.join(dict_ddz[i] for i in card_list if i != '')
    gameID = str(text_id.get())
    url = str(text_url.get())
    if len(card_ID) == 0:
        tkinter.messagebox.showinfo('提示', '配牌不能为空！')
    elif len(set(card_list)) != len(card_list):
        tkinter.messagebox.showinfo('提示', '每张牌只支持配置1次，请检查配置！')
    elif len(card_ID) != 85:
        tkinter.messagebox.showinfo('提示', '请配置17张牌！')
    elif gameID.isdigit() is False:
        tkinter.messagebox.showinfo('提示', '请输入正确的游戏ID！')
    else:
        try:
            res = requests.get(url + '?user_id=' + gameID + '&doudizhu=' + card_ID[:-1], timeout=(3, 3))
            # print('{}?user_id={}&doudizhu={}'.format(url, gameID, card_ID[:-1]))
            tkinter.messagebox.showinfo('提示', res.text)
        except:
            tkinter.messagebox.showinfo('提示', '请检查游戏ID或者是否连接到内网！')


# 清除配牌
def text_out():
    text_card.delete('1.0', END)


# 更新数据库jb
def update_jb_sql():
    try:
        game_id = str(text_id.get())
        jb_num = sql_jb.get()
        db = pymysql.connect('10.0.0.32', 'root', '123456', 'game', 3306)
        cursor = db.cursor()
        sql = 'UPDATE user_info SET balance={} WHERE user_id={}'.format(jb_num, game_id)
        cursor.execute(sql)
        db.commit()
        tkinter.messagebox.showinfo('提示', '修改成功！')
        db.close()
    except:
        tkinter.messagebox.showinfo('提示', '无法连接到数据库，请联系管理员！')


button_req = Button(MyGUI, text='确定发送', command=gettxt, width=9, height=2, bd=4).grid(row=8, column=12, columnspan=13)
button_out = Button(MyGUI, text='清除重选', command=text_out, width=9, height=2, bd=4).grid(row=9, column=12, columnspan=13)
button_out = Button(MyGUI, text='修改金币', command=update_jb_sql, width=9, height=2, bd=4).grid(row=10, column=12, columnspan=13)


button_re()

MyGUI.mainloop()