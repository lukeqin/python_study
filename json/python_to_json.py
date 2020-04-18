#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/18 15:22
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : python_to_json.py
# @notice ：


import json


# python dict
data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str = json.dumps(data)
print("Python data: ", repr(data))
print("Json object: ", json_str)

# json to python data
data2 = json.loads(json_str)
print("data2['name']: ", data2['name'])
print("data2['url']: ", data2['url'])


# read data from json file
with open('data.json', 'w') as f:
    json.dump(data, f)

with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)