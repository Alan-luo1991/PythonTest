#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import xlrd
import pymysql


def con_mysql(sql):
    db = pymysql.connect('10.0.0.32', 'root', '123456', 'game', 3306)
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()
    return cursor.fetchone()


def openxl(fileurl):
    tablename = xlrd.open_workbook(fileurl)
    tablename = tablename.sheet_by_index(0)
    return tablename


def checkconfig():
    # filelist = ['add_times_info_doudizhu.xlsx', 'game_config.xlsx', 'handcard_info.xlsx', 'person_aicontrol_info.xlsx',
    #             'platform_group_control.xlsx', 'platform_person_control.xlsx', 'takecard_info.xlsx', 'type_score_xuezhan.xlsx', 'xuezhandaodi.xlsx']
    filelist = ['game_config.xlsx']
    for filename in filelist:
        fileurl = r'E:\designer\配置表\{}'.format(filename)
        sheet = openxl(fileurl)
        xl_rows = sheet.nrows
        xl_rows -= 4
        try:
            for row in range(xl_rows):
                sql = 'select * from {} where id={}'.format(filename[:-5], row+1)
                sql_result = con_mysql(sql)
                sql_result = list(sql_result)
                xl_result = sheet.row_values(row+4)
                for i in range(len(xl_result)):
                    if sql_result[i] != xl_result[i]:
                        print('{}表第{}行,第{}列->ERRO! 配置表为：{} 数据库为：{} 表地址：{}'.format(filename, row + 1, i + 1, xl_result[i], sql_result[i], fileurl))
                    # if sql_result[i] == xl_result[i]:
                    #     print('{}表第{}行,第{}列->PASS'.format(filename, row+1, i+1))
                    # else:
                    #     print('{}表第{}行,第{}列->ERRO! 配置表为：{} 数据库为：{} 表地址：{}'.format(filename, row+1, i+1, xl_result[i], sql_result[i], fileurl))
        except:
            pass



checkconfig()