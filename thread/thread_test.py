#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/15 22:15
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : thread_test.py
# @notice ：


import _thread
import time


def print_tiem(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" %(threadName, time.ctime(time.time())))

try:
    _thread.start_new_thread(print_time, ("Thread-1", 2,))
    _thread.start_new_thread(print_time, ("Thread-2", 4,))
except:
    print("Error: Can not start thread.")

while 1:
    pass