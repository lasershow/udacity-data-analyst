# coding: utf-8

import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
TEST_FLAG = False

if TEST_FLAG:
    OSMFILE = "/Users/akihiro/Downloads/tokyo_suginami_sample.osm"
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
            'インターチェンジ': 'IC',
            'ＩＣ': 'IC',
            'ＪＣＴ': 'JCT',
            'ジャンクション': 'JCT',
            }

def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


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


def update_name(name, mapping):
    keys = mapping.keys()
    for key in keys:
        if key in name:
            print mapping[key]
            return re.sub(key, mapping[key], name)
    return name


def test():
    st_types = audit(OSMFILE)
    # assert len(st_types) == 3
    pprint.pprint(dict(st_types))

    for st_type, ways in st_types.iteritems():
        for name in ways:
            better_name = update_name(name, mapping)
            print name, "=>", better_name

if __name__ == '__main__':
    test()
