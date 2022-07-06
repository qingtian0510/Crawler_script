#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/12 10:52 下午
# @Author  : dylantian
# @Software: PyCharm

from multiprocessing import Process

def func():
    for i in range(10000):
        print("子进程", i)

if __name__ == '__main__':
    p = Process(target=func)
    p.start()
    for i in range(10000):
        print("主进程", i)
