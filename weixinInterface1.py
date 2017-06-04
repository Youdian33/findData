# -*- coding: utf-8 -*-
import hashlib
import web
import os
import lxml
import time
import findDataUp
import wxHot
import random

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
                return self.render.reply_text(fromUser,toUser,int(time.time()),u"魔都出品:\n "+resp+u"【终极数据】:\n"+data)
                # return self.render.reply_text(fromUser,toUser,int(time.time()),data)
            elif u"建议" in content:
                # title,url = wxHot.getHot(
                url1=u"谢谢你的建议,我先拿个小本子记下来~"
# $def with (toUser,fromUser,createTime,title,description,url)
                return self.render.reply_text(fromUser,toUser,int(time.time()),url1)
            elif u"托" in content:
                tbData=[u"果一托比谁敌手?巴 神,生子当如大头咩~~",
                        u"天下三分,四川一分,虎虎一分,大红鹰两分,蛋鸡黑鬼负一分~",
                        u"有一种饼干,叫奥利奥~",
                        u"有一种竞技,叫XY~",
                        u"大头大头,下雨不愁~",
                        u"姓教主,得永生~",
                        u"大头二哥三木四中五多七士八叔,不要怪我多嘴,名字里面带单数的都能托~"]
# $def with (toUser,fromUser,createTime,title,description,url)
                return self.render.reply_text(fromUser,toUser,int(time.time()),u"魔都曰:"+random.choice(tbData))
            elif u"黑" in content:
                tbData=[u"二哥是条汉子~~",
                        u"人缺啥就喜欢叫啥,比如红胖~",
                        u"有人说天道酬勤,魔都是个例外~",
                        u"MO说,有种你别给我前锋,所以直到他离开都没见过31以上的CF~",
                        u"八叔抽了个欧冠拉姆,然后嘚吧嘚吧的80了~",
                        u"jeff有我这一辈子都用不完的前锋,但是他的前锋永远都拿不到球~"]
                return self.render.reply_text(fromUser,toUser,int(time.time()),u"魔都曰:"+random.choice(tbData))

            elif u"豪" in content:
                tbData=[u"骑士哥其实需要我这样的秘书~~",
                        u"最受尊重的豪估计就是水母了~",
                        u"碎嘴豪我不敢说,怕惹骚气~",
                        u"友情提示,虎虎绝壁是官托~",
                        u"大米米说让他们打着,追上来了我反击一波流带走~",
                        u"四川是最大的官托,抽卡千万别信~",
                        u"花时间玩这个游戏的你才是最大的豪~",
                        u"何以谓之豪也?打不过的,弃坑的号全收了,请团队玩,承包天梯前30,是以谓之豪也~",
                        u"有一种人不要惹,果一到果五,每区都手握重兵,不花钱还能抢红包,国师是也"]
# $def with (toUser,fromUser,createTime,title,description,url)
                return self.render.reply_text(fromUser,toUser,int(time.time()),u"魔都曰:"+random.choice(tbData))
            else:
                return self.render.reply_text(fromUser,toUser,int(time.time()),u"标准格式为 欧冠5@伊布拉希莫维奇 你不按套路出牌啊~过输入错误了也有可能中彩蛋...")