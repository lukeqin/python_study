#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/28 22:02
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : decorator_1.py
# @notice ：


def hi(name="yasoob"):
    print("now you are inside the hi() function")

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    print(greet())
    print(welcome())
    print("now you are back in the hi() function")


hi()
greet()