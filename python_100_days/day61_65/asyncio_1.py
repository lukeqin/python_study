#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/05/03 16:08
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : asyncio_1.py
# @notice ：


import asyncio


async def fetch(host):
    print(f'Start fetching {host}\n')
    reader, write = await asyncio.open_connection(host, 80)
    write.write(b'GET / HTTP/1.1\r\n')
    write.write(f'Host: {host}\r\n'.encode())
    write.write(b'\r\n')
    await write.drain()
    line = await reader.readline()
    while line != b'\r\n':
        print(line.decode().rstrip())
        line = await reader.readline()
    print('\n')
    write.close()

def main():
    urls = ('www.sohu.com', 'www.douban.com', 'www.163.com')
    loop = asyncio.get_event_loop()
    tasks = [fetch(url) for url in urls]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == '__main__':
    main()