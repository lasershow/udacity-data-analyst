# coding: utf-8

import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
TEST_FLAG = True

if TEST_FLAG:
    OSMFILE = "tokyo-sample.osm"
else:
    OSMFILE = "/Users/akihiro/Downloads/suginami_tokyo.osm"

expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road",
            "Trail", "Parkway", "Commons"]

# UPDATE THIS VARIABLE
mapping = { "St": "Street",
            "St.": "Street",
            'Ave': "Avenue",
            'Rd.': 'Road',
            'Sta.': 'Station',
            'Ent.': 'Entrance',
            'brdg.': 'Bridge',
            'udagawacho': '宇田川町',
            'takadanobaba': '高田馬場',
            'sakuragaoka-cho': '桜ヶ丘町',
            'dogenzaka': '道玄坂',
            'jingumae': '神宮前',
            'shinsen': '神泉',
            'Nerima': '練馬',
            'Omotesando': '表参道',
            'Matsubara': '松原'
            }

def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

def is_station_name(elem):
    return (elem.attrib['k'] == "motorway_junction")

def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types


def update_name(name):
    keys = mapping.keys()
    for key in keys:
        if key in name:
            print mapping[key]
            try:
                re.sub(key, mapping[key], name)
            except UnicodeDecodeError:
                return re.sub(key, mapping[key], name.encode('utf-8'))
                print "UnicodeDecodeError"
            else:
                return re.sub(key, mapping[key], name)
    return name


if __name__ == '__main__':
    st_types = audit(OSMFILE)
    pprint.pprint(dict(st_types))

    for st_type, ways in st_types.items():
        for name in ways:
            better_name = update_name(name)
            print name, "=>", better_name
