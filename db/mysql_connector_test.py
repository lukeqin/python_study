#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/12 15:36
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : mysql_connector_test.py
# @notice ：


import db.connector

mydb = db.connector.connect(
    host="ip",  # 数据库主机地址
    user="dev",  # 数据库用户名
    passwd="",  # 数据库密码
    database="dev_db"  #database
)

# connection
print(mydb)


# create db
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE dev_db")


# view db name
# mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")
#
# for x in mycursor:
#     print(x)


# connect a db
# database="dev_db"  #database


# create a table in a db
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")


# view if a table is existing
# mycursor = mydb.cursor()
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)


# primary key
# mycursor = mydb.cursor()
# mycursor.execute(
#     "ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")


# create a table and a primary key
# mycursor = mydb.cursor()
# mycursor.execute(
#     "CREATE TABLE sites1 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")


# insert data
# mycursor = mydb.cursor()
#
# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = ("RUNOOB", "https://www.runoob.com")
# mycursor.execute(sql, val)
#
# mydb.commit()  # 数据表内容有更新，必须使用到该语句
# print(mycursor.rowcount, "记录插入成功。")


# insert bulk data
# mycursor = mydb.cursor()
# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = [('Google', 'https://www.google.com'),
#     ('Github', 'https://www.github.com'), ('Taobao', 'https://www.taobao.com'),
#     ('stackoverflow', 'https://www.stackoverflow.com/')]
#
# mycursor.executemany(sql, val)
#
# mydb.commit()  # 数据表内容有更新，必须使用到该语句
#
# print(mycursor.rowcount, "记录插入成功。")

# insert one data record and print data record id
# mycursor = mydb.cursor()
#
# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = ("Zhihu", "https://www.zhihu.com")
# mycursor.execute(sql, val)
#
# mydb.commit()
#
# print("1 条记录已插入, ID:", mycursor.lastrowid)


# query data
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM sites")
# myresult = mycursor.fetchall()  # fetchall() 获取所有记录
#
# for x in myresult:
#     print(x)

# filed
# mycursor = mydb.cursor()
# mycursor.execute("SELECT name, url FROM sites")
# myresult = mycursor.fetchall()
#
# for x in myresult:
#     print(x)

# get one record
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM sites")
# myresult = mycursor.fetchone()
#
# print(myresult)


# where condition syntax
# mycursor = mydb.cursor()
# sql = "SELECT * FROM sites WHERE name ='RUNOOB'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
#
# for x in myresult:
#     print(x)

# 通配符 %
# mycursor = mydb.cursor()
# sql = "SELECT * FROM sites WHERE url LIKE '%oo%'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
#
# for x in myresult:
#     print(x)

# 为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义查询的条件
# mycursor = mydb.cursor()
# sql = "SELECT * FROM sites WHERE name = %s"
# na = ("RUNOOB",)
# mycursor.execute(sql, na)
# myresult = mycursor.fetchall()
#
# for x in myresult:
#     print(x)


# order
# mycursor = mydb.cursor()
# sql = "SELECT * FROM sites ORDER BY name DESC"    # or DESC
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
#
# for x in myresult:
#     print(x)


# limit
# mycursor = mydb.cursor()
# # mycursor.execute("SELECT * FROM sites LIMIT 3")
# mycursor.execute("SELECT * FROM sites LIMIT 3 OFFSET 1")
# myresult = mycursor.fetchall()
#
# for x in myresult:
#     print(x)


# delete data
# mycursor = mydb.cursor()
# sql = "DELETE FROM sites WHERE name = 'stackoverflow'"
# mycursor.execute(sql)
# mydb.commit()
#
# print(mycursor.rowcount, " 条记录删除")

# delete with where
# mycursor = mydb.cursor()
# sql = "DELETE FROM sites WHERE name = %s"
# na = ("zhihu",)
# mycursor.execute(sql, na)
# mydb.commit()
#
# print(mycursor.rowcount, " 条记录删除")


# update data
# mycursor = mydb.cursor()
# sql = "UPDATE sites SET name = 'Taobaobao' WHERE name = 'Taobao'"
'''
sql = "UPDATE sites SET name = %s WHERE name = %s
val = ("new name", "Taobao")
'''
# mycursor.execute(sql)
# mydb.commit()
#
# print(mycursor.rowcount, " 条记录被修改")


# delete table
# mycursor = mydb.cursor()
# sql = "DROP TABLE IF EXISTS sites1"  # 删除数据表 sites
#
# mycursor.execute(sql)