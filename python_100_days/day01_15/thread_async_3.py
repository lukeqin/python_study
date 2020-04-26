#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/25 17:14
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : thread_async_3.py
# @notice ：


from time import time


def main():
    total = 0
    number_list = [x for x in range(1, 100000001)]
    start = time()
    for number in number_list:
        total += number
    print(total)
    end = time()
    print('Excution time: %.3fs' % (end - start))


if __name__ == '__main__':
    main()