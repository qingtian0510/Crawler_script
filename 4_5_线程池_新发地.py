#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/18 4:38 下午
# @Author  : dylantian
# @Software: PyCharm
import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor


def download_one_page(url, page_index):
    params = {
        "limit": 20,
        "current": page_index,
        "pubDateStartTime": "",
        "pubDateEndTime": "",
        "prodPcatid": "",
        "prodCatid": "",
        "prodName": ""

    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"
    }
    resp = requests.post(url=url, params=params, headers=headers)
    print(resp.text)
    json_data = resp.json()
    for lis in json_data["list"]:
        # print(lis)
        print(list(lis.values()))
        csvwriter.writerow(list(lis.values()))

    print(f"page {page_index}", "提取完成！")


    # html = etree.HTML(resp.text)
    # table = html.xpath("/html/body/div[2]/div/div/div/div[4]/div[1]/div/table")

f = open("新发地菜价.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)


if __name__ == '__main__':
    url = "http://www.xinfadi.com.cn/getPriceData.html"
    # url = "http://www.xinfadi.com.cn/priceDetail.html"
    download_one_page(url, 1)


    with ThreadPoolExecutor(50) as t:
        for i in range(1, 200):
            t.submit(download_one_page, url, i)

    print("全部下载完成！")

