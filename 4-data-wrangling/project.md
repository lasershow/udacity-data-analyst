# OpenStreetMap Data Case Study

### Map Area
Tokyo, Japan

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


### Unique Tags
As the beginning of the audit, I measured unique tags.


### Patterns in the Tags
Then I examined the type of tag.

## Change to the correct name

```
Sta.
Ent.
brdg.
インターチェンジ
ＩＣ
ＪＣＴ
ジャンクション
```
