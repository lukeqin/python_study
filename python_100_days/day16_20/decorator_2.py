#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/28 22:06
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : decorator_2.py
# @notice ：


# 1
# def hi(name="yasoob"):
#     def greet():
#         return "now you are in the greet() function"
#
#     def welcome():
#         return "now you are in the welcome() function"
#
#     if name == "yasoob":
#         return greet
#     else:
#         return welcome
#
#
# a = hi()
# print(a)
#
# print(a())


# 2
# def hi():
#     return "hi yasoob!"
#
# def doSomethingBeforeHi(func):
#     print("I am doing some boring work before executing hi()")
#     print(func())
#
# doSomethingBeforeHi(hi)


# 3
# def a_new_decorator(a_func):
#     def wrapTheFunction():
#         print("I am doing some boring work before executing a_func()")
#
#         a_func()
#
#         print("I am doing some boring work after executing a_func()")
#
#     return wrapTheFunction
#
# def a_function_requiring_decoration():
#     print(
#         "I am the function which needs some decoration to remove my foul smell")
#
# a_function_requiring_decoration()
#
# a_function_requiring_decoration = a_new_decorator(
#     a_function_requiring_decoration)
#
# a_function_requiring_decoration()


# 4
# @a_new_decorator
# def a_function_requiring_decoration():
#     """Hey you! Decorate me!"""
#     print("I am the function which needs some decoration to "
#           "remove my foul smell")
#
# # a_function_requiring_decoration()
# # a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
#
# print(a_function_requiring_decoration.__name__)


# 5
