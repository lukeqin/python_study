#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/03/19 19:36
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : scope_namaspace.py
# @notice ：


# 名称空间和作用域
# https://www.runoob.com/python3/python3-namespace-scope.html

# 面向对象，classes
# https://www.runoob.com/python3/python3-class.html


g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域


total = 0  # 这是一个全局变量
# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total

# 调用sum函数
sum(10, 20)
print("函数外是全局变量 : ", total)


num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)
fun1()
print(num)


def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()


a = 10
def test(a):
    a = a + 1
    print(a)
test(a)


