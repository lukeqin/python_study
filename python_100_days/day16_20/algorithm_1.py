#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/27 22:09
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : algorithm_1.py
# @notice ：


# 1
for x in range(20):
    for y in range(33):
        z = 100 - x - y
        if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
            print(x, y, z)


# 2
fish = 6
while True:
    total = fish
    enough = True
    for _ in range(5):
        if (total -1) % 5 == 0:
            total = (total - 1) // 5 * 4
        else:
            enough = False
            break
    if enough:
        print(fish)
        break
    fish += 5