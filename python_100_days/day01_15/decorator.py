#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/22 22:06
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : decorator.py
# @notice ：


class Person(object):
    # 限定Person对象只能绑定_name, _age和_gender属性
    # __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s is playing Aeroplane Chess.' % self._name)
        else:
            print('%s is playing chinese poker.' % self._name)


def main():
    person = Person('Wang da', 12)
    person.play()
    person.age = 22
    person.play()


if __name__ == '__main__':
    main()