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

if "test" in dblist:
    print("db test is exists")


# set set
mydb = myclient["test"]
mycol = mydb["sites"]

collist = mydb.list_collection_names()
if "sites" in collist:
    print("Col is exists")

# insert data to col
mydict = { "name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com" }
x = mycol.insert_one(mydict)
print(x)

# return _id filed
print(x.inserted_id)

# insert multi docs
mylist1 = [
  { "name": "Taobao", "alexa": "100", "url": "https://www.taobao.com" },
  { "name": "QQ", "alexa": "101", "url": "https://www.qq.com" },
  { "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com" },
  { "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com" },
  { "name": "Github", "alexa": "109", "url": "https://www.github.com" }
]

x = mycol.insert_many(mylist1)
print(x.inserted_ids)

# insert multi fileds with id
mylist2 = [
  { "_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
  { "_id": 2, "name": "Google", "address": "Google 搜索"},
  { "_id": 3, "name": "Facebook", "address": "脸书"},
  { "_id": 4, "name": "Taobao", "address": "淘宝"},
  { "_id": 5, "name": "Zhihu", "address": "知乎"}
]

x = mycol.insert_many(mylist2)
print(x.inserted_ids)