#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/12 17:22
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : mysql_pymysql_test.py
# @notice ：


import pymysql


# 打开数据库连接
db = pymysql.connect("ip", "dev", "", "dev_db")

# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")
#
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
#
# print("Database version : %s " % data)
#
# # 关闭数据库连接
# db.close()


# create a table
# cursor = db.cursor()
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""
# cursor.execute(sql)
# db.close()


# insert data record
# cursor = db.cursor()
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
#
# db.close()


# query data record
# cursor = db.cursor()
# sql = "SELECT * FROM EMPLOYEE \
#        WHERE INCOME > %s" % (1000)
# try:
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     for row in results:
#         fname = row[0]
#         lname = row[1]
#         age = row[2]
#         sex = row[3]
#         income = row[4]
#         print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % (
#         fname, lname, age, sex, income))
# except:
#     print("Error: unable to fetch data")
#
# db.close()


# update data record
# cursor = db.cursor()
# sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
#
# db.close()


# delete data record
# cursor = db.cursor()
# sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
#
# db.close()