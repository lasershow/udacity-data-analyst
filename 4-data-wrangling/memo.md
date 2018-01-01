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
i.attrib["iid"] で オプションにアクセスできる
```
