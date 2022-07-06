#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/21 4:37 下午
# @Author  : dylantian
# @FileName: bs4_test.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
import time

base_url = "https://umei.cc"
url = "https://umei.cc/bizhitupian/weimeibizhi/"
resp = requests.get(url)
resp.encoding = 'utf-8'
# print(resp.text)

main_page = BeautifulSoup(resp.text, "html.parser")
alist = main_page.find("ul", class_="pic-list").find_all("a")
for a in alist:
    # print(a.get('href')) #直接用get可以获取属性值
    child_page_resp = requests.get(base_url + a.get('href'))
    child_page_resp.encoding = 'utf-8'
    child_page_text = child_page_resp.text
    # 从子页面获取图片下载地址
    child_page = BeautifulSoup(child_page_text, "html.parser")
    section = child_page.find("section", class_="img-content")
    img = section.find("img")
    src = img.get("src")
    # print(img.get("src"))
    #下载图片
    img_resp = requests.get(src)
    # img_resp.content # 这里拿到的字节
    image_name = src.split("/")[-1]
    with open("imgs" + image_name, mode="wb") as f:
        f.write(img_resp.content)

    print("over!!!", image_name)
    time.sleep(0.5)
