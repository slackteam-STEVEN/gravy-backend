# -*- coding: utf-8 -*-

# ライブラリをインポート
import os
import psycopg2
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
from get_channel_id import youtube_id


viewCount, rating = youtube_id()

DEVELOPER_KEY = "AIzaSyCHYoFt8HPBPSFoj2g43oU8c5UsZS9Z7TQ"

youtube = build("youtube", "v3", developerKey=DEVELOPER_KEY)

channel_viewCount = []
channel_rating = []

for channel_id in viewCount:
    
    channel_response = youtube.channels().list(
        part = 'snippet,statistics',
        id = channel_id
        ).execute()
        
    for channel_result in channel_response.get("items", []):
        if channel_result["kind"] == "youtube#channel":
           
            channel_viewCount.append([channel_id, channel_result["snippet"]["title"],channel_result["statistics"]["viewCount"],channel_result["statistics"]["subscriberCount"],channel_result["snippet"]["publishedAt"]])
print(channel_viewCount)

for channel_id in rating:
    
    channel_response = youtube.channels().list(
        part = 'snippet,statistics',
        id = channel_id
        ).execute()
    
    for channel_result in channel_response.get("items", []):
        if channel_result["kind"] == "youtube#channel":
           
            channel_rating.append([channel_id, channel_result["snippet"]["title"],channel_result["statistics"]["viewCount"],channel_result["statistics"]["subscriberCount"],channel_result["snippet"]["publishedAt"]])
print(channel_rating)


channel_rating
channel_rating[0]
channel_rating[0][1]



url = "https://www.youtube.com/channel/" + channel_rating[0][0]
title = channel_rating[0][1]
view_count = channel_rating[0][2]
subscribers = channel_rating[0][3]
post_date = channel_rating[0][4]

dbname = "gravy.db"
conn = psycopg2.connect("dbname=gravy user=tamadashota")
cur = conn.cursor()
#ここにfor文
for channel_viewCount_result in channel_viewCount:

    print(channel_viewCount_result)
    

cur.execute(f"INSERT INTO channel (title, url, view_count, subscribers, post_date) VALUES ('{title}', '{url}', {view_count}, {subscribers}, '{post_date}')")

conn.commit()
cur.close()
conn.close()
