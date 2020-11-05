# -*- coding: utf-8 -*-

# ライブラリをインポート
import os
import psycopg2
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
from get_channel_id import youtube_id


viewCount, rating = youtube_id()

DEVELOPER_KEY = "xxx"

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

            channel_viewCount.append([channel_id, channel_result["snippet"]["title"],channel_result["statistics"]["viewCount"],channel_result["statistics"]["subscriberCount"],channel_result["snippet"]["publishedAt"],channel_result["snippet"]["thumbnails"]["medium"]["url"]])
print(channel_viewCount)

for channel_id in rating:

    channel_response = youtube.channels().list(
        part = 'snippet,statistics',
        id = channel_id
        ).execute()

    for channel_result in channel_response.get("items", []):
        if channel_result["kind"] == "youtube#channel":

            channel_rating.append([channel_id, channel_result["snippet"]["title"],channel_result["statistics"]["viewCount"],channel_result["statistics"]["subscriberCount"],channel_result["snippet"]["publishedAt"],channel_result["snippet"]["thumbnails"]["medium"]["url"]])
print(channel_rating)


dbname = "gravy.db"
conn = psycopg2.connect("host=XXX.XXX.XXX.100 dbname=gravy user=XXXX port=5432 password=XXXXXX")
cur = conn.cursor()
#ここにfor文
for channel_viewCount_result in channel_viewCount:
    print(channel_viewCount_result)
    url = "https://www.youtube.com/channel/" + channel_viewCount_result[0]
    title = channel_viewCount_result[1]
    view_count = channel_viewCount_result[2]
    subscribers = channel_viewCount_result[3]
    post_date = channel_viewCount_result[4]
    thumbnail_url = channel_viewCount_result[5]
    sql = f"INSERT INTO channel (title, url, view_count, subscribers, post_date,thumbnail_url) VALUES ('{title}', '{url}', {view_count}, {subscribers}, '{post_date}', '{thumbnail_url}')"
    cur.execute(sql)

for channel_rating_result in channel_rating:
    url = "https://www.youtube.com/channel/" + channel_viewCount_result[0]
    title = channel_viewCount_result[1]
    view_count = channel_viewCount_result[2]
    subscribers = channel_viewCount_result[3]
    post_date = channel_viewCount_result[4]
    thumbnail_url = channel_rating_result[5]
    sql = f"INSERT INTO channel (title, url, view_count, subscribers, post_date,thumbnail_url) VALUES ('{title}', '{url}', {view_count}, {subscribers}, '{post_date}', '{thumbnail_url}')"
    cur.execute(sql)

conn.commit()
cur.close()
conn.close()

