#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/28 22:29
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : decorator_5.py
# @notice ：


from functools import wraps


# def requires_auth(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         auth = request.authorization
#         if not auth or not check_auth(auth.username, auth.password):
#             authenticate()
#         return f(*args, **kwargs)
#     return decorated


# log
def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logit
def addition_func(x):
    return x + x

result = addition_func(4)