#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/18 15:33
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : python_time.py
# @notice ：


import time

# current time
ticks = time.time()
print("Current time: ", ticks)


# local time
localtime = time.localtime(time.time())
print("Local time: ", localtime)


# asctime
localtime = time.asctime(time.localtime(time.time()))
print(localtime)


# strftime
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strftime("%A %b %d %H:%M:%S %Y", time.localtime()))

a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))


# calendar
import calendar


cal = calendar.month(2016, 1)
print(" 2016 1 :")
print(cal)


# time module
# time altzone
print("time.altzone: %d" % time.altzone)
# time asctime
print("time.asctime(time.localtime()): %s" % time.asctime(time.localtime()))
# time clock
print(time.perf_counter())
print(time.process_time())
# time.ctime
print("time.ctime(): %s" % time.ctime())
# time.gmtime
print("gmtime: ", time.gmtime())
# time.sleep
print("Start: %s" % time.ctime())
#time.sleep(0.5)
print("End: %s" % time.ctime())
# time.strftime and time.strptime
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("返回元组: ", time.strptime("30 Nov 00", "%d %b %y"))
# time zone and tzname
print(time.timezone)
print(time.tzname)


# clander
print(calendar.calendar(2020,w=2,l=1,c=6))
# firstweekday
print(calendar.firstweekday)
# isleap
print(calendar.isleap(2020))
# leapdays
print(calendar.leapdays(2000, 2020))
# month
print(calendar.month(2020, 5, w=2, l=1))
# monthcalendar
print(calendar.monthcalendar(2020, 4))
# monthrange
print(calendar.monthrange(2020, 1))
# prcal
print(calendar.prcal(2020, w=2, l=1, c=6))
# prmonth
print(calendar.prmonth(2020, 2, w=2, l=1))
# calender week day
print(calendar.weekday(2020, 4, 18))