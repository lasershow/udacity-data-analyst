# OpenStreetMap Data Case Study

### Map Area
Suginami,Tokyo,Japan

- [mapzen tokyo](https://mapzen.com/data/metro-extracts/metro/tokyo_japan/)

## Problems Encountered in the Map
After initially downloading a small sample size of the Tokyo area and running it against a provisional data.py file, I noticed five main problems with the data, which I will discuss in the following order:

<!-- まずは小さいデータを使用して、問題点を把握してみる。 -->
<!-- osmをxmlに変換する -->

- The same thing, but various names and abbreviations are used.

`ex`

```xml
<tag k="name" v="有明ジャンクション"/>
<tag k="highway" v="motorway_junction"/>

<tag k="name" v="芝浦JCT"/>
<tag k="highway" v="motorway_junction"/>

<tag k="name" v="成田ＪＣＴ"/>
```

`ex2`

```xml
<tag k="wikipedia" v="ja:川口東インターチェンジ"/>
<tag k="name" v="千葉北ＩＣ"/>
<tag k="name" v="湾岸習志野IC"/>
```

- Japanese is used for Japanese data set. Therefore, it may be necessary to perform processing specific to Japanese.(Russian and many other languages are included.
)

`ex`

```xml
<tag k="name" v="下高井戸敬老会館"/>

 <node id="31236676" lat="35.634834" lon="139.7687577" version="3" timestamp="2014-12-07T22:38:59Z" changeset="27322515" uid="571410" user="Павел Гетманцев"/>
```

- High way where class is not registered

`ex`

```xml
<tag k="highway" v="unclassified"/>
```

- Mysterious note

`ex`

```xml
<tag k="note" v="estimated"/>
```

- abbreviation

`ex`

```xml
<tag k="name" v="府中駅北口"/>
<tag k="highway" v="traffic_signals"/>
<tag k="name:en" v="Fuchu Station North Entrance"/>

<tag k="name" v="西府駅入口"/>
<tag k="name:en" v="Nishifu Sta. Ent."/>

<tag k="name" v="日野橋"/>
<tag k="name:en" v="Hino brdg."/>
```

## Data Audit
First of all, I decided to audit the XML file.
TODO

`data.py`

### Unique Tags
As the beginning of the audit, I measured unique tags.

```py
{'node': 864177, 'nd': 1055982, 'bounds': 1, 'member': 15818, 'tag': 560767, 'relation': 791, 'way': 171563, 'osm': 1}
```

### Patterns in the Tags
Then I examined the type of tag.

```py
{'problemchars': 0, 'lower': 498542, 'other': 9043, 'lower_colon': 53182}
```

### Change to the correct name

`python3-code/audit.py`

```
udagawacho → '宇田川町'
takadanobaba → '高田馬場'
sakuragaoka-cho →　'桜ヶ丘町'
dogenzaka → '道玄坂'
jingumae →　'神宮前'
shinsen → '神泉'
Matsubara →　'松原'
Nerima → '練馬'
Omotesando → '表参道'
```

## Process your Dataset

### data to csv
Converting data from XML to CSV format. Then import the cleaned .csv files into a SQL database

`data_to_csv.py`

### create database

`create_database.py`

## Explore your Database

`query.py`

- size of the file
- number of unique users
- number of nodes and ways
- number of chosen type of nodes, like cafes, shops etc.


### size of the file
### number of unique users

`query.py`

```sql
sqlite> SELECT COUNT(DISTINCT(e.uid))          
FROM (SELECT uid FROM nodes UNION ALL SELECT uid FROM ways) e;
```

```
Number of unique users:  15
```

### number of nodes and ways

```sql
sqlite> SELECT COUNT(*) FROM nodes
```

```sql
sqlite> SELECT COUNT(*) FROM ways
```

```
Number of nodes:  815
Number of ways:  184
```

### number of chosen type of nodes, like cafes, shops etc.

`Top contributing users`

```sql
sqlite> SELECT e.user, COUNT(*) as num
FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e
GROUP BY e.user
ORDER BY num DESC
LIMIT 10;
```

```
Top contributing users:  [(u'roguish', 233), (u'ribbon', 196), (u'Nahainec', 186), (u'yoshitk', 142), (u'kurauchi', 113), (u'futurumspes', 90), (u'TCGshinta', 24), (u'luschi', 4), (u'RichRico', 2), (u'Rub21', 2)]
```

## Ideas for additional improvements

I will describe two additional problems related to improvement.

`The value of input varies depending on the person.`

We should prepare some conventions for those who register. For example IC, ic,インターチェンジ unified in IC.

By preparing the document, human error can be reduced much. However, man-hours to prepare the document and human cost to execute it occur.

`Even the same thing means that the number of input information is different.`

Likewise, Should be suggested to some extent what value should be entered.We can not remember this, so I think that it is better to encourage using the system.For example, when you enter a bridge, items to be entered are displayed.

By doing this you can bring consistency to the data set. Unity will bring good results for data analysis such as EDA.

However, because data unification requires knowledge of all tags, considerable preprocessing time is taken into account.

## Files

- tokyo_sample.osm : sample data of the OSM file
- data.py : data audit about measure tags and tag types
- python3-code/audit.py : audit street, city and update their names
- database.py : create database of the CSV files
- schema.py : database schema file
- mapparser.py : find unique tags in the data
- query.py : different queries about the database using SQL
- report.pdf : pdf of this document
- sample.py : extract sample data from the OSM file
- tags.py : count multiple patterns in the tags

### File size
Project OSM file size is about 60MB
