#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/25 20:16
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : client_2.py
# @notice ：


from socket import socket
from json import loads
from base64 import b64decode


def main():
    client = socket()
    client.connect(('127.0.0.1', 9999))

    in_data = bytes()
    data = client.recv(1024)
    while data:
        in_data += data
        data = client.recv(1024)

    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')
    with open('./' + filename, 'wb') as f:
        f.write(b64decode(filedata))
    print('Pic was saved.')


if __name__ == '__main__':
    main()