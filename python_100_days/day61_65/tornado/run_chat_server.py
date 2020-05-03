#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/05/03 20:41
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : run_chat_server.py
# @notice ：


import tornado.web
import tornado.websocket
import os
import tornado.web
import tornado.ioloop
import platform


nicknames = set()
connections = {}


class LoginHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('login.html', hint='')

    def post(self):
        nickname = self.get_argument('nickname')
        if nickname in nicknames:
            self.render('login.html', hint='昵称已被使用，请更换昵称')
        self.set_secure_cookie('nickname', nickname)
        self.render('chat.html')


class ChatHandler(tornado.websocket.WebSocketHandler):

    def open(self):
        nickname = self.get_secure_cookie('nickname').decode()
        nicknames.add(nickname)
        for conn in connections.values():
            conn.write_message(f'~~~{nickname}进入了聊天室~~~')
        connections[nickname] = self

    def on_message(self, message):
        nickname = self.get_secure_cookie('nickname').decode()
        for conn in connections.values():
            if conn is not self:
                conn.write_message(f'{nickname}说：{message}')

    def on_close(self):
        nickname = self.get_secure_cookie('nickname').decode()
        del connections[nickname]
        nicknames.remove(nickname)
        for conn in connections.values():
            conn.write_message(f'~~~{nickname}离开了聊天室~~~')


if __name__ == '__main__':
    if platform.system() == "Windows":
        import asyncio
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    app = tornado.web.Application(
        handlers=[
            (r'/login', LoginHandler),
            (r'/chat', ChatHandler)],
        template_path=os.path.join(os.path.dirname(__file__), 'templates'),
        static_path=os.path.join(os.path.dirname(__file__), 'static'),
        cookie_secret='MWM2MzEyOWFlOWRiOWM2MGMzZThhYTk0ZDNlMDA0OTU=',
    )
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()