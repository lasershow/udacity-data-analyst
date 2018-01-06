## csvの読み込み

`公式ドキュメント`
https://docs.python.jp/3/tutorial/inputoutput.html
python2
https://docs.python.org/2/library/csv.html#csv.reader

`Pythonのwithステートメントのまとめ`
http://shin.hateblo.jp/entry/2013/03/23/211750

```py
with open("filename", "r") as file:
  whole_str = file.read()
```

file.read([size])で指定したバイト数を読み込み。size未指定の場合はすべて読み込み。
file.readline()で1行読み込み。文字列に改行文字は残る。最後の行を読み込んだ後に””（空文字）がかえる。
file.readlines()で全行を読み込んでリストを返す。

https://python.civic-apps.com/file-io/

`r`
読み込み

※そもそもなぜファイル読み込みが必要なのか

- 読み込まないと使えない！
- pandasとか使ってるとめんどくさってなるよね（ブラックボックス）

※ファイルをクローズしないと何が起こる？

`with を使うと、処理中に例外が発生しても必ず最後にファイルを閉じることができます。`
https://tonari-it.com/python-with-file-open-close/

### 使用しているデータについて

http://rredc.nrel.gov/solar/old_data/nsrdb/1991-2005/tmy3/by_USAFN.html

### csv reader

`公式`
https://docs.python.jp/2.7/library/csv.html
