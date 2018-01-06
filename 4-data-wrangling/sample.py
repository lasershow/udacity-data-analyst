#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
- まずはデータを読み込む
- サンプルとしてテスト用に読み込んで見る

"""
import xml.etree.ElementTree as ET
import os.path
import pprint
import re

test_flag = True
lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')


if test_flag == True:
    # file_path = "/Users/akihiro/Downloads/exampleresearcharticle.xml"
    file_path = "/Users/akihiro/Downloads/tokyo_suginami_sample.osm"
else:
    # 相対パスだと動かなかった ~/Downloads
    file_path = "/Users/akihiro/Downloads/tokyo_japan.osm"

def get_root(file_name):
    # データが大きすぎる
    for event, elem in ET.iterparse(file_path):
        print(event, elem)
    return

def count_tags(filename):
    tags = {}
    for event, elem in ET.iterparse(filename):
        if not elem.tag in tags.keys():
            # print "------new key"
            tags[elem.tag] = 1
        else:
            tags[elem.tag] += 1
    return tags

def key_type(element, keys):
    if element.tag == "tag":
        # print element.get('k')
        k = element.attrib['k']
        if lower.search(k):
            keys["lower"] += 1
        elif lower_colon.search(k):
            keys["lower_colon"] += 1
        elif problemchars.search(k):
            keys["problemchars"] += 1
        else:
            keys["other"] += 1

    return keys

def get_user(element):
    return element.attrib['uid']


def process_map_user(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        if element.get('uid'):
            users.add(get_user(element))
    return users


def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys


if __name__ == '__main__':
    # パス確認用
    # tree = ET.parse(file_path)
    # root = tree.getroot()
    # for child in root:
    #     print child.tag
    print(count_tags(file_path))
    print(process_map(file_path))
