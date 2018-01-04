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
DSC = re.findall("<a href=\"(.*?=yes)\"", req.text, flags = re.DOTALL)
DSC.pop(0)
DSC.pop(0)
DSC.pop(0)

img = re.findall("<img src=\"(http://img..*?.jpg)\"", req.text, flags = re.DOTALL)

for DSC in DSC:
    DSC = DSC.replace('&amp;', '&')
    req = requests.get("url" + DSC, stream = True)
    # url = http://host.domain/
    
    file = open(dir + "/" + str(count) + type, 'wb')
    shutil.copyfileobj(req.raw, file)
    file.close

    count += 1
    time.sleep(1)

for img in img:
    req = requests.get(img, stream = True)
    
    file = open(dir + "/" + str(count) + type, 'wb')
    shutil.copyfileobj(req.raw, file)
    file.close

    count += 1
    time.sleep(1)

print ("下載完畢")
