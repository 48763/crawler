# encoding: utf-8
'''
ame: nhentai-Downloader
Ver: 1.0.3
Author: Yuki
Github: https://github.com/48763
facebook page: https://www.facebook.com/Y.K.fans/?ref=bookmarks
Blog: https://yukifans.com
'''
import requests
import re
import urlparse
import shutil

'''
path = "https://domain/dir/"
url = path + raw_input("輸入編號：")
'''
url = raw_input("輸入網址：")

num = re.findall("/(\d\d*)", url)

req = requests.get(url)
video_url = re.findall('src: "(.*?)"}', req.text, flags = re.DOTALL)

req = requests.get(video_url[0], stream = True)
mp4 = open('./' + num[0] + '.mp4', 'wb')

shutil.copyfileobj(req.raw, mp4)
mp4.close

print '下載完畢'
