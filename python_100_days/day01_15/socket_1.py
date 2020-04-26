#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/25 18:20
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : socket_1.py
# @notice ：


from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime


def main():
    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind(('127.0.0.1', 9999))
    server.listen(512)

    print('Server starting listening...')
    while True:
        client, addr = server.accept()
        print(str(addr) + 'Accepted to server.')
        client.send(str(datetime.now()).encode('utf-8'))
        client.close()


if __name__ == '__main__':
    main()