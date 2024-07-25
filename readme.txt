ディレクトリ内のテキストファイルのエンコーディング一覧を出力するツール

前提環境
python3と，下記ライブラリがインストールされている必要があります．
・chardet
・glob
・sys
・pandas as pd
・numpy as np
・os

初期設定:

まずはCLIのカレントディレクトリをこのディレクトリとし，必要なライブラリーをpython環境にインストールします．

---
cd <このディレクトリへのパス>
pip install -r requirements.txt
---


使い方:

python3が使えるコマンドライン上で，下記コマンドを実行します．

---
python detect_encoding.py <テキストファイルが入ったディレクトリへのパス> <検知結果のCSVを出力するディレクトリへのパス>
---

例:
---
python detect_encoding.py texts_test texts_test
---

<テキストファイルが入ったディレクトリへのパス>※必須: 例: "./text_directory" "/home/shiroto/text_directory" など
<検知結果のCSVを出力するディレクトリへのパス>: 例: "out_directory" "/home/shiroto/out_directory" など．入力を省略した場合はコマンドを実行したディレクトリに出力されます．

実行すると，<検知結果のCSVを出力するディレクトリへのパス>に，「endocings_in_directory_<テキストファイルが入ったディレクトリ名>.csv」というCSVファイルが出力されます．
下記のような形式です．

---
,ファイル名,文字コード
0,test1_UTF8.txt,utf-8
1,test3_UTF8.txt,utf-8
2,test2_SJIS.txt,SHIFT_JIS

---

上記ファイルをExcelなどで開くことで，ファイルごとのエンコーディングが分かります．


2024年7月25日 白石研白戸作成 