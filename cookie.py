#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/22 9:02 下午
# @Author  : dylantian
# @Software: PyCharm

import requests

session = requests.session()

# 登录
url = "https://api.17k.com/pv/log.php?Platform=Web&Guid=c401ca5b-dd19-4f29-a395-024b8f2482d0&Uid=96693894&Nickname=qingtian0510&cpsSource=0&Channel=web&callback=Q_jsonp_852048"
resp = session.get(url)

# print(resp.text)
# print(resp.cookies)

# 拿"我的书架"上的数据，使用刚才的session，保存有cookie（用户登录信息等）
resp = session.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919")
print(resp.json())
