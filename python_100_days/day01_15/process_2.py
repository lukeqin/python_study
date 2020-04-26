#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/25 16:05
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : process_2.py
# @notice ：


from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print('Starting download process, pid [%d].' % getpid())
    print('Starting download %s ...' % filename)
    time_to_download = randint(2, 5)
    sleep(time_to_download)
    print('%s download ended, elapsed %d s.' %(filename, time_to_download))

def main():
    start = time()
    p1 = Process(target=download_task, args=('Python.pdf',))
    p1.start()
    p2 = Process(target=download_task, args=('1.mp4',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('Total elapse time %.2f s.' % (end - start))


if __name__ == '__main__':
    main()