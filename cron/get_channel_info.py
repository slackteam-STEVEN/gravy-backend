# -*- coding: utf-8 -*-

# ライブラリをインポート
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
from test2 import youtube_id
videos, rating = youtube_id()

DEVELOPER_KEY = "xxx"
ID = "youtube_id"
youtube = build("youtube", "v3", developerKey=DEVELOPER_KEY)
videos_response = youtube.videos().list(part="id,snippet,statistics",id=ID).execute()
#videos = []

channel_response = youtube.channels().list(
    part = 'snippet,statistics',
    id = ID
    ).execute()

channels = []

for channel_result in channel_response.get("items", []):
    if channel_result["kind"] == "youtube#channel":
        print(channel_result["statistics"])
        channels.append([channel_result["snippet"]["title"],channel_result["statistics"]["subscriberCount"],channel_result["statistics"]["viewCount"],channel_result["snippet"]["publishedAt"]])
print(channels)

# while True:
#     if nextPagetoken != None:
#         nextpagetoken = nextPagetoken

#         search_response = youtube.search().list(
#         part = "snippet",
#         channelId = ID,
#         maxResults = 50,
#         order = "date", #日付順にソート
#         pageToken = nextpagetoken #再帰的に指定
#         ).execute()
 
#     for search_result in search_response.get("items", []):
#         if search_result["id"]["kind"] == "youtube#video":
#             searches.append(search_result["id"]["videoId"])

#     try:
#         nextPagetoken =  search_response["nextPageToken"]
#     except:
#         break

# dbname = "gravy.db"
# conn = get_connection()
# cur = conn.cursor()
# cur.execute('')
# cur.close()
# conn.close()
