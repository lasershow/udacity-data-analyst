# OpenStreetMap Data Case Study

### Map Area
Tokyo, Japan

- [mapzen tokyo](https://mapzen.com/data/metro-extracts/metro/tokyo_japan/)

## Problems Encountered in the Map

After initially downloading a small sample size of the Tokyo area and running it against a provisional data.py file, I noticed five main problems with the data, which I will discuss in the following order:

<!-- まずは小さいデータを使用して、問題点を把握してみる。 -->
<!-- osmをxmlに変換する -->

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

```
監査が完了したら、次にSQLデータベースに挿入するデータを準備します。
これを行うには、OSM XMLファイルの要素を解析し、それらを文書形式から
表形式に変換し、.csvファイルに書き込むことができます。これらのcsvファイルは、
テーブルとしてSQLデータベースにインポートされます。

この変換のプロセスは次のとおりです。
- iterparseを使用して、XMLの各トップレベル要素を繰り返し実行します
- カスタム関数を使用して各要素を複数のデータ構造に整形する
- スキーマおよび検証ライブラリを利用して、変換されたデータが正しい形式であることを確認する
- 各データ構造を適切な.csvファイルに書き込む

データをロードし、反復的な解析を実行し、
csvファイルに出力します。あなたの仕事はそれぞれを変換するshape_element関数を完了することです
要素を正しい形式に変換します。このプロセスを簡単にするために、すでにスキーマを定義しています（
.csvファイルと最終的なテーブルの最後のコードタブのschema.pyファイル）。を使用する
cerberusライブラリこのスキーマに対する出力をensすることができます
```

- 監査を行う(ケーススタディから学ぶ)
