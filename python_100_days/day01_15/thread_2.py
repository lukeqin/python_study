#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/25 16:24
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : thread_2.py
# @notice ：


from random import randint
from threading import Thread
from time import time, sleep


class DownloadTask(Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('Starting downlaod %s ...' % self._filename)
        time_to_download = randint(2, 5)
        sleep(time_to_download)
        print('%s download ended, total time elapse %d s.' % (self._filename, time_to_download))


def main():
    start = time()
    t1 = DownloadTask('Python.pdf')
    t1.start()
    t2 = DownloadTask('1.mp4')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('Total time elapse %.2f s.' % (end - start))


if __name__ == '__main__':
    main()