## osmについて

```
less osmファイル
```

で普通に見れる

## 反復解析
タグを繰り返し実行して、タグを取り出す。
lesson3に詳しくあるらしい

```py
# 一度rootを取得する必要がある？
# 複数のタグがあるので、さらにタグをfindしなければならない？
def get_authors(root):
    authors = []
    for author in root.findall('./fm/bibl/aug/au'):
        data = {
                "fnm": None,
                "snm": None,
                "email": None,
                "insr": []
        }
        data["fnm"] = author.find('./fnm').text
        data["snm"] = author.find('./snm').text
        data["email"] = author.find('./email').text
        insr = author.findall('./insr')
        for i in insr:
            data["insr"].append(i.attrib["iid"])
        authors.append(data)

    return authors
```

```
i.attrib["iid"] で オプションにアクセスできるs
```

## osmのドキュメントを見る

特有のXMLを把握する必要がある

https://wiki.openstreetmap.org/wiki/JA:%E3%83%8E%E3%83%BC%E3%83%89
https://wiki.openstreetmap.org/wiki/JA:%E3%82%A6%E3%82%A7%E3%82%A4
https://wiki.openstreetmap.org/wiki/JA:%E3%83%AA%E3%83%AC%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3

```
ノードは OSM スキームでの基本要素であり、他の要素の構成単位となるものです。ノードは緯度と経度（単一の地理座標）で構成されます。（オプションで標高ele=*を含むことも可能です。）
ノードはウェイ（後述）を定義するために必要ですが、ノード単体でも、例えば電話ボックス、パブなどの全てのPOIを表すことができます。単体ノードには、例えば amenity=telephone など、少なくとも1つのタグを付けなくてはなりません。
通常、ウェイを構成するノードはそれ自身のタグを持ちません（タグはウェイを記述するためだけに用いられています）。しかし、これはルールではありません。例えば、railway=rail タグの付いたウェイが railway=station タグの付いたノードを含むこともできます。
```

- rootのタグを取得する
- rootのタグに含まれる、ネストされたものを取得する
- 読み込む際の条件を変更する、開始タグを設定する

- 反復解析
- タグの種類の解析

## pythonの正規表現

https://docs.python.jp/3/library/re.html

```py
prog = re.compile(pattern)
result = prog.match(string)
```

### searchとmatchの違い

match(pattern, string)	文字列の先頭で正規表現とマッチするか判定します。
search(pattern, string)	文字列を操作して、正規表現がどこにマッチするか調べます。

### event start endについて
https://discussions.udacity.com/t/what-does-the-parameter-events-start-mean/171946/2
