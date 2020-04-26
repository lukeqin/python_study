#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/25 20:04
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : socket_2.py
# @notice ：


from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread


def main():
    class FileTransferHandler(Thread):

        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'cf.jpg'
            my_dict['filedata'] = data
            json_str = dumps(my_dict)
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    server = socket()
    server.bind(('127.0.0.1', 9999))
    server.listen(512)
    print('Server starting listening...')
    with open('cf.jpg', 'rb') as f:
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        FileTransferHandler(client).start()


if __name__ == '__main__':
    main()