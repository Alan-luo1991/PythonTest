#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/12/16 下午 17:51
# @Author   : Alan_luo
# @Site     :
# @File     :
# @Purpose  :
# @Software : PyCharm
# @Copyright:   (c)  2019
# @Licence  :     <your licence>
# @Version  : V1.0 2019/12/16 1744

from requests import *
from pybase64 import *


def req_userinfo():
    userinfo_url = 'http://10.0.0.32:8080/user/getUser'
    waiwang_url = 'http://192.168.11.77:9087/user/getUser'
    # heads = {'Content-Type': 'application/json'}
    # heads['Header'] = {
    #     'Content-Type': 'application/json'
    # }
    data = {
        'userId': 1
    }
    res = post(userinfo_url, data=data)
    user_data = b64decode(res.text[33:-1])
    print(res.text[33:-2])
    print(type(user_data))
    print(user_data)
    print(res.json())
    res.close()



req_userinfo()
