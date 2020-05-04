#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/05/04 10:54
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : countdown.py
# @notice ：


from time import sleep


def countdown(n):
    while n > 0:
        yield n
        n -= 1

def main():
    for num in countdown(5):
        print(f'Countdown: {num}')
        sleep(1)
    print('Countdown Over!')


if __name__ == '__main__':
    main()