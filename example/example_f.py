#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/03/21 16:31
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : example_f.py
# @notice ：


# 1
# 给定一个字符串，然后移除制定位置的字符
test_str = "Runoob"

# 输出原始字符串
print("原始字符串为 : " + test_str)

# 移除第三个字符 n
new_str = ""

for i in range(0, len(test_str)):
    if i != 2:
        new_str = new_str + test_str[i]

print("字符串移除后为 : " + new_str)


# 2
# sub str
def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("不存在！")
    else:
        print("存在！")

string = "www.runoob.com"
sub_str = "runoob"
check(string, sub_str)


# 3
# string length
str = "runoob"
print(len(str))

#
def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter

str = "runoob"
print(findLen(str))


# 4
import re


def Find(string):
    # findall() 查找匹配正则表达式的字符串
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string)
    return url

string = 'Runoob 的网页地址为：https://www.runoob.com，Google 的网页地址为：https://www.google.com'
print("Urls: ", Find(string))


# 5
# exec str as code
def exec_code():
    LOC = """ 
def factorial(num): 
    fact=1 
    for i in range(1,num+1): 
        fact = fact*i 
    return fact 
print(factorial(5)) 
"""
    exec(LOC)

exec_code()


# 6
str='Runoob'
print(str[::-1])

#
str='Runoob'
print(''.join(reversed(str)))


# 7
def rotate(input, d):
    Lfirst = input[0: d]
    Lsecond = input[d:]
    Rfirst = input[0: len(input) - d]
    Rsecond = input[len(input) - d:]

    print("头部切片翻转 : ", (Lsecond + Lfirst))
    print("尾部切片翻转 : ", (Rsecond + Rfirst))


if __name__ == "__main__":
    input = 'Runoob'
    d = 2  # 截取两个字符
    rotate(input, d)


# 8
def dictionairy():
    # 声明字典
    key_value = {}

    # 初始化
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("按键(key)排序:")

    # sorted(key_value) 返回一个迭代器
    # 字典按键排序
    for i in sorted(key_value):
        print((i, key_value[i]), end=" ")


def main():
    # 调用函数
    dictionairy()


# 主函数
if __name__ == "__main__":
    main()


# 9
def returnSum(myDict):
    sum = 0
    for i in myDict:
        sum = sum + myDict[i]

    return sum

dict = {'a': 100, 'b': 200, 'c': 300}
print("\nSum :", returnSum(dict))


# 10
# remove key and value from dictionary
# del
# test_dict = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}
#
# # 输出原始的字典
# print("字典移除前 : " + str(test_dict))
#
# # 使用 del 移除 Zhihu
# del test_dict['Zhihu']
#
# # 输出移除后的字典
# print("字典移除后 : " + str(test_dict))
#
# # 移除没有的 key 会报错
# # del test_dict['Baidu']


# pop()
# test_dict = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}
#
# # 输出原始的字典
# print("字典移除前 : " + str(test_dict))
#
# # 使用 pop 移除 Zhihu
# removed_value = test_dict.pop('Zhihu')
#
# # 输出移除后的字典
# print("字典移除后 : " + str(test_dict))
#
# print("移除的 key 对应的 value 为 : " + str(removed_value))
#
# print('\r')
#
# # 使用 pop() 移除没有的 key 不会发生异常，我们可以自定义提示信息
# removed_value = test_dict.pop('Baidu', '没有该键(key)')
#
# # 输出移除后的字典
# print("字典移除后 : " + str(test_dict))
# print("移除的值为 : " + str(removed_value))


# items()
# test_dict = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}
#
# # 输出原始的字典
# print("字典移除前 : " + str(test_dict))
#
# # 使用 pop 移除 Zhihu
# new_dict = {key: val for key, val in test_dict.items() if key != 'Zhihu'}
#
# # 输出移除后的字典
# print("字典移除后 : " + str(new_dict))


# 11
# merge dictionaries
# update()
def Merge(dict1, dict2):
    return (dict2.update(dict1))


# 两个字典
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

# 返回  None
print(Merge(dict1, dict2))

# dict2 合并了 dict1
print(dict2)


# **
def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res


# 两个字典
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict3 = Merge(dict1, dict2)
print(dict3)


# 12
# Convert the string time to a timestamp
import time

a1 = "2019-5-10 23:40:00"
# 先转换为时间数组
timeArray = time.strptime(a1, "%Y-%m-%d %H:%M:%S")

# 转换为时间戳
timeStamp = int(time.mktime(timeArray))
print(timeStamp)

# 格式转换 - 转为 /
a2 = "2019/5/10 23:40:00"
# 先转换为时间数组,然后转换为其他格式
timeArray = time.strptime(a2, "%Y/%m/%d %H:%M:%S")
otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
print(otherStyleTime)


# 13
import time
import datetime

# 先获得时间数组格式的日期
threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days=3))
# 转换为时间戳
timeStamp = int(time.mktime(threeDayAgo.timetuple()))
# 转换为其他字符串格式
otherStyleTime = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime)


#
import time
import datetime

# 给定时间戳
timeStamp = 1557502800
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
threeDayAgo = dateArray - datetime.timedelta(days=3)
print(threeDayAgo)


