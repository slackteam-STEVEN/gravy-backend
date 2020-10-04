from apiclient.discovery import build
import psycopg2

YOUTUBE_API_KEY = 'AIzaSyBAeMYIqAd3ieYs3c33HRyPqcKI07F8HW0'

VIDEO_CATEGORY_LIST = {
	1:"Film & Animation",
	2:"Autos & Vehicles",
	# 10:"Music",
    # 15:"Pets & Animals",
    # 17:"Sports",
    # 19:"Travel & Events",
    # 20:"Gaming",
    # 22:"People & Blogs",
    # 23:"Comedy",
    # 24:"Entertainment",
    # 25:"News & Politics",
    # 26:"Howto & Style",
    # 27:"Education",
    # 28:"Science & Technology",
}

def get_youtube_info(order,video_category_id):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    search_response = youtube.search().list(
        q='',
        part='snippet',
        #視聴回数が多い順に取得
        order=order,
        type='video',
        #カテゴリ選別
        videoCategoryId=video_category_id,
        #表示する数
        maxResults=3
    ).execute()
    #search_responseをインテンド外に渡すための処理
    return search_response

for video_category_id in VIDEO_CATEGORY_LIST.keys():  #VIDEO_CATEGORY_LIST.keys() key一覧のリストを返す処理(method)
    print(VIDEO_CATEGORY_LIST[video_category_id]) #VIDEO_CATEGORY_LIST(辞書型)という変数に対してvideo_category_id(int型)という変数の値をkeyとして指定し対応するvalueを出力

    for order in ["viewCount", "rating"]:
        print(order)
        search_response = get_youtube_info(order,video_category_id)

        for result in search_response['items']:
            result["id"]["videoId"]
            youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
            #videoId取得
            videos_response = youtube.videos().list(part="id,snippet,statistics",id=result["id"]["videoId"]).execute()

            detail = videos_response.get("items", [])[0]
            print(detail["statistics"])

            statistics = detail["statistics"]
            if "viewCount" in list(statistics.keys()):
                viewCount = statistics["viewCount"]
                print("viewCount_exist")
            else:
                viewCount = "-1"
                print("viewCount_not exist")

            if "likeCount" in list(statistics.keys()):
                likeCount = statistics["likeCount"]
                print("likeCount_exist")
            else:
                likeCount = "-1"
                print("likeCount_not exist")

            print(list(statistics.keys()))

            title = detail["snippet"]["title"]
            url = 'https://www.youtube.com/watch?v=' + detail["id"]
            post_date = detail["snippet"]["publishedAt"]

            print(f"INSERT INTO video (title, url, view_count, raiting, post_date, category) VALUES ('{title}', '{url}', '{viewCount}', '{likeCount}', '{post_date}', '{video_category_id}');")




            #DB格納
            print(f"INSERT INTO video (title, url, view_count, raiting, post_date, category) VALUES ('{title}', '{url}', '{viewCount}', '{likeCount}', '{post_date}');")
            conn = psycopg2.connect("dbname=gravy user=koba")
            cur = conn.cursor()
            cur.execute(f"INSERT INTO video (title, url, view_count, raiting, post_date, category) VALUES ('{title}', '{url}', '{viewCount}', '{likeCount}', '{post_date}', '{video_category_id}');")
            cur.execute("select * from video;")
            print(cur.fetchall())
            conn.commit()
            cur.close()
            print(conn.autocommit)
            conn.close()