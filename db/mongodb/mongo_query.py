#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/19 16:02
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : mongo_query.py
# @notice ：


import pymongo


myclient = pymongo.MongoClient("mongodb://192.168.59.129:27017/")
mydb = myclient["test"]
mycol = mydb["sites"]

# the first data frm sites
x = mycol.find_one()
print(x)

for x in mycol.find():
    print(x)

# query a filed from sites
for x in mycol.find({}, {"_id": 0, "name": 1, "alexa": 1}):
    print(x)

# except a specific
for x in mycol.find({},{ "alexa": 0 }):
  print(x)

# 0 and 1
# for x in mycol.find({},{ "name": 1, "alexa": 0 }):
#   print(x)

# query param
myquery = {"name": "RUNOOB"}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)

# $gt
myquery = {"name": {"$gt": "H"}}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)

# regex
myquery = {"name": {"$regex": "^R"}}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)

# numbers data
myresult = mycol.find().limit(3)
for x in myresult:
    print(x)