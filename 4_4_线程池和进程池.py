#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/18 10:52 上午
# @Author  : dylantian
# @Software: PyCharm

# 线程池： 一次性开辟一些线程。我们用户直接给线程池提交任务，线程任务的调度交给线程池来完成

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def fn(name):
    for i in range(1000):
        print(name, i)

if __name__ == '__main__':
    # 创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(fn, name=f"thread_{i}")
    # 等待线程池中的任务全部执行完毕，才继续往下执行（守护线程）
    print("123")
