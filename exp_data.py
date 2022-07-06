#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 4:08 下午
# @Author  : dylantian
# @Software: PyCharm
import csv

# f = open('data/exp_data.csv', mode='r')
# fout = open('data/exp_result.txt', mode='w')

f = open('data/base_data.csv', mode='r')
fout = open('data/base_result.txt', mode='w')

result_tmp = []
count = 0
for line in f.readlines():
    # print(line.strip())
    line = line.strip()
    strs = line.split(',')
    qimei36 = strs[0]
    article_id = strs[2]
    if len(article_id) < 13:
        continue

    tts = article_id.split("_")
    if len(tts) > 1:
        continue
    start_article_id = strs[3]
    if len(start_article_id) < 9:
        continue
    if start_article_id[8] == 'S' or start_article_id[8] == 'V':
        continue

    # data_key = qimei36 + "_" + start_article_id
    # if article_id != start_article_id:
    #     # print(line)
    #     if data_key in result_tmp:
    #         if article_id not in result_tmp[data_key]:
    #             result_tmp[data_key].append(article_id)
    #     else:
    #         tmp_list = []
    #         tmp_list.append(article_id)
    #         result_tmp[data_key] = tmp_list
    res = article_id + "\t" + start_article_id
    if res not in result_tmp:
        result_tmp.append(res)

print("count:", len(result_tmp))
for line in result_tmp:
    fout.write(line + "\n")

# print("len:", len(result_tmp))
# # print(result_tmp)
# result = {}
# count = 0
# csvwriter = csv.writer(fout)
# for k,v in result_tmp.items():
#     if len(v) >= 3 and len(v) <= 6:
#         count = count + 1
#         new_v = [str(item) for item in v]
#         res = k.split("_")[1] + "\t" + "\t".join(new_v)
#
#         print(res)
#         fout.write(res + "\n")
#
#
#

f.close()
fout.close()

