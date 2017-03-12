#-*- coding: UTF-8 -*-
'''
Created on 2017年3月11日
@author: luke
'''

    
if 1 in [1, 0] == True:
    print 'a'
else:
    print 'b'  

'''
输出是b
'''


if (1 in [1, 0]) == True:
    print 'a'
else:
    print 'b'
    
'''
输出是a，如果没有（）会先[1, 0] == True，结果是False
'''
