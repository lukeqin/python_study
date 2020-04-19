#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/19 19:41
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : uwsgi_test.py
# @notice ：


def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]