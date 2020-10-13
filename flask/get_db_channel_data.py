from flask import Flask
from flask import request
import psycopg2

conn = psycopg2.connect("dbname=gravy user=xxx")
cur = conn.cursor()
# cur.execute("SELECT * FROM video;")
## 条件に合った情報を取得してくる形にする
cur.execute("SELECT * FROM channel;")
# cur.fetchone()
rows = cur.fetchall()
conn.commit()
cur.close()
conn.close()

channel = []


for channel_info in range(len(rows)):
    channel_title = rows[channel_info][0]
    channel_url = rows[channel_info][1]
    channel_view_count = rows[channel_info][2]
    channel_subscribers =  rows[channel_info][3]
    channel_post_date =  rows[channel_info][4]
    channel_created_at = rows[channel_info][5]
    channel_thumbnail_url = rows[channel_info][6]
    
    channel.append({"title": channel_title, 
                    "url": channel_url, 
                    "view_count": channel_view_count,
                    "subscribers": channel_subscribers,
                    "post_date": channel_post_date,
                    "created_at": channel_created_at,
                    "thumbnail_url": channel_thumbnail_url})
#まずは元になるデータを作成します。
#内容はヘッドになるデータを入力し中身を作ります
str_json = channel
# #JSONを書き込むファイルを開く
# f = open('output.json', 'w')

# #JSONを作ります
# json.dump(str_json, f, ensure_ascii=False) #このとき気をつけないといけないのはASCIIコードを使わないということです。
# #日本語のみ使うようにします


# str_json = json.loads(str.text) #JSONデータのロード
# to_direct = str_json['ヘッド1']['Key1'] #JSONのヘッドデータからKey1を取り込む
# to_client = to_direct['Value1'] #キー値データからValueを抜き出す

## おまじない
