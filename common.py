# -*- coding: utf-8 -*-

__author__ = 'youdian'

import re
import requests
import json
import yaml

def getYaml(filename, name):
    f = open('%s.yaml' % (filename), 'r')
    x = yaml.load(f)
    f.close()
    return x[name]

def updateYmal(fileName, property, value):
    f = open('%s.yaml' % (fileName), 'r+')
    conf = yaml.load(f)
    f.close()
    conf[property]=value
    f1 = open('%s.yaml' % (fileName), 'w')
    yaml.safe_dump(conf, f1)

def query_music_info(word):
    baseurl = r'http://s.music.163.com/search/get/?type=1&limit=5&offset=0&s=%s' % (word)
    resp = requests.get(baseurl)
    music = json.loads(resp._content)
    return music


# aa = query_music_info("春风十里")
# print(aa)