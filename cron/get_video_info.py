#from apiclient.discovery import build
from googleapiclient.discovery import build
import psycopg2

YOUTUBE_API_KEY = 'XXXXXXXXX'

VIDEO_CATEGORY_LIST = {
	1:"Film & Animation",
	2:"Autos & Vehicles",
	10:"Music",
    15:"Pets & Animals",
    17:"Sports",
    19:"Travel & Events",
    20:"Gaming",
    22:"People & Blogs",
    23:"Comedy",
    24:"Entertainment",
    25:"News & Politics",
    26:"Howto & Style",
    27:"Education",
    28:"Science & Technology",
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
        maxResults=10
    ).execute()
    #search_responseをインテンド外に渡すための処理
    return search_response

for video_category_id in VIDEO_CATEGORY_LIST.keys():  #VIDEO_CATEGORY_LIST.keys() key一覧のリストを返す処理(method)

    for order in ["viewCount", "rating"]:
        search_response = get_youtube_info(order,video_category_id)

        for result in search_response['items']:
            result["id"]["videoId"]
            youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
            #videoId取得
            videos_response = youtube.videos().list(part="id,snippet,statistics",id=result["id"]["videoId"]).execute()

            detail = videos_response.get("items", [])[0]

            statistics = detail["statistics"]
            if "viewCount" in list(statistics.keys()):
                viewCount = statistics["viewCount"]
            else:
                viewCount = "-1"

            if "likeCount" in list(statistics.keys()):
                likeCount = statistics["likeCount"]
            else:
                likeCount = "-1"

            title = detail["snippet"]["title"]
            title = title.replace("'", "").replace('"', '')
            url = 'https://www.youtube.com/watch?v=' + detail["id"]
            post_date = detail["snippet"]["publishedAt"]
            thumbnail_url =detail["snippet"]["thumbnails"]["medium"]["url"]


            #DB格納
            conn = psycopg2.connect("host=XXX.XXX.XXX.100 dbname=gravy user=XXXX port=5432 password=XXXXXX")
            cur = conn.cursor()
            cur.execute(f"INSERT INTO video (title, url, view_count, raiting, post_date, category, thumbnail_url) VALUES ('{title}', '{url}', '{viewCount}', '{likeCount}', '{post_date}', '{video_category_id}', '{thumbnail_url}');")
            conn.commit()
            cur.close()
            conn.close()
            print("success")