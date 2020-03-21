#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/03/21 12:16
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : example_e.py
# @notice ：


# 1.1
def swapList(newList):
    size = len(newList)

    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList


newList = [1, 2, 3]

print(swapList(newList))


# 1.2
def swapList(newList):
    newList[0], newList[-1] = newList[-1], newList[0]

    return newList


newList = [1, 2, 3]
print(swapList(newList))


# 2.1
def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1 - 1, pos2 - 1))


# 2.2
def swapPositions(list, pos1, pos2):
    first_ele = list.pop(pos1)
    second_ele = list.pop(pos2 - 1)

    list.insert(pos1, second_ele)
    list.insert(pos2, first_ele)

    return list


List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1 - 1, pos2 - 1))


# 3
RUNOOB = [6, 0, 4, 1]
print('清空前:', RUNOOB)

RUNOOB.clear()
print('清空后:', RUNOOB)


# 4
def clone_runoob(li1):
    li_copy = li1[:]
    return li_copy


li1 = [4, 8, 2, 10, 15, 18]
li2 = clone_runoob(li1)
print("原始列表:", li1)
print("复制后列表:", li2)

#
def clone_runoob(li1):
    li_copy = []
    li_copy.extend(li1)
    return li_copy


li1 = [4, 8, 2, 10, 15, 18]
li2 = clone_runoob(li1)
print("原始列表:", li1)
print("复制后列表:", li2)

#
def clone_runoob(li1):
    li_copy = list(li1)
    return li_copy


li1 = [4, 8, 2, 10, 15, 18]
li2 = clone_runoob(li1)
print("原始列表:", li1)
print("复制后列表:", li2)


# 5
#
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count


lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print(countX(lst, x))

#
def countX(lst, x):
    return lst.count(x)


lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print(countX(lst, x))


# 6
total = 0

list1 = [11, 5, 17, 18, 23]

for ele in range(0, len(list1)):
    total = total + list1[ele]

print("列表元素之和为: ", total)

#
total = 0
ele = 0

list1 = [11, 5, 17, 18, 23]

while (ele < len(list1)):
    total = total + list1[ele]
    ele += 1

print("列表元素之和为: ", total)


#
list1 = [11, 5, 17, 18, 23]


def sumOfList(list, size):
    if (size == 0):
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)


total = sumOfList(list1, len(list1))

print("列表元素之和为: ", total)


#
from functools  import reduce

list1 = [11, 5, 17, 18, 23]
sum=reduce(lambda x,y:x+y,list1)
print(sum)


# 6
def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result


list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))


# 7
list1 = [10, 20, 4, 45, 99]
list1.sort()
print("最小元素为:", *list1[:1])

#
list1 = [10, 20, 1, 45, 99]
print("最小元素为:", min(list1))


# 7
list1 = [10, 20, 4, 45, 99]
list1.sort()
print("最大元素为:", list1[-1])

#
list1 = [10, 20, 1, 45, 99]
print("最大元素为:", max(list1))

