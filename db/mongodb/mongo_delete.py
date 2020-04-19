#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/19 16:25
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : mongo_delete.py
# @notice ：


import pymongo


myclient = pymongo.MongoClient("mongodb://192.168.59.129:27017/")
mydb = myclient["test"]
mycol = mydb["sites"]

# delete one
myquery = {"name": "Taobao"}
mycol.delete_one(myquery)

for x in mycol.find():
    print(x)

# delete multi
myquery = {"name": {"$regex": "^F"}}
x = mycol.delete_many(myquery)
print(x.deleted_count, "docs were been deleted")

# delete all docs
x = mycol.delete_many({})
print(x.deleted_count, "docs were been deleted")

# delete col
mycol.drop()