#-*- coding: UTF-8 -*-
'''
Created on 2017年3月11日
@author: luke
'''

'''
装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。
它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。装饰器是解决这类问题的绝佳设计，
有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。
'''

'''
例子：没个函数运行时记录时间
'''

import datetime


def funcruntime(func):
    def wrapper(*args, **kwargs):
        print "%s: %s" %(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), func.__name__)
        return func(*args)
    return wrapper

@funcruntime
def func_a():
    print "Func_a, running"

@funcruntime
def func_b():
    print "Func_b, running"

func_a()
func_b()