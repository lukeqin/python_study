#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/24 22:07
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : read_write_b.py
# @notice ：


def main():
    try:
        with open('cf.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open('w.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('Open the file failed.')
    except IOError as e:
        print('Error of write and read file.')
    print('Process Done')

if __name__ == '__main__':
    main()