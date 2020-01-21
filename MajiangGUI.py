#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/12/12 下午 17:51
# @Author   : Alan_luo
# @Site     :
# @File     : MajiangGUI.py
# @Purpose  :
# @Software : PyCharm
# @Copyright:   (c)  2019
# @Licence  :     <your licence>
# @Version  : V1.1 2019/12/13 16:44
from cgitb import text
from tkinter import *
from functools import partial
import tkinter.messagebox
import pymysql, json
from requests import *
from pybase64 import *

# 初始化选牌窗口
MyGUI = Tk(className="麻将配牌")
# 自定义窗口大小
MyGUI.geometry("620x530")
# 初始化配牌字典
dict_maj = dict(一万='11,', 二万='12,', 三万='13,', 四万='14,', 五万='15,', 六万='16,', 七万='17,', 八万='18,', 九万='19,',
                一筒='21,', 二筒='22,', 三筒='23,', 四筒='24,', 五筒='25,', 六筒='26,', 七筒='27,', 八筒='28,', 九筒='29,',
                一条='31,', 二条='32,', 三条='33,', 四条='34,', 五条='35,', 六条='36,', 七条='37,', 八条='38,', 九条='39,',)
# 取出所有的key
name_list = dict_maj.keys()

# 初始化窗口
text_card = Text(MyGUI, width=87, height=7)
text_card.grid(row=0, column=0, columnspan=13)
placeholder_1 = Label(MyGUI, text='换三张说明：输入0，代表关闭换三张，输入3，代表开启换三张\n目前换三张和改金币只支持32测试服').grid(row=4, column=1, columnspan=10)
placeholder_2 = Label(MyGUI, text='').grid(row=5, column=1)
user_text = Label(MyGUI, text='游戏ID：', height=2).grid(row=7, column=1)
text_ID = Entry(MyGUI, width=30, bd=1)
text_ID.grid(row=7, column=2, columnspan=3)
url_test = Label(MyGUI, text='服务器：', height=2).grid(row=8, column=1)
text_url = Entry(MyGUI, width=30, bd=1)
text_url.insert(END, 'http://10.0.0.32:6778/config')
text_url.grid(row=8, column=2, columnspan=3)
sql_change = Entry(MyGUI, width=30, bd=1)
sql_change.insert(END, '0')
sql_change.grid(row=9, column=2, columnspan=3)
text_change = Label(MyGUI, text='换三张：', height=2).grid(row=9, column=1)
sql_jb = Entry(MyGUI, width=30, bd=1)
sql_jb.insert(END, '0')
sql_jb.grid(row=10, column=2, columnspan=3)
text_jb = Label(MyGUI, text='金币数：', height=2).grid(row=10, column=1)
next_card = Entry(MyGUI, width=30, bd=1)
next_card.insert(END, '请输入麻将中文名称,例如：一万')
next_card.grid(row=11, column=2, columnspan=3)
text_next_card = Label(MyGUI, text='下一张：', height=2).grid(row=11, column=1)


# 创建所有扑克按钮
def button_re():
    for button_index, button_name in enumerate(name_list):
        button_card = Button(text=button_name, command=lambda name=button_name: text_card.insert(END, name + ','), bd=4, padx=15)
        button_card.grid(row=int(button_index / 9 + 1), column=button_index % 9 + 1)


# 发送get请求
def gettxt():
    card_str = text_card.get('0.0', 'end')
    card_list = card_str[:-2].split(',')
    statis_card_number = {}
    card_max_number = 0
    for i in card_list:
        statis_card_number[i] = card_list.count(i)
    for key, value in statis_card_number.items():
        if value > card_max_number:
            card_max_number = value
    card_ID = ''.join(dict_maj[i] for i in card_list if i != '')
    gameID = str(text_ID.get())
    url = str(text_url.get())
    if card_ID == '':
        tkinter.messagebox.showinfo('提示', '配牌不能为空！')
    elif card_max_number > 4:
        tkinter.messagebox.showinfo('提示', '相同牌不能超过4张！')
    elif gameID.isdigit() is False:
        tkinter.messagebox.showinfo('提示', '请输入正确的游戏ID！')
    # elif len(card_ID) != 39:
    #     tkinter.messagebox.showinfo('提示', '请配置13张牌！')
    else:
        try:
            res = get(url + '?user_id=' + gameID + '&maj=' + card_ID[:-1], timeout=(3, 3))
            tkinter.messagebox.showinfo('提示', res.text)
            # # print(url + '?user_id=' + gameID + '&maj=' + card_ID)
            # tkinter.messagebox.showinfo('提示', '恭喜你，配牌成功！')
        except:
            tkinter.messagebox.showinfo('提示', '无法连接到服务器，请检查地址或者联系服务器管理员！')


# 清除配牌
def text_out():
    text_card.delete('1.0', END)


# 更新数据库换三张
def update_hsz_sql():
    try:
        change_num = sql_change.get()
        db = pymysql.connect('10.0.0.32', 'root', '123456', 'game', 3306)
        cursor = db.cursor()
        sql = 'UPDATE xuezhandaodi SET exchange={} WHERE id between 1 and 5'.format(change_num)
        cursor.execute(sql)
        db.commit()
        tkinter.messagebox.showinfo('提示', '写入成功！')
        db.close()
    except:
        tkinter.messagebox.showinfo('提示', '无法连接到数据库，请联系管理员！')


# 更新数据库jb
def update_jb_sql():
    try:
        gameID = str(text_ID.get())
        jb_num = sql_jb.get()
        db = pymysql.connect('10.0.0.32', 'root', '123456', 'game', 3306)
        cursor = db.cursor()
        sql = 'UPDATE user_info SET balance={} WHERE user_id={}'.format(jb_num, gameID)
        cursor.execute(sql)
        db.commit()
        tkinter.messagebox.showinfo('提示', '修改成功！')
        db.close()
    except:
        tkinter.messagebox.showinfo('提示', '请检查游戏ID或者是否连接到内网！')


# 获取下一张牌
def take_next_card():
    cardpool_url = 'http://10.0.0.32:8801/user/mjAppointTakeCard'
    gameID = text_ID.get()
    card_key = next_card.get()
    if (card_key in name_list) is False:
        tkinter.messagebox.showinfo('提示', '请输入正确的中文牌型！')
    elif len(gameID) == 0:
        tkinter.messagebox.showinfo('提示', '请输入正确的游戏ID！')
    else:
        card = dict_maj[next_card.get()]
        data = {'UserId': int(gameID), 'Mj': int(card[:-1])}
        req = post(cardpool_url, json=data)
        print(req.text)
        if len(req.text) == 12:
            tkinter.messagebox.showinfo('提示', '配牌成功')
        else:
            tkinter.messagebox.showinfo('提示', '配牌失败，请检查是否开局或者是否有剩余麻将！')


button_req = Button(MyGUI, text='确定发送', command=gettxt, width=9, height=2, bd=4).grid(row=7, column=8, columnspan=9)
button_out = Button(MyGUI, text='清除重选', command=text_out, width=9, height=2, bd=4).grid(row=8, column=8, columnspan=9)
button_hsz_sql = Button(MyGUI, text='换三张',  command=update_hsz_sql, width=9, height=2, bd=4).grid(row=9, column=8, columnspan=9)
button_jb_sql = Button(MyGUI, text='改金币',  command=update_jb_sql, width=9, height=2, bd=4).grid(row=10, column=8, columnspan=9)
button_next_card = Button(MyGUI, text='拿牌',  command=take_next_card, width=9, height=2, bd=4).grid(row=11, column=8, columnspan=9)


button_re()
MyGUI.mainloop()