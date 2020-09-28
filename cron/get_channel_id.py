from googleapiclient.discovery import build

YOUTUBE_API_KEY = 'xxx'

def youtube_id():

    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    search_viewCount = youtube.search().list(
    part='snippet',
    #視聴回数が多い順に取得
    order='viewCount',
    type='channel',
    #表示する数
    maxResults=50
    ).execute()

    search_rating = youtube.search().list(
    part='snippet',
    #高評価が多い順に取得
    order='rating',
    type='channel',
    #表示する数
    maxResults=50
    ).execute()
    #出力
    #print(search_viewCount['items'])
    #print(search_rating['items'])
    #print(len(search_viewCount['items']))
    videos = []

    for result in search_viewCount['items']:
        #print(result)
        #print(result["id"])
        #print(result["id"]["channelId"])    
        videos.append(result["id"]["channelId"])
    
    rating = []

    for result in search_rating['items']:
        #print(result)
        #print(result["id"])
        #print(result["id"]["channelId"])    
        rating.append(result["id"]["channelId"])
    return videos ,rating