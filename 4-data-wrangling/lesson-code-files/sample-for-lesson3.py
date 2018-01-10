#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
- まずはデータを読み込む
- サンプルとしてテスト用に読み込んで見る

"""
import xml.etree.ElementTree as ET
import os.path
test_flag = True

file_path = "/Users/akihiro/Downloads/exampleresearcharticle.xml"

#読み込み
tree = ET.parse(file_path)

# rootを取得し、出力
root = tree.getroot()
print "-----root child tag-----"
for child in root:
    print child.tag

#rootからさらに絞込
text = root.find("./fm/bibl/title")
print "-----./fm/bibl/title-----"
for p in text:
    # <Element 'p' at 0x104115d90> pだけだとタグが入力になる
    print p.text
