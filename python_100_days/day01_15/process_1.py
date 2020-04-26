#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/25 15:58
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : process_1.py
# @notice ：


from random import randint
from time import time, sleep


def download_task(filename):
    print('Starting download %s...' % filename)
    time_to_download = randint(2, 5)
    sleep(time_to_download)
    print('%s download ended, elapsed time %s s' %(filename, time_to_download))

def main():
    start = time()
    download_task('Python.pdf')
    download_task('1.mp4')
    end = time()
    print('Total time %.2f s.' %(end - start))

if __name__ == '__main__':
    main()