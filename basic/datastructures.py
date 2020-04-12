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


# create a list of 2-tuples like (number, square)
print([(x, x**2) for x in range(6)])
# the tuple must be parenthesized, otherwise an error is raised
# >>> [x, x**2 for x in range(6)]
#   File "<stdin>", line 1, in <module>
#     [x, x**2 for x in range(6)]


# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])


# pi
from math import pi
print([str(round(pi, i)) for i in range(1, 6)])


# Nested list conprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# The following list comprehension will transpose rows and columns
# 1
print([[row[i] for row in matrix] for i in range(4)])

# 2
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print([x for x in transposed])

# 3
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print([x for x in transposed])

# In the real world, you should prefer built-in functions to complex flow statements. The zip() function would do a great job for this use case:
# tuple
print(list(zip(*matrix)))


# The del statement
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
del a
#print(a)


# Tuples and Sequences
print("Tuples and Sequences")
t = 12345, 54321, 'hello'
print(t[0])
print(t)

# tuples may be nested
u = t, (1, 2, 3, 4, 5)
print(u)

# Tuples are immutable
# t[0] = 88888
# but they can contain mutbale objects
v = ([1, 2, 3], [3, 2, 1])
print(v)

empty = ()
singleton = 'hello',
t2 = 'hello', 'world'
print(len(empty))
print(len(singleton))
print(len(t2))
print(singleton)
print(t2)

x, y, z = t
print(x, y, z)


# Sets
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('carbgrass' in basket)

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
# unique letters in a
print(a)
# letters in a but not in b
print(a - b)
# letters in a or b or both
print(a | b)
# letters both in a and b
print(a & b)
# letters in a or b but not both
print(a ^ b)

# set
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)


# Dictionaries
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
print(list(tel))
print(sorted(tel))
print('guido' in tel)
print('jack' not in tel)


# The dict() constructor builds dictionaries directly from sequences of key-value pairs:
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
#
print({x: x**2 for x in (2, 4, 6)})
#
print(dict(sape=4139, guido=4127, jack=4098))


# Looping Techniques
# items()
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# enumerate()
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# zip()
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))

# reversed()
for i in reversed(range(1, 10, 2)):
    print(i)

# sorted()
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(basket):
    print(f)

#
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)


# More on Conditions
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)


# Comparing Sequences and Other Types
'''
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
'''