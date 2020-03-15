#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/03/15 21:52
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : datastructures.py
# @notice ：


# for, list append
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
# x that still exists after the loop completes

# map
squares1 = list(map(lambda x: x**2, range(10)))
print(squares1)

# for x in
squares2 = [x**2 for x in range(10)]
print(squares2)



# combs
print([(x, y) for x in [1, 2, 3] for y in (3, 1, 4) if x != y])

# combs1, for
combs1 = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs1.append((x, y))
print(combs1)


# vec
vec = [-4, -2, 0, 2, 4]
# create a new list with the value doubled
print([x*2 for x in vec])
# filter the list to exclude negative numbers
print([x for x in vec if x >= 0])
# apply a function to all the elements
print([abs(x) for x in vec])

# call a method on each element
freshfruit = ['  banana', '  loganberry', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])

