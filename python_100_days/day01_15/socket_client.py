#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/25 18:27
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : socket_client.py
# @notice ：


from socket import socket


def main():
    client = socket()
    client.connect(('127.0.0.1', 9999))
    print(client.recv(1024).decode('utf-8'))
    client.close()


if __name__ == '__main__':
    main()