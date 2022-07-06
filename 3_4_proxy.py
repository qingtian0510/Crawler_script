#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/23 11:19 下午
# @Author  : dylantian
# @Software: PyCharm


# 代理：原理，通过第三方的机器去发送请求

import requests

proxies = {
    "https": "https://61.153.251.150:22222"
}

resp = requests.get("https://www.baidu.com", proxies=proxies)
resp.encoding = "utf-8"

print(resp.text)
