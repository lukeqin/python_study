#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/19 16:23
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : mongo_sort.py
# @notice ：


import pymongo


myclient = pymongo.MongoClient("mongodb://192.168.59.129:27017/")
mydb = myclient["test"]
mycol = mydb["sites"]

# sort by alexa
mydoc = mycol.find().sort("alexa")
for x in mydoc:
  print(x)

# desc
mydoc = mycol.find().sort("alexa", -1)
for x in mydoc:
    print(x)