#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/12 23:05
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : server.py
# @notice ：


import socket
import sys


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999
print(host)

serversocket.bind((host, port))
serversocket.listen(5)

while True:
    clientsocket, addr = serversocket.accept()
    print("Accept addr: %s" % str(addr))

    msg = '欢迎访问SERVER！' + "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()