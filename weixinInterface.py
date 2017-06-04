# -*- coding: utf-8 -*-
import hashlib
import web
import os
import lxml
import time
import findDataUp
import wxHot
import random
import sqlData
import common

from lxml import etree

class WeixinInterface:

    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        #获取输入参数
        data = web.input()
        signature=data.signature
        timestamp=data.timestamp
        nonce=data.nonce
        echostr=data.echostr
        #自己的token
        token="youdian521" #这里改写你在微信公众平台里输入的token
        #字典序排序
        list=[token,timestamp,nonce]
        list.sort()
        sha1=hashlib.sha1()
        map(sha1.update,list)
        hashcode=sha1.hexdigest()
        #sha1加密算法

        #如果是来自微信的请求，则回复echostr
        if hashcode == signature:
            return echostr
    def POST(self):
        str_xml = web.data() #获得post来的数据
        # print(str(str_xml))
        xml = etree.fromstring(str_xml)#进行XML解析
        msgType=xml.find("MsgType").text
        fromUser=xml.find("FromUserName").text
        toUser=xml.find("ToUserName").text
        if msgType == "event":
            mscontent = xml.find("Event").text
            if mscontent == "subscribe":
                replayText = u'欢迎关注本微信，这个微信是本人业余爱好所建立，纯属兴趣而已'
                return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)
            if mscontent == "unsubscribe":
                replayText = u'我现在功能还很简单，知道满足不了您的需求，但是我会慢慢改进~'
                return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)
        if msgType == 'text':
            content=xml.find("Content").text
            if "@" in content:
                a = content.split("@")
                resp,data = findDataUp.findData(a[0].encode("utf-8"),a[1].encode("utf-8"))
                # return self.render.reply_text(fromUser,toUser,int(time.time()),u"魔都出品: "+resp)
                return self.render.reply_text(fromUser,toUser,int(time.time()),u"魔都曰：\n"+resp+u"【终极数据】:\n"+data)
            elif "#" in content:
                a = content.split("#")
                resp,data = findDataUp.findDataS(a[0].encode("utf-8"),a[1].encode("utf-8"),a[2].encode("utf-8"))
                return self.render.reply_text(fromUser,toUser,int(time.time()),u"魔都曰：\n"+resp+u"【终极数据】:\n"+data)
            elif u"抽球" in content:
                data = u"http://5sing.kugou.com/m/Song/Detail/fc/15577602"
                return self.render.reply_music(fromUser, toUser, int(time.time()), u"抽球壮志在我心", u"Jeff出品", data)
            elif u"姗姗" in content:
                data=u"https://pan.baidu.com/s/1qYeZ0eC"
                return self.render.reply_music(fromUser,toUser,int(time.time()),u"给最爱的玲和姗",u"我生命中最重要的礼物",data)
            elif u"实况之声" in content:
                tbData=common.getYaml("music","musicData")
                dataMusic=random.choice(tbData)
                namemusic = dataMusic["name"]
                urlmusic= dataMusic["url"]
                # data=u"http://5sing.kugou.com/m/Song/Detail/yc/3211693"
                return self.render.reply_music(fromUser,toUser,int(time.time()),namemusic,u"Jeff出品",urlmusic)
            elif u"jeff" in content:
                tbData=common.getYaml("music","jeffData")
                dataMusic=random.choice(tbData)
                namemusic = dataMusic["name"]
                urlmusic= dataMusic["url"]
                # data=u"http://5sing.kugou.com/m/Song/Detail/yc/3211693"
                return self.render.reply_music(fromUser,toUser,int(time.time()),namemusic,u"Jeff出品",urlmusic)
            elif u"算我一个" in content:
                return self.render.reply_text(fromUser,toUser,int(time.time()),u"诺，坐等摔杯为号！")
            elif u"托" in content:
                tbData=common.getYaml("note","tbData")
                return self.render.reply_text(fromUser,toUser,int(time.time()),u"魔都曰:"+random.choice(tbData))
            elif u"黑" in content:
                hbData=common.getYaml("note","hbData")
                return self.render.reply_text(fromUser,toUser,int(time.time()),u"魔都曰:"+random.choice(hbData))
            elif u"豪" in content:
                thData=common.getYaml("note","thData")
                return self.render.reply_text(fromUser,toUser,int(time.time()),u"魔都曰:"+random.choice(thData))
            elif u"算分规则" in content:
                thData=common.getYaml("skill","text1")
                return self.render.reply_text(fromUser,toUser,int(time.time()),u"魔都曰:"+thData)
            elif u"技能得分" in content:
                thData=common.getYaml("skill","text2")
                return self.render.reply_text(fromUser,toUser,int(time.time()),u"魔都曰:"+thData)
            # elif u"8888" in content:
            #     $def with (toUser,fromUser,createTime,title,description,picurl,$url)
            #     urlpic=u"http://share.weiyun.com/f07c10659f700483a4b57831e2817887"
            #     url1 = u"http://share.weiyun.com/f07c10659f700483a4b57831e2817887"
            #     return self.render.reply_pic(fromUser,toUser,int(time.time()),u"title",u"description",urlpic,url1)
            # $def with (toUser,fromUser,createTime,title,description,music_url)
            elif u"音乐" in content:
                s = content.replace(u"音乐","")
                music = common.query_music_info(s)
                title = music['result']['songs'][0]['name']
                desc =  u'随便听听~'
                url = music['result']['songs'][0]['audio']
                return self.render.reply_music(fromUser,toUser,int(time.time()),title,desc,url)
            else:
                return self.render.reply_text(fromUser,toUser,int(time.time()),u"魔都召集:运营无能，只管圈钱；技术兼职，缺陷不改；客服省事，意见不复！特召集球迷千名，直面三石，陈书案前，知错能改，既往不咎，否，则文化部批号见！共举义事，复【算我一个】！ \n标准格式为 欧冠5@伊布拉希莫维奇,想知道数据得分可输入:攻#欧冠6#梅西 不按照套路出牌有可能中彩蛋...")