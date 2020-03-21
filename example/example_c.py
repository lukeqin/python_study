#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/03/21 12:15
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : example_c.py
# @notice ：


# 1
# 如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153。
#
# 1000以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。

# Python 检测用户输入的数字是否为阿姆斯特朗数

# 获取用户输入的数字
# num = int(input("请输入一个数字: "))
#
# # 初始化变量 sum
# sum = 0
# # 指数
# n = len(str(num))
#
# # 检测
# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** n
#     temp //= 10
#
# # 输出结果
# if num == sum:
#     print(num, "是阿姆斯特朗数")
# else:
#     print(num, "不是阿姆斯特朗数")


# 2
# 获取用户输入数字
# lower = int(input("最小值: "))
# upper = int(input("最大值: "))
#
# for num in range(lower, upper + 1):
#     # 初始化 sum
#     sum = 0
#     # 指数
#     n = len(str(num))
#
#     # 检测
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** n
#         temp //= 10
#
#     if num == sum:
#         print(num)


# 3
# 获取用户输入十进制数
# dec = int(input("输入数字："))
#
# print("十进制数为：", dec)
# print("转换为二进制为：", bin(dec))
# print("转换为八进制为：", oct(dec))
# print("转换为十六进制为：", hex(dec))


# 4
# 用户输入字符
# c = input("请输入一个字符: ")
#
# # 用户输入ASCII码，并将输入的数字转为整型
# a = int(input("请输入一个ASCII码: "))
#
# print(c + " 的ASCII 码为", ord(c))
# print(a, " 对应的字符为", chr(a))


# 5
# 定义一个函数
# def hcf(x, y):
#     """该函数返回两个数的最大公约数"""
#
#     # 获取最小值
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#
#     for i in range(1, smaller + 1):
#         if ((x % i == 0) and (y % i == 0)):
#             hcf = i
#
#     return hcf
#
#
# # 用户输入两个数字
# num1 = int(input("输入第一个数字: "))
# num2 = int(input("输入第二个数字: "))
#
# print(num1, "和", num2, "的最大公约数为", hcf(num1, num2))


# 6
# 定义函数
# def lcm(x, y):
#     #  获取最大的数
#     if x > y:
#         greater = x
#     else:
#         greater = y
#
#     while (True):
#         if ((greater % x == 0) and (greater % y == 0)):
#             lcm = greater
#             break
#         greater += 1
#
#     return lcm
#
#
# # 获取用户输入
# num1 = int(input("输入第一个数字: "))
# num2 = int(input("输入第二个数字: "))
#
# print(num1, "和", num2, "的最小公倍数为", lcm(num1, num2))


# 7
# 定义函数
def add(x, y):
    """相加"""

    return x + y


def subtract(x, y):
    """相减"""

    return x - y


def multiply(x, y):
    """相乘"""

    return x * y


def divide(x, y):
    """相除"""

    return x / y


# 用户输入
# print("选择运算：")
# print("1、相加")
# print("2、相减")
# print("3、相乘")
# print("4、相除")
#
# choice = input("输入你的选择(1/2/3/4):")
#
# num1 = int(input("输入第一个数字: "))
# num2 = int(input("输入第二个数字: "))
#
# if choice == '1':
#     print(num1, "+", num2, "=", add(num1, num2))
#
# elif choice == '2':
#     print(num1, "-", num2, "=", subtract(num1, num2))
#
# elif choice == '3':
#     print(num1, "*", num2, "=", multiply(num1, num2))
#
# elif choice == '4':
#     print(num1, "/", num2, "=", divide(num1, num2))
# else:
#     print("非法输入")


# 8
# 引入日历模块
# import calendar
#
# # 输入指定年月
# yy = int(input("输入年份: "))
# mm = int(input("输入月份: "))
#
# # 显示日历
# print(calendar.month(yy, mm))


# 9
# def recur_fibo(n):
#     """递归函数
#     输出斐波那契数列"""
#     if n <= 1:
#         return n
#     else:
#         return (recur_fibo(n - 1) + recur_fibo(n - 2))
#
#
# # 获取用户输入
# nterms = int(input("您要输出几项? "))
#
# # 检查输入的数字是否正确
# if nterms <= 0:
#     print("输入正数")
# else:
#     print("斐波那契数列:")
#     for i in range(nterms):
#         print(recur_fibo(i))


# 10
# 写文件
# with open("test.txt", "wt") as out_file:
#     out_file.write("该文本会写入到文件中\n看到我了吧！")
#
# # Read a file
# with open("test.txt", "rt") as in_file:
#     text = in_file.read()
#
# print(text)


# 11
# 测试实例一
print("测试实例一")
str = "runoob.com"
print(str.isalnum()) # 判断所有字符都是数字或者字母
print(str.isalpha()) # 判断所有字符都是字母
print(str.isdigit()) # 判断所有字符都是数字
print(str.islower()) # 判断所有字符都是小写
print(str.isupper()) # 判断所有字符都是大写
print(str.istitle()) # 判断所有单词都是首字母大写，像标题
print(str.isspace()) # 判断所有字符都是空白字符、\t、\n、\r

print("------------------------")

# 测试实例二
print("测试实例二")
str = "runoob"
print(str.isalnum())
print(str.isalpha())
print(str.isdigit())
print(str.islower())
print(str.isupper())
print(str.istitle())
print(str.isspace())


