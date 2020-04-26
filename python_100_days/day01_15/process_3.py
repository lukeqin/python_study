#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/25 16:14
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : process_3.py
# @notice ：


from multiprocessing import Process
from time import sleep


counter = 0

def sub_task(string):
    global counter
    while counter < 10:
        print(string, end='', flush=True)
        counter += 1
        sleep(0.01)

def main():
    Process(target=sub_task, args=('Ping',)).start()
    Process(target=sub_task, args=('Pong',)).start()


if __name__ == '__main__':
    main()