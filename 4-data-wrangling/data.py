#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
- まずはデータを読み込む
- サンプルとしてテスト用に読み込んで見る

"""
import xml.etree.ElementTree as ET
import os.path
test_flag = False

if test_flag == True:
    file_path = "/Users/akihiro/Downloads/tokyo_suginami_sample.osm"
else:
    # 相対パスだと動かなかった ~/Downloads
    file_path = "/Users/akihiro/Downloads/tokyo_japan.osm"

def get_root(file_name):
    # データが大きすぎる
    for event, elem in ET.iterparse(file_path):
        print(event, elem)
    return

if __name__ == '__main__':
    # パス確認用
    print(os.path.expanduser('~'))
    print(get_root(file_path))
