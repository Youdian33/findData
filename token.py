import requests

def getToken():
    appid ="wxb7b018341bbcebad"
    secret ="f74f104b214641c3faf3d7371af3e312"
    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s"%(appid,secret)
    resp = requests.get(url)
    print(resp._content)

token = "1K0mBSNSQIoTxWFf1b0YQaUq_jzYoexwUGw1HksLYK5ISYvwEh25YU4vUtLrZ7HNmlTwFU6Qj5gY8WeWV2SNOA8upDoSPJzvUUpBBUg0JmqSbgWeYmomXBzwOfn43VenYUBhAAADZG"

def getData(token):
    url2 ="https://api.weixin.qq.com/cgi-bin/material/batchget_material?access_token=%s"%(token)
    par = {"type":"voice","offset":"offset","count":5}
    resp1 = requests.post(url2,data=par)
    print(resp1._content)

getData(token)