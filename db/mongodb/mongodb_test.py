#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/18 23:17
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : mongodb_test.py
# @notice ：


import pymongo


myclient = pymongo.MongoClient("mongodb://192.168.59.129:27017/")
dblist = myclient.list_database_names()

print(dblist)