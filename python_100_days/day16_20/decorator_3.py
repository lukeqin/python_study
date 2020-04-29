#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/28 22:16
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : decorator_3.py
# @notice ：


from functools import wraps


def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction


@a_new_decorator
def a_function_requiring_decoration():
    """Hey yo! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")


print(a_function_requiring_decoration.__name__)
a_function_requiring_decoration()