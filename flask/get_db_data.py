from flask import Flask
from flask import request
import psycopg2

conn = psycopg2.connect("dbname=gravy user=sadakatafuyuno")
cur = conn.cursor()
cur.execute("SELECT * FROM video;")
cur.execute("SELECT * FROM channel;")
cur.fetchone()
conn.commit()
cur.close()
conn.close()

#まずは元になるデータを作成します。

#まずは元になるデータを作成します。
#内容はヘッドになるデータを入力し中身を作ります
str_json = {
    "ヘッド1":{
        "Key1": Value1,
        "Key2": "Value2"
    },
    "ヘッド2":{
        "Key1": Value1,
        "Key2": "Value2"
    },
    "ヘッド3":{
        "Key1": Value1,
        "Key2": "Value2"
    }
}

#JSONを書き込むファイルを開く
f = open('output.json', 'w')

#JSONを作ります
json.dump(str_json, f, ensure_ascii=False) #このとき気をつけないといけないのはASCIIコードを使わないということです。
#日本語のみ使うようにします


str_json = json.loads(str.text) #JSONデータのロード
to_direct = str_json['ヘッド1']['Key1'] #JSONのヘッドデータからKey1を取り込む
to_client = to_direct['Value1'] #キー値データからValueを抜き出す

## おまじない
