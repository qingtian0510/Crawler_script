#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/12 10:41 下午
# @Author  : dylantian
# # @Software: PyCharm
'''
 进程（Process）是计算机中的程序关于某数据集合上的一次运行活动，是系统进行资源分配和调度的基本单位，是操作系统
      结构的基础。在早期面向进程设计的计算机结构中，进程是程序的基本执行实体；在当代面向线程设计的计算机结构中，
      进程是线程的容器。程序是指令、数据及其组织形式的描述，进程是程序的实体。
 线程（thread）是操作系统能够进行运算调度的最小单位。它被包含在进程之中，是进程中的实际运作单位。
      一条线程指的是进程中一个单一顺序的控制流，一个进程中可以并发多个线程，每条线程并行执行不同的任务。
      在Unix System V及SunOS中也被称为轻量进程（lightweight processes），
      但轻量进程更多指内核线程（kernel thread），而把用户线程（user thread）称为线程。
一个进程可以有很多线程，每条线程并行执行不同的任务。
'''

#


from threading import Thread

# def func():
#     for i in range(1000):
#         print("func", i)
#
# if __name__ == '__main__':
#     t = Thread(target=func)
#
#     t.start()
#     for i in range(1000):
#         print("main", i)

#
# class MyThread(Thread):
#     def run(self):
#         for i in range(1000):
#             print("子线程", i)
#
# if __name__ == "__main__":
#     t = MyThread()
#     t.start()
#
#     for i in range(1000):
#         print("主线程", i)


def func(name):
    for i in range(1000):
        print(name, i)

if __name__ == '__main__':
    t1 = Thread(target=func, args=("AAA",)) #参数必须是个元组
    t1.start()

    t2 = Thread(target=func, args=("BBB",)) #参数必须是个元组
    t2.start()
