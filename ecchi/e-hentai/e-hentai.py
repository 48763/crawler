# encoding: utf-8
'''
Name: Hentai-Downloader
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

headers = {
"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", 
"accept-encoding":"gzip, deflate, br", 
"accept-language":"zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4", 
"upgrade-insecure-requests":"1", 
"user-agent":"Chrome/59.0.3071.115"
}

dir = raw_input("儲存的資料夾名稱：")

if not os.path.exists(dir):
    os.makedirs(dir)
else: 
    print "資料夾已存在！"
    sys.exit()

count = 1
type = ".jpg"
current = requests.get(raw_input("輸入網址："))
next = re.search("<div id=\"gdt\">.*<a href=\"(.*?-1)\"><", current.text, flags = re.DOTALL)

while current.url != next.group(1):
    headers['referer'] = current.url
    prv = current
    current = requests.get(next.group(1), cookies = current.cookies, headers = headers)
    time.sleep(random.randint(1,2))
    
    img = re.findall("<img id=\"img\" src=\"(.*?)\"", current.text)
    img = requests.get(img[0], stream = True)

    file = open(dir + "/" + str(count) + type, 'wb')
    shutil.copyfileobj(img.raw, file)
    file.close
    
    next = re.search("<a id=\"next\" .*? href=\"(.*?-\d*?)\">", current.text, flags = re.DOTALL)
    count += 1
    time.sleep(random.randint(1,2))

print ("下載完畢")