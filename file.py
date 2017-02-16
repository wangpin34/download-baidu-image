# -*- coding: utf-8 -*-
import os

def mkdirIfNonexist(path):
  if not os.path.exists(path):
    os.mkdir(path)
