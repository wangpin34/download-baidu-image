# -*- coding: utf-8 -*-
import sys
import urllib2
import json
import types
import random
from characterUtil import encodeURIComponent
from imageAPI import searchByWord, decodeImageURL, fetchImg
from file import mkdirIfNonexist
import ConfigParser

config = ConfigParser.ConfigParser()
config.readfp(open('config.ini', "rb"))

proxyHost = config.get('global', 'proxy')

if proxyHost is not None:
    proxy=urllib2.ProxyHandler({'http': proxyHost})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)

reload(sys)                      # reload 才能调用 setdefaultencoding 方法
sys.setdefaultencoding('utf-8')  # 设置 'utf-8'

keyWords = encodeURIComponent('娜美')
result = searchByWord(keyWords, 0, 100)
result = json.loads(result)
data = result['data']

links = []

for entity in data:
    objURL = entity.get('objURL')
    links.append(decodeImageURL(objURL))

mkdirIfNonexist('./temp')
for link in links:
    if link is None:
        continue
    response = fetchImg(link)
    if response is None:
        continue
    info = response.info()
    if info.getmaintype() == 'image':
      ext = info.getsubtype()
      name = str(random.uniform(1,2)).replace('.', '') + '.' + ext
      file = open('./temp/' + name, 'wb')
      file.write(response.read())
      file.close()
