# import scrapetube
# import hashlib
# import telegram
# import requests
# import json
# from pytube import YouTube

# from time import sleep
# import os

# bot_token = 'my token'
# bot_chatID = '@PinkPanthersShow'

# bot = telegram.Bot(token=f'{bot_token}')
# c_videos = scrapetube.get_channel("UC1fIyfhQtm1fSljyKBf2uKA")
# videos = list()
# for video in c_videos:
#    videos.append(f"https://www.youtube.com/watch?v={str(video['videoId'])}")
# videos.reverse()
# def upload_video(title, desc):
#     bot.send_video(chat_id=bot_chatID, video=open(fr'{title}.mp4', 'rb'),caption=f"{desc}", supports_streaming=True)
# for i in list(range(len(videos))):
#     yt = YouTube(videos[i])
#     print(f"{yt.title} : {videos[i]}")
#     ys = yt.streams.get_highest_resolution()
#     ys.download()
#     upload_video(str(yt.title), str(yt.description))
# #print (list(videos)[0])
# #links.reverse()
# #print(links)
# #print(title)
# #print(videos)
# input()

