import urllib2

templateURL = 'http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&fp=result&queryWord=%s&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%s&face=0&istype=2&nc=1&pn=%s&rn=%s&gsm=1e'

URLMapSpe = { '_z2C$q': ':', 'AzdH3F': '/', '_z&e3B': '.' }
URLMap = {
    'w': 'a',
    'k': 'b',
    'v': 'c',
    '1': 'd',
    'j': 'e',
    'u': 'f',
    '2': 'g',
    'i': 'h',
    't': 'i',
    '3': 'j',
    'h': 'k',
    's': 'l',
    '4': 'm',
    'g': 'n',
    '5': 'o',
    'r': 'p',
    'q': 'q',
    '6': 'r',
    'f': 's',
    'p': 't',
    '7': 'u',
    'e': 'v',
    'o': 'w',
    '8': '1',
    'd': '2',
    'n': '3',
    '9': '4',
    'c': '5',
    'm': '6',
    '0': '7',
    'b': '8',
    'l': '9',
    'a': '0'
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #'Accept-Encoding': 'gzip, deflate, sdch', # leads to unexpected data
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cookie': 'BDqhfp=%E7%B4%A2%E9%9A%86%26%260-10-1undefined%26%260%26%261; BIDUPSID=274E948C016A02F123675D5E30FE4A4D; BAIDUID=1E865B2D98CCC978986377AD7C84FD2A:FG=1; PSTM=1467387983; MCITY=-%3A; indexPageSugList=%5B%22%E7%B4%A2%E9%9A%86%22%2C%22%E5%A5%B3%E5%B8%9D%22%5D; cleanHistoryStatus=0; firstShowTip=1; PSINO=5; H_PS_PSSID=1462_21088_18133_22036_21672_22075',
    #'Host': 'image.baidu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}

def searchByWord(word, startFrom, total):
    try:
        url = templateURL%(word, word, startFrom, total)
        #print url
        request = urllib2.Request(url, None, headers)
        response =  urllib2.urlopen(request)
    except urllib2.URLError, e:
        print e.reason
        return
    return response.read()

def decodeImageURL(url):
    if url is None:
        return url
    for key in URLMapSpe:
        url = url.replace(key, URLMapSpe[key])
    urlList = list(url)
    url = []
    for char in urlList:
        if char in URLMap:
            result = URLMap[char]
        else:
            result = char
        url.append(result)
    return ''.join(url)

def fetchImg(url):
    try:
        request = urllib2.Request(url, None, headers)
        response =  urllib2.urlopen(request)
        return response
    except urllib2.URLError, e:
        print 'Fetch image from %s failed, reason: %s'%(url, e.reason)
        return
