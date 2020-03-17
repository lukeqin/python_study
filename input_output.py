#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/03/17 19:27
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : input_output.py
# @notice ：


# Fancier output formatting
'''
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
'Results of the 2016 Referendum'
'''


'''
>>> yes_votes = 42_572_654
>>> no_votes = 43_132_495
>>> percentage = yes_votes / (yes_votes + no_votes)
>>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'
'''


# str()
# repr()
'''
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> # The repr() of a string adds string quotes and backslashes:
... hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> # The argument to repr() may be any Python object:
... repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
'''


'''
str(object)：将指定的值转换为字符串。用于转换bytes时，可指定编码和错误处理方式

repr(object)：返回指定值的字符串表示

print(repr("Hello, \nWorld!"))
# 'Hello, \nWorld!'

print(str("Hello, \nWorld!"))
# Hello, 
# World!

函数str()和repr()都可以将Python中的对象转换为字符串，它们的使用以及输出都非常相似。但也存在不一致的情况。

import decimal

a = decimal.Decimal(1.25)
print(str(a), repr(a))  # 1.25 Decimal('1.25')


from datetime import date

b = date.today()
print(str(b), repr(b))  # 2019-05-22 datetime.date(2019, 5, 22)

这两者之间到底有什么区别呢？总结来说以下几点：

两者之间的目标不同：str()主要面向用户，其目的是可读性，返回形式为用户友好性和可读性都较强的字符串类型；而repr()面向的是Python解释器，
或者说开发人员，其目的是准确性，其返回值表示Python解释器内部的含义，常作为编程人员debug用途。

在解释器中直接输入a时调用repr()函数，而print(a)则调用str()函数。

repr()的返回值一般可以用eval()函数来还原对象，通常来说有如下等式。

```python
obj == eval(repr(obj))
```

但需要提醒的是，这个等式不是所有情况下都成立。

这两个方法分别调用内建的__str__()方法和__repr__()方法，一般来说在类中都应该定义__repr__()方法，而__str__()方法则为可选，
当可读性比准确性更为重要的时候应该考虑定义__str__()方法。如果类中没有定义__str__()方法，则默认会使用__repr__()方法的结果来返回对象的字符串表示形式。
用户实现__repr__()方法的时候最好保证其返回值可以用eval()方法使对象重新还原。

'''


# Formated string literals
import math
print(f'The value of pi is approximately {math.pi:.3f}.')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

# Other modifiers can be used to convert the value before it is formatted. '!a' applies ascii(), '!s' applies str(), and '!r' applies repr():

animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')


# The string format() method
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

print('This {food} is {adjective}.'.format(food='spam',
                                           adjective='absolutely horrible'))

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                       other='Georg'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))

# ** notation
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

#
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# Manual string formatting
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))

# zfill()
'''
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
'''


# Old string formatting
print('The value of pi is approximately %5.3f.' % math.pi)


# Reading and writing files
with open('workfile') as f:
    read_data = f.read()
print(read_data)
#f.closed()
#f.read()


# Method of file objects
# read s single line from the file
# f.readline()
with open('workfile') as f:
    for line in f:
        print(line, end='')

# file write
'''
>>> f.write('This is a test\n')
15

>>> value = ('the answer', 42)
>>> s = str(value)  # convert the tuple to string
>>> f.write(s)
18

>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)      # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)  # Go to the 3rd byte before the end
13
>>> f.read(1)
b'd'
'''


# Save structured data with json
'''
If you have an object x, you can view its JSON string representation with a simple line of code:

>>>
>>> import json
>>> json.dumps([1, 'simple', 'list'])
'[1, "simple", "list"]'
Another variant of the dumps() function, called dump(), simply serializes the object to a text file. So if f is a text file object opened for writing, we can do this:

json.dump(x, f)
To decode the object again, if f is a text file object which has been opened for reading:

x = json.load(f)
'''

