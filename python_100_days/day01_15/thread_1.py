#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/25 16:19
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : thread_1.py
# @notice ：


from random import randint
from threading import Thread
from time import time, sleep


def download(filename):
    print('Starting download %s...' % filename)
    time_to_download = randint(2, 5)
    sleep(time_to_download)
    print('%s download ended, elapsed time %s s' % (filename, time_to_download))

def main():
    start = time()
    t1 = Thread(target=download, args=('Python.pdf',))
    t1.start()
    t2 = Thread(target=download, args=('1.mp4',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('Total elapse time %.3f.' % (end - start))


if __name__ == '__main__':
    main()
