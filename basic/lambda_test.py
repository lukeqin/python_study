#-*- coding: UTF-8 -*-
'''
Created on 2017年3月11日
@author: luke
'''

'''
lambda是匿名函数，没有函数名，是一个函数对象，可以把匿名函数赋值给一个变量，也可以作为返回值返回。
lambda x, y: x + y，冒号前是变量，冒号后是表达式，只能写一个表达式。定义简单函数时使用lambda能使代码更简洁。
'''

'''1'''
f = lambda x, y: x + y
print f(2, 3)
print f(1, -5)

'''2'''
print map(lambda x: x * 2, [1, 2, 3, 4, 5])


'''3'''
def lambdareturn(x, y):
    return lambda: x * y


