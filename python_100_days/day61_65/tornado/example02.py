#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/05/03 18:03
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : example02.py
# @notice ：


import os
import re


import tornado.ioloop
import tornado.web
import platform

from tornado.options import define, options, parse_command_line


define('port', default=8000, type=int)

users = {}


class User(object):
    """用户"""

    def __init__(self, nickname, gender, birthday):
        self.nickname = nickname
        self.gender = gender
        self.birthday = birthday


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        nickname = self.get_cookie('nickname')
        if nickname in users:
            self.render('userinfo.html', user=users[nickname])
        else:
            self.render('userform.html', hint='请填写个人信息')


class UserHandler(tornado.web.RequestHandler):
    def post(self):
        nickname = self.get_body_argument('nickname').strip()
        gender = self.get_body_argument('gender')
        birthday = self.get_body_argument('birthday')

        if not re.fullmatch(r'\w{6,20}', nickname):
            self.render('userform.html', hint='请输入有效的昵称')
        elif nickname in users:
            self.render('userform.html', hint='昵称已经被使用过')
        else:
            users[nickname] = User(nickname, gender, birthday)
            self.set_cookie('nickname', nickname, expires_days=7)
            self.render('userinfo.html', user=users[nickname])


def main():
    if platform.system() == "Windows":
        import asyncio
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', MainHandler),
                  (r'/register', UserHandler)],
        template_path=os.path.join(os.path.dirname(__file__), 'templates'))
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()