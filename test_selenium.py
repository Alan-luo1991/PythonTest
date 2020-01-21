#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/12/09  上午 11:05
# @Author   : Alan_luo
# @Site     :
# @File     : test_selenium.py
# @Purpose  :
# @Software : PyCharm
# @Copyright:   (c)  2019
# @Licence  :     <your licence>
from selenium import webdriver
url_1 = 'http://10.0.0.15:1234'  # 血战麻将
url_2 = 'http://10.0.0.32:7456/'  # 斗地主


def running_maj(url):
    browser_1 = webdriver.Chrome(executable_path='E:\GeckoDriver\chromedriver.exe')
    browser_1.get(url)
    browser_1.set_window_size(width=960, height=520, windowHandle='current')
    browser_1.set_window_position(y=0, x=0)
    browser_2 = webdriver.Chrome(executable_path='E:\GeckoDriver\chromedriver.exe')
    browser_2.get(url)
    browser_2.set_window_size(width=960, height=520, windowHandle='current')
    browser_2.set_window_position(y=0, x=970)
    browser_3 = webdriver.Chrome(executable_path='E:\GeckoDriver\chromedriver.exe')
    browser_3.get(url)
    browser_3.set_window_size(width=960, height=520, windowHandle='current')
    browser_3.set_window_position(y=521, x=0)
    browser_4 = webdriver.Chrome(executable_path='E:\GeckoDriver\chromedriver.exe')
    browser_4.get(url)
    browser_4.set_window_size(width=960, height=520, windowHandle='current')
    browser_4.set_window_position(y=521, x=970)


def running_ddz(url):
    browser_1 = webdriver.Chrome(executable_path='E:\GeckoDriver\chromedriver.exe')
    browser_1.get(url)
    browser_1.set_window_size(width=960, height=520, windowHandle='current')
    browser_1.set_window_position(y=0, x=0)
    browser_2 = webdriver.Chrome(executable_path='E:\GeckoDriver\chromedriver.exe')
    browser_2.get(url)
    browser_2.set_window_size(width=960, height=520, windowHandle='current')
    browser_2.set_window_position(y=0, x=970)
    browser_3 = webdriver.Chrome(executable_path='E:\GeckoDriver\chromedriver.exe')
    browser_3.get(url)
    browser_3.set_window_size(width=960, height=520, windowHandle='current')
    browser_3.set_window_position(y=521, x=521)


while True:
    try:
        game = int(input("请输入你想要打开的游戏：\n 1：血战麻将 \n 2：斗地主 \n"))
        if game == 1:
            running_maj(url_1)
            continue
        elif game == 2:
            running_ddz(url_2)
            continue
        else:
            print("请选择正确的游戏，后续游戏开发中...")
    except:
        print("请选择正确的游戏，后续游戏开发中...")
