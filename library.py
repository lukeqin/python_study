#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/03/20 20:32
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : library.py
# @notice ：


# operating system interface
import os
print(os.getcwd())
os.chdir("C:\dev")
print(os.getcwd())
# print(os.system('mkdir today'))


# import argparse
#
# parser = argparse.ArgumentParser(prog = 'top',
#     description = 'Show top lines from each file')
# parser.add_argument('filenames', nargs='+')
# parser.add_argument('-l', '--lines', type=int, default=10)
# args = parser.parse_args()
# print(args)


# from urllib.request import urlopen
# for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
#     line = line.decode('utf-8')  # Decoding the binary data to text.
#     if 'EST' in line or 'EDT' in line:  # look for Eastern Time
#         print(line)


