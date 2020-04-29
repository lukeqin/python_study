#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/27 22:44
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : variables_meta.py
# @notice ：


def add(x:int, y:int) -> int:
    return x + y


print(help(add))
print(add.__annotations__)