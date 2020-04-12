#-*- coding: UTF-8 -*-
'''
Created on 2017年3月11日
@author: luke
'''

import random
import redis

db = redis.Redis(host='127.0.0.1', port=6379)
for i in range(100):
    n = random.randint(-10000, 10000)
    db.set(i, n)
    print db.get(i)