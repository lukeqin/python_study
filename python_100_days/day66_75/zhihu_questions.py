#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/05/03 22:19
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : zhihu_questions.py
# @notice ：


from urllib.parse import urljoin

import re
import requests

from bs4 import BeautifulSoup


def main():
    headers = {'user-agent': 'Baiduspider'}
    base_url = 'https://www.zhihu.com/'
    seed_url = urljoin(base_url, 'explore')
    resp = requests.get(seed_url, headers=headers)
    soup = BeautifulSoup(resp.text, 'lxml')
    # print(soup)
    href_regex = re.compile(r'^/question')
    link_set = set()
    for a_tag in soup.find_all('a', {'href': href_regex}):
        print(a_tag)
        if 'href' in a_tag.attrs:
            href = a_tag.attrs['href']
            full_url = urljoin(base_url, href)
            link_set.add(full_url)
    print('Total %d question pages found.' % len(link_set))


if __name__ == '__main__':
    main()