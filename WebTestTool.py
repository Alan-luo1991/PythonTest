#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/12/23 上午 11:26
# @Author   : Alan_luo
# @Site     :
# @File     : WebTestTool.py
# @Purpose  :
# @Software : PyCharm
# @Copyright:   (c)  2019
# @Licence  :     <your licence>
# @Version  :   V1.0 2019/12/23 10:49
from flask import Flask
# 实例化，可视为固定格式
app = Flask(__name__)

# route()方法用于设定路由；类似spring路由配置
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # app.run(host, port, debug, options)
    # 默认值：host=127.0.0.1, port=5000, debug=false
    app.run()
