#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/18 14:38
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : xml_parse_dom.py
# @notice ：


from xml.dom.minidom import parse
import xml.dom.minidom


DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print("Root element : %s" % collection.getAttribute("shelf"))

movies = collection.getElementsByTagName("movie")

for movie in movies:
    print("+++Movie+++")
    if movie.hasAttribute("title"):
        print("Title: %s" % movie.getAttribute("title"))

    type = movie.getElementsByTagName('type')[0]
    print("Type: %s" % type.childNodes[0].data)
    format = movie.getElementsByTagName('format')[0]
    print("format: %s" % format.childNodes[0].data)
    rating = movie.getElementsByTagName('rating')[0]
    print("rating: %s" % rating.childNodes[0].data)
    description = movie.getElementsByTagName('description')[0]
    print("description: %s" % description.childNodes[0].data)