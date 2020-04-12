#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/12 23:11
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : client.py
# @notice ：


import socket
import sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
print(host)
port = 9999

s.connect((host, port))

msg = s.recv(1024)
s.close()

print(msg.decode('utf-8'))