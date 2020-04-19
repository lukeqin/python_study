#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/19 16:19
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : mongo_update.py
# @notice ：


import pymongo


myclient = pymongo.MongoClient("mongodb://192.168.59.129:27017/")
mydb = myclient["test"]
mycol = mydb["sites"]

# change alexa filed data, the fisrt one
myquery = {"alexa": "10000"}
newvalues = {"$set": {"alexa": "12345"}}
mycol.update_one(myquery, newvalues)
for x in mycol.find():
    print(x)

# set with regex
myquery = {"name": {"$regex": "^F"}}
newvalues = {"$set": {"alexa": "123"}}
x = mycol.update_many(myquery, newvalues)
print(x.modified_count, "文档已修改")