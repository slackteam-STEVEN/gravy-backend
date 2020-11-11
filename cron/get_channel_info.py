# -*- coding: utf-8 -*-

# ライブラリをインポート
import os
import psycopg2
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
from get_channel_id import youtube_id
import configparser

config = configparser.ConfigParser()
config.read('gravy.ini')
KEY = config.get('YOUTUBE', 'api_key')
HOST = config.get('DB', 'host')
DATABASE = config.get('DB', 'database')
USER = config.get('DB', 'user')
PORT = config.get('DB', 'port')
PASSWORD = config.get('DB', 'password')

viewCount, rating = youtube_id()

YOUTUBE_API_KEY = KEY

youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

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


dbname = "DATABASE"
conn = psycopg2.connect(f"host={HOST} dbname={DB_NAME} user={USER} port={PORT} password={PASSWORD}")
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
print("success")
