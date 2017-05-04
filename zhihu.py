#-*- coding: UTF-8 -*-
'''
Created on 2017年3月15日
@author: luke
'''

import sys
import urllib2
from BeautifulSoup import BeautifulSoup
import MySQLdb                                                                                           
import _mysql_exceptions
reload(sys)
sys.setdefaultencoding("utf-8")

class MysqlHhlper(object):
    def __init__(self):
        self.__Host = 'localhost'
        self.__User = 'root'
        self.__Passwd = 'xx'
        self.__Db = 'zhihu'

    def __Conn(self):
        try:
            conn = MySQLdb.connect(host=self.__Host, user=self.__User, passwd=self.__Passwd, db=self.__Db, port=3306, charset="utf8")
        except Exception, e:
            conn = None
        return conn

    def myread(self, sql):
        conn = self.__Conn()
        if not conn:
            return None
        try:
            cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
            cur.execute(sql,)
            data = cur.fetchall()
        except Exception,e: 
            data = None
        finally:
            cur.close()
            conn.close()
        return data

    def mywrite(self, sql, tname):
        conn = self.__Conn()
        if not conn:
            return None
        try:
            cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
            cur.execute(sql, tname)
        except Exception,e: 
            return None
        finally:
            conn.commit()
            cur.close()
            conn.close()
        return 0

class MysqlNav(object):
    def __init__(self):
        self.__nav = MysqlHhlper()

    def readhotopic(self):
        sql = "select * from hotopic"
        return self.__nav.myread(sql)

    def writehotopic(self, tname):
        sql = "insert into hotopic(QNAME) values(%s)"
        params = (tname,)
        return self.__nav.mywrite(sql, params)

if __name__ == '__main__':
    url = "https://www.zhihu.com/topic/19607535"
    page = urllib2.urlopen(url)     
    soup = BeautifulSoup(page)  
    data = soup.findAll(attrs = {'class' : ['question_link']})

    t = MysqlNav()

    for i in data:
        if i.string:
            tname = i.string.strip()
            t.writehotopic(tname)
    
    d = t.readhotopic()
    for i in range(len(d)):
        for k,v in d[i].items():
            print k, v



