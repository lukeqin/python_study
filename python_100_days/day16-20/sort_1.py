#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/26 20:28
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : sort_1.py
# @notice ：


# 1 简单选择排序
# 每次j循环找出最小的，放到最左边，i循环从第1个值开始
def select_sort(items, comp=lambda x, y: x < y):
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]


# 2 冒泡排序
# j循环把i循环的当前值，找到了合适的位置，i循环结束后都排完
def bubble_sort(items, comp=lambda x, y: x > y):
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(i, len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items


# 3 搅拌排序(冒泡排序升级版)
def bubble_sort_update(items, comp=lambda x, y: x > y):
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(i, len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
            items[j], items[j + 1] = items[j + 1], items[j]
            swapped = True
        if swapped:
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j -1] = items[j -1], items[j]
                    swapped = True
        if not swapped:
            break
    return items


# 4 合并(将两个有序的列表合并成一个有序的列表)
