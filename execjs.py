#!/usr/bin/env/python3
# -*- coding: utf-8 -*-


import execjs

zjh_c_bet = execjs.compile(open(r"D:\Mytest\QA-TOOL\app\script\zjh-client.js").read().decode("utf-8")).call('loginHandle', 'steam')
