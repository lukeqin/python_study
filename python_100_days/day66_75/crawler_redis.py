#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/05/04 09:30
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : crawler_redis.py
# @notice ：


from hashlib import sha1
from urllib.parse import urljoin


import pickle
import re
import requests
import zlib


from bs4 import BeautifulSoup
from redis import Redis


def main():
    base_url = 'https://www.zhihu.com/'
    seed_url = urljoin(base_url, 'explore')

    client = Redis(host='192.168.59.130', port=6379, password='12345678')
    headers = {'user-agent': 'Baiduspider'}
    resp = requests.get(seed_url, headers=headers)
    soup = BeautifulSoup(resp.text, 'lxml')
    href_regex = re.compile(r'^/question')
    hasher_proto = sha1()

    for a_tag in soup.find_all('a', {'href': href_regex}):
        href = a_tag.attrs['href']
        full_url = urljoin(base_url, href)
        hasher = hasher_proto.copy()
        hasher.update(full_url.encode('utf-8'))
        field_key = hasher.hexdigest()

        if not client.hexists('zhihu', field_key):
            html_page = requests.get(full_url, headers=headers).text
            zipped_page = zlib.compress(pickle.dumps(html_page))
            client.hset('zhihu', field_key, zipped_page)
    print('Total %d question pages found.' % client.hlen('zhihu'))


if __name__ == '__main__':
    main()