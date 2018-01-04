# encoding: utf-8
'''
Name: nhentai-Downloader
Ver: 1.0.0
Author: Yuki
Github: https://github.com/48763
facebook page: https://www.facebook.com/Y.K.fans/?ref=bookmarks
Blog: https://yukifans.com
'''
import os
import sys
import requests
import re
import shutil
import random
import time

dir = raw_input("儲存的資料夾名稱：")

if not os.path.exists(dir):
    os.makedirs(dir)
else: 
    print "資料夾已存在！"
    sys.exit()

count = 1
type = ".jpg"
req = requests.get(raw_input("輸入網址："))
list = re.findall("href=\"(/g/\d*?/\d*/)\"", req.text, flags = re.DOTALL)
list.pop(0)

for list in list:
    req = requests.get("https://nhentai.net" + list)
    time.sleep(random.randint(1,2))
    
    img = re.search("<img src=\"(https://i..*?)\"", req.text, flags = re.DOTALL) 
    req = requests.get(img.group(1), stream = True)
    
    file = open(dir + "/" + str(count) + type, 'wb')
    shutil.copyfileobj(req.raw, file)
    file.close

    count += 1
    time.sleep(random.randint(1,2))

print ("下載完畢")