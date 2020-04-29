#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/28 22:20
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : decorator_4.py
# @notice ：


from functools import wraps


def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated

@decorator_name
def func():
    return("Function is running")

# can_run = True
# print(func())

can_run = False
print(func())
