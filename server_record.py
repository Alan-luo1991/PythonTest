#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/24 0024 上午 11:05
# @Author   :
# @Site     : 
# @File     : server_record.py
# @Purpose  :
# @Software : PyCharm
# @Copyright:   (c)  2018
# @Licence  :     <your licence>

"""
获取服务器日志的脚本，注意需要配置的部分
"""

import paramiko
import re, os
import time
import xlwt, xlrd

"""**********************************配置开始*********************************************"""

user_id = "15964"  # 账号设置，如果设置为user_id = ""，则查询所有账号日志
day_time = "2018-12-29"  # 日志日期
key_word = "spin"  # 查找的日志类型，例如login、spin，存在base_log中， 如果设置为空，则查询所有类型
log_file = "E://log.xls"  # 日志保存的地方

"""**********************************配置结束*********************************************"""

remote_path = ""  # 服务器日志路径
base_log = os.getcwd() + "\\" + "base_log.xlsx"  ## 基本的log配置表，名字和位置配在这
print(base_log)


def decor(func):
    def middle(*args, **kwargs):
        print(func.__name__, ("is running..."))
        time1 = time.time()
        func(*args, **kwargs)
        time2 = time.time()
        print(func.__name__, ("耗时为%ss" % int(time2 - time1)))

    return middle


class Server():
    def __init__(self):
        """
        初始化连接，将当天的所有log数据依次写入
        :param remote_path: 服务器数据路径
        """
        self.local_path = "E:\\server_record.log"
        self.search_item = "{winningslots\}:  spin.*?\t%s\t" % str(user_id)
        self.t = paramiko.Transport(" ", "")  # ssh的ip和端口
        self.t.connect(username="", password="")  # 账号和密码
        self.sftp = paramiko.SFTPClient.from_transport(self.t)  # 配置连接服务器
        # self.sftp.get(remote_path, local_path)

    @decor
    def select_data(self, key):
        all_file = self.sftp.listdir(remote_path)
        file_path = []
        for i in all_file:
            if str(day_time) in i:
                file_path.append(remote_path + "/" + i)
        file_path.sort()
        print ("Remote_log_path:"), file_path  # 云端文件路径
        print ("Log Detail:")
        # 开始处理写入
        row = 1  # 行

        # 写第一行
        style1 = xlwt.easyxf('pattern: pattern solid, fore_color coral; align: wrap on, vert center, horiz center')
        style2 = xlwt.easyxf("align: wrap off, vert center, horiz left")
        data = xlrd.open_workbook(base_log)
        sheet = data.sheet_by_index(0)  # 第一个sheet的数据获取
        index_list = sheet.col(1)  # 获取第二列的数据，作为key

        key_index = []
        for i in index_list:
            key_index.append(i.value)

        key_col = key_index.index(key)  # 需要的key对应行数

        key_value = []
        for count, i in enumerate(sheet.row(key_col)):
            if i.value == "":
                key_value.append(sheet.cell(0, count).value)
            else:
                key_value.append(i.value)

        workbook = xlwt.Workbook("utf-8")
        worksheet = workbook.add_sheet(day_time)

        # 设置列宽
        for i in range(len(key_value)):
            worksheet.col(i).width = 256 * 13

        for loc, i in enumerate(key_value[1:]):
            worksheet.write(0, loc, i, style1)

        #  第一行数据写完
        for i in file_path:
            self.sftp.get('0.0', 'end')  # 循环复制文件到本地
            if key == "spin1":
                self.get_data()
            else:
                # 根据key处理打印需要的数据
                key_re = "{slots\}:  %s.*?\t%s\t" % (key, user_id)
                with open(self.local_path, "r") as f:
                    data = f.readlines()
                for num, i in enumerate(data):
                    col = 0
                    if re.search(key_re, i):
                        data_select = re.split("\t|\t".decode("utf-8"), i)
                        for count, j in enumerate(data_select):
                            # print "行：", row, "列：", count, "j:", j
                            if count == 0:
                                j = j.split("|")[1][:-5] + j.split("|")[-1].split(" ")[-1]
                            print(j)
                            if j != "|":
                                # print ("row:"), row, ("count:"), count
                                worksheet.write(row, col, j, style2)
                                col += 1
                        row += 1

        workbook.save(log_file)

        self.t.close()


if __name__ == '__main__':
    da = Server()
    da.select_data(key_word)
    print ("日志已保存在 %s" % log_file)
