#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/24 22:16
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : json_1.py
# @notice ：


import json


def main():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }

    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('Save data succees')

if __name__ == '__main__':
    main()

# dumps是将dict转化成str格式，loads是将str转化成dict格式。
#
# dump和load也是类似的功能，只是与文件操作结合起来了。