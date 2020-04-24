#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/24 21:45
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : read1.py
# @notice ：


import time


def main():
    f = None
    try:
        # f = open('abc.txt', 'r', encoding='utf-8')
        with open('abc.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('The file was not found.')
    except LookupError:
        print('Unknown encoding.')
    except UnicodeDecodeError:
        print('Decoding fialed.')
    # finally:
    #     if f:
    #         f.close()

    with open('abc.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    with open('abc.txt') as f:
        lines = f.readlines()
    print(lines)


if __name__ == '__main__':
    main()