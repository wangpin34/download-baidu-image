# -*- coding: utf-8 -*-
import urllib

def encodeURIComponent(str):
    return urllib.quote(str, safe='~()*!.\'')
