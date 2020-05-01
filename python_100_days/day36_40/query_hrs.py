#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/05/01 21:26
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : query_hrs.py
# @notice ：


import pymysql
from pymysql.cursors import DictCursor


# def main():
#     con = pymysql.connect(host='192.168.59.130', port=3306,
#                           database='hrs', charset='utf8',
#                           user='dev', password='dev')
#
#     try:
#         with con.cursor(cursor=DictCursor) as cursor:
#             cursor.execute(
#                 'select dno as no, dname as name, dloc as loc from tb_dept')
#             results = cursor.fetchall()
#             print(results)
#             print('编号\t名称\t\t所在地')
#             for dept in results:
#                 print(dept['no'], end='\t')
#                 print(dept['name'], end='\t')
#                 print(dept['loc'])
#     finally:
#         con.close()
#
# if __name__ == '__main__':
#         main()


class Emp(object):

    def __init__(self, no, name, job, sal):
        self.no = no
        self.name = name
        self.job = job
        self.sal = sal

    def __str__(self):
        return f'\n编号：{self.no}\n姓名：{self.name}\n职位：{self.job}\n月薪：{self.sal}\n'


def main():
    page = int(input('页码: '))
    size = int(input('大小: '))
    con = pymysql.connect(host='192.168.59.130', port=3306,
                          database='hrs', charset='utf8',
                          user='dev', password='dev')
    try:
        with con.cursor() as cursor:
            cursor.execute(
                'select eno as no, ename as name, job, sal from tb_emp limit %s,%s',
                ((page - 1) * size, size)
            )
            for emp_tuple in cursor.fetchall():
                emp = Emp(*emp_tuple)
                print(emp)
    finally:
        con.close()


if __name__ == '__main__':
    main()