from flask import Flask
from flask import request
import psycopg2

def video_data(end_created_at, start_created_at, category):

    conn = psycopg2.connect("dbname=gravy user=xxx")
    cur = conn.cursor()
    # cur.execute("SELECT * FROM video;")
    ## 条件に合った情報を取得してくる形にする
    cur.execute(f"SELECT * FROM video WHERE created_at <= '{end_created_at}' AND created_at >= '{start_created_at}' AND category = '{category}';")
    # cur.fetchone()
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()

    video = []

    for video_info in range(len(rows)):
        video_title = rows[video_info][0]
        video_url = rows[video_info][1]
        video_view_count = rows[video_info][2]
        video_raiting  =  rows[video_info][3]
        video_post_date =  rows[video_info][4]
        video_created_at = rows[video_info][5]
        video_thumbnail_url = rows[video_info][6]
        video_category = rows[video_info][7]
        video.append({"title": video_title, 
                        "url": video_url, 
                        "view_count": video_view_count,
                        "raiting ": video_raiting ,
                        "post_date": video_post_date,
                        "created_at": video_created_at,
                        "thumbnail_url": video_thumbnail_url,
                        "category": video_category,})
    return video
#まずは元になるデータを作成します。
#内容はヘッドになるデータを入力し中身を作ります
# str_json = video
# #JSONを書き込むファイルを開く
# f = open('output.json', 'w')

# #JSONを作ります
# json.dump(str_json, f, ensure_ascii=False) #このとき気をつけないといけないのはASCIIコードを使わないということです。
# #日本語のみ使うようにします


# str_json = json.loads(str.text) #JSONデータのロード
# to_direct = str_json['ヘッド1']['Key1'] #JSONのヘッドデータからKey1を取り込む
# to_client = to_direct['Value1'] #キー値データからValueを抜き出す

## おまじない
