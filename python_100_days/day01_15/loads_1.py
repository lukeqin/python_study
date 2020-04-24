#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/24 22:25
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : loads_1.py
# @notice ：


import requests
import json


def main():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])


if __name__ == '__main__':
    main()