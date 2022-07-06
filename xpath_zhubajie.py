#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/22 11:30 上午
# @Author  : dylantian
# @FileName: xpath_zhubajie.py
# @Software: PyCharm

# 拿到页面源代码
# 提取和解析数据

import requests
from lxml import etree

#xpath 解析的数组index是以 1 开始

url = "https://beijing.zbj.com/search/f/?kw=saas"
resp = requests.get(url)
# print(resp.text)

html = etree.HTML(resp.text)
divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div")
count = 0
for div in divs:
    price = div.xpath("./div/div/a[2]/div[2]/div[1]/span[1]/text()")
    title = div.xpath("./div/div/a[2]/div[2]/div[2]/p/text()")
    location = div.xpath("./div/div/a[1]/div/div/span/text()")
    print(location)
    if count > 10:
        break
    count = count + 1
