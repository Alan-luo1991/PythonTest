#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import paramiko
import os.path
import time

print(time.ctime(os.path.getmtime('E:/WebTestTool/xuezhandaodi.out')))

def DownSerLog():
    try:
        ser_url = paramiko.Transport('10.0.0.32', 22)
        ser_url.connect(username='testsvr', password='123456')
        sftp = paramiko.SFTPClient.from_transport(ser_url)
        print('开始下载，文件较大，预计需要1-2分钟，请耐心等待...')
        sftp.get('/tmp/xuezhandaodi.out', 'E:/WebTestTool/xuezhandaodi.out')
        print("下载成功")
        ser_url.close()
    except:
        print("下载失败")


def OpenLog():
    with open('E:/WebTestTool/xuezhandaodi.out', 'r', encoding='utf8') as f:
        a = f.readlines()
        resultControl = []
        test_result = ''
        time = ''
        for i in a:
            key = 'resultControl'
            if key in i and time in i:
                resultControl.append(i)
        cardtype = {'PingHu': '平胡', 'DuiDuiHu': '对对胡', 'QingYiSe': '清一色', 'XiaoQiDui': '小七对', 'LongQiDui': '龙七对', 'QingDui': '清对',
                    'JiangDui': '将对', 'QingQiDui': '清七对', 'JiangQiDui': '将七对','QingLongQiDui': '清龙七对', 'ShiBaLuoHan': '十八罗汉',
                    'QingShiBaLuoHan': '清十八罗汉', 'JiangJinGouDiao': '将金钩钓', 'QingJinGouDiao': '清金钩钩', 'QingYaoJiu': '清幺九',
                    'CT_NONE': '无叫', 'DianGang': '点杠', 'BaGang': '巴杠', 'AnGang': '暗杠', 'HuPai': '点炮', 'Zimo': '自摸', 'ChaDaJiao': '查大叫',
                    'Huazhu': '花猪', 'ServiceFee': '服务费', 'ZhuanYu': '转雨', 'GangShangKaiHua': '杠上开花','GangShangPao': '杠上炮',
                    'QiangGangHu': '抢杠胡', 'HaiDiLaoYue': '海底捞月', 'JinGouDiao': '金钩钩', 'TianHu': '天胡', 'DiHu': '地胡', 'RenHu': '人胡',
                    'DuanYaoQiu': '断幺九', 'MengQing': '门清','DaiYaoJiu': '带幺九'}
        cardindex = 1
        for cardtypeid in cardtype:
            for result in resultControl:
                if cardtypeid in result:
                    a = 1
                    test_result += ''.join('牌型{}：{}已覆盖\n'.format(cardindex, cardtype[cardtypeid]))
                    break
            if a != 1:
                test_result += ''.join('牌型{}：{} \033[1;31m 未覆盖 \033[0m\n'.format(cardindex, cardtype[cardtypeid]))
            a = 0
            cardindex += 1
        print(test_result)
        return