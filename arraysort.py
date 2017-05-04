#-*- coding: UTF-8 -*-
'''
Created on 2017年3月13日
@author: luke
'''

dict = [
    {'id':'4','name':'b'},
    {'id':'6','name':'c'},
    {'id':'3','name':'a'},
    {'id':'1','name':'g'},
    {'id':'8','name':'f'}
]

'''1'''
dict.sort(lambda x,y: cmp(x['id'], y['id']))    

'''2'''
newdict = sorted(dict, key=lambda x:x['id']) 

'''
[{'id': '1', 'name': 'g'}, 
{'id': '3', 'name': 'a'}, 
{'id': '4', 'name': 'b'}, 
{'id': '6', 'name': 'c'}, 
{'id': '8', 'name': 'f'}]
'''

'''
Python对容器内数据的排序有两种，一种是容器自己的sort函数，一种是内建的sorted函数。
sort函数和sorted函数唯一的不同是，sort是在容器内排序，sorted生成一个新的排好序的容器.
'''