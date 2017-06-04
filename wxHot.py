# coding=utf-8
# author: YouDian 2016年4月23日 11:29:53
import requests
import random

apiKey="cf0adaf71693c890b5ac9d32dee61d5b"
headers = {"apikey":apiKey}

def getHot():
    url = "http://apis.baidu.com/txapi/weixin/wxhot"
    r = requests.get(url,params={"num":"30"},headers=headers)
    responseBody = eval(r._content)
    aa=responseBody["newslist"]
    i = random.randint(1, 30)
    url1=aa[i]["url"].replace("\\","")
    # url1=aa[i]["url"]
    return aa[i]["title"],url1