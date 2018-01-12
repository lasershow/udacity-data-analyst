#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
- まずはデータを読み込む
- サンプルとしてテスト用に読み込んで見る

"""
import xml.etree.ElementTree as ET
import os.path
import re
from collections import defaultdict
import pprint

TEST_FLAG = False
lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

if TEST_FLAG:
    file_path = "/Users/akihiro/Downloads/tokyo_suginami_sample.osm"
else:
    # 相対パスだと動かなかった ~/Downloads
    file_path = "/Users/akihiro/Downloads/suginami_tokyo.osm"

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

def process_map_key_type(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys

if __name__ == '__main__':
    # count tags data audit
    #⚠Caution (It takes a lot of time to get this result.)
    print count_tags(file_path)
    print process_map_key_type(file_path)
