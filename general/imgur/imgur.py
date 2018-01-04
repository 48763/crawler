# encoding: utf-8
'''
Name: imgur-Downloader
Ver: 1.0.0
Author: Yuki
Github: https://github.com/48763
facebook page: https://www.facebook.com/Y.K.fans/?ref=bookmarks
Blog: https://yukifans.com
'''
import requests
import re
import shutil
import time

req = requests.get(raw_input("輸入網址："))

num = re.search("{\"count\":(/d*)", req.text, flags = re.DOTALL)
dic = re.search("\"images\"\:\[(.*?)\]", req.text, flags = re.DOTALL)
hash = re.findall("\"hash\"\:\"(.*?)\"", dic.group(1), flags = re.DOTALL)
type  = re.search("\"ext\"\:\"(.*?)\"", req.text, flags = re.DOTALL)

for hash in hash:
    req = requests.get("https://i.imgur.com/" + hash + type.group(1), stream = True)
    file = open('./' + hash + type.group(1), 'wb')
    # ./ 當前目錄
    # 欲更改儲存目錄，自行變更
    shutil.copyfileobj(req.raw, file)
    file.close
    time.sleep(1)

print ("下載完畢")
