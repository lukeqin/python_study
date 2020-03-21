#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/03/21 12:16
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : example_d.py
# @notice ：


# 1
str = "www.runoob.com"
print(str.upper())          # 把所有字符中的小写字母转换成大写字母
print(str.lower())          # 把所有字符中的大写字母转换成小写字母
print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写


# 2
import calendar
monthRange = calendar.monthrange(2020,2)
print(monthRange)


# 3
# 引入 datetime 模块
import datetime

def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday

# 输出
print(getYesterday())

# 4 list
'''
>>> li
['a', 'b', 'mpilgrim', 'z', 'example']
>>> li.append("new")
>>> li
['a', 'b', 'mpilgrim', 'z', 'example', 'new']
>>> li.insert(2, "new")
>>> li
['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new']
>>> li.extend(["two", "elements"])
>>> li
['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']

join
>>> params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
>>> ["%s=%s" % (k, v) for k, v in params.items()]
['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
>>> ";".join(["%s=%s" % (k, v) for k, v in params.items()])
'server=mpilgrim;uid=sa;database=master;pwd=secret'

split
>>> li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
>>> s = ";".join(li)
>>> s
'server=mpilgrim;uid=sa;database=master;pwd=secret'
>>> s.split(";")  
['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
>>> s.split(";", 1)
['server=mpilgrim', 'uid=sa;database=master;pwd=secret']

map
>>> li = [1, 9, 8, 4]
>>> [elem*2 for elem in li]   
[2, 18, 16, 8]
>>> li
[1, 9, 8, 4]
>>> li = [elem*2 for elem in li]
>>> li
[2, 18, 16, 8]

>>> params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
>>> params.keys()
dict_keys(['server', 'database', 'uid', 'pwd'])
>>> params.values()
dict_values(['mpilgrim', 'master', 'sa', 'secret'])
>>> params.items()
dict_items([('server', 'mpilgrim'), ('database', 'master'), ('uid', 'sa'), ('pwd', 'secret')])
>>> [k for k, v in params.items()]
['server', 'database', 'uid', 'pwd']
>>> [v for k, v in params.items()]
['mpilgrim', 'master', 'sa', 'secret']
>>> ["%s=%s" % (k, v) for k, v in params.items()]
['server=mpilgrim', 'database=master', 'uid=sa', 'pwd=secret']

>>> li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
>>> [elem for elem in li if len(elem) > 1]
['mpilgrim', 'foo']
>>> [elem for elem in li if elem != "b"]
['a', 'mpilgrim', 'foo', 'c', 'd', 'd']
>>> [elem for elem in li if li.count(elem) == 1]
['a', 'mpilgrim', 'foo', 'c']
'''


# 4
people={}
for x in range(1,31):
    people[x]=1
# print(people)
check=0
i=1
j=0
while i<=31:
    if i == 31:
        i=1
    elif j == 15:
        break
    else:
        if people[i] == 0:
            i+=1
            continue
        else:
            check+=1
            if check == 9:
                people[i]=0
                check = 0
                print("{}号下船了".format(i))
                j+=1
            else:
                i+=1
                continue


# 5
def main():
    fish = 1
    while True:
        total, enough = fish, True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1)  //  5 * 4
            else:
                enough = False
                break
        if enough:
            print(f'总共有{fish}条鱼')
            break
        fish += 1


# if __name__ == '__main__':
#     main()


# 6
# import time
#
# print('按下回车开始计时，按下 Ctrl + C 停止计时。')
# while True:
#
#     input("")  # 如果是 python 2.x 版本请使用 raw_input()
#     starttime = time.time()
#     print('开始')
#     try:
#         while True:
#             print('计时: ', round(time.time() - starttime, 0), '秒', end="\r")
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print('结束')
#         endtime = time.time()
#         print('总共的时间为:', round(endtime - starttime, 2), 'secs')
#         break


# 7
# 定义立方和的函数
def sumOfSeries(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i * i

    return sum


# 调用函数
n = 5
print(sumOfSeries(n))


# 8
# 定义函数，arr 为数组，n 为数组长度，可作为备用参数，这里没有用到
def _sum(arr, n):
    # 使用内置的 sum 函数计算
    return (sum(arr))


# 调用函数
arr = []
# 数组元素
arr = [12, 3, 4, 15]

# 计算数组元素的长度
n = len(arr)

ans = _sum(arr, n)

# 输出结果
print('数组元素之和为', ans)


# 9
def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)


def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp


def printArray(arr, size):
    for i in range(size):
        print("%d" % arr[i], end=" ")


arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2, 7)
printArray(arr, 7)


