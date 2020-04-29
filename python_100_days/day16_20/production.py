#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/25 20:49
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : production.py
# @notice ：


# 1 productin
prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

prices2 = {key: value for key, value in prices.items() if value > 100}
print(prices)
print(prices2)


# nested list
# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# courses = ['语文', '数学', '英语']
#
# scores = [[None] * len(courses) for _ in range(len(names))]
# print(scores)
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
#         scores[row][col] = float(input(f'Please input {name}\'s {course} score: '))
#         print(scores)
# print(scores)


# 3 heapq模块（堆排序）
import heapq


list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

print(heapq.nlargest(3, list1))
print(heapq.nsmallest(3, list1))
print(heapq.nlargest(2, list2, key=lambda x: x['price']))
print(heapq.nlargest(2, list2, key=lambda x: x['shares']))


# 4 itertools
import itertools


s = itertools.permutations('ABCD')
s = itertools.combinations('ABCDE', 3)
s = itertools.product('ABCD', '123')
# s = itertools.cycle(('A', 'B', 'C'))
for i in s:
    print(i)


# 5 collections
from collections import Counter


words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]

counter = Counter(words)
print(counter.most_common(3))