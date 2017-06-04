# -*- coding: utf-8 -*-

__author__ = 'youdian'

import re
import requests
import json
import yaml

def fixName(name):
    f = open('test.yaml','r')
    x =yaml.load(f)
    f.close()
    a =x['name']
    name=name.decode("utf-8")
    if (name in a):
        return a[name]
    else:
        return name

def getData(type,name):
    question=type+'+'+name
    url ='http://wscs.gm.163.com/cgi-bin/csa/csa_sprite.py?act=ask&question=%s&product_name=wscs&log_name=wscs'% question
    r = requests.get(url)
    print(url)
    aa=r._content.decode("gb2312")
    aa =json.loads(aa)
    bb =aa["answer"]
    bb = bb.replace('<br/>','<br>')
    cc = bb.split("<br>")
    while '' in cc:
        cc.remove('')
    par=[]
    for i in cc:
        dr = re.compile(r'<[^>]+>',re.S)
        dd = dr.sub('',i)
        par.append(dd)
    return par


def tp99(arg):
    a=int(arg)
    return round(a*1.1)+99

def find_data(arg,value):
    for i in arg:
        if all(j in i.encode("utf-8") for j in value):
            getNum = re.compile(r'\d+',re.S)
            dataNum = getNum.findall(i.encode("utf-8"))
            return dataNum

def find_str(arg,value):
    for i in arg:
        if value in i:
            return i

def assertScore(arg):
    if arg < 600:
        return 1
    elif arg>=600 and arg<650:
        return 2
    elif arg>=650 and arg<700:
        return 3
    elif arg>=700 and arg<750:
        return 4
    elif arg>=750 and arg<800:
        return 5
    elif arg>=800 and arg<850:
        return 6
    elif arg>=850 and arg<900:
        return 7
    elif arg>=900 and arg<950:
        return 8
    elif arg>=950 and arg<1000:
        return 9
    elif arg>=1000 and arg<1100:
        return 10
    elif arg>=1100 and arg<1200:
        return 11
    elif arg>=1200 and arg<1300:
        return 12
    elif arg>=1300 and arg<1400:
        return 13
    elif arg>=1400 and arg<1500:
        return 14
    elif arg>=1500 and arg<1600:
        return 15
    else:
        return 0

# 1为进攻,2为速,3为技,4为防
def sumScore(type,jingong,fangshou,jishu,liliang,sudu,naili):
    if type=="攻":
        score = assertScore(jingong)*2+(assertScore(jishu)+assertScore(liliang)+assertScore(sudu))*0.8+\
                (assertScore(naili)+assertScore(fangshou))*0.2
        return score
    elif type=="速":
        score = assertScore(sudu)*2+(assertScore(jishu)+assertScore(liliang)+assertScore(jingong))*0.8+\
                (assertScore(naili)+assertScore(fangshou))*0.2
        return score
    elif type=="技":
        score = assertScore(jishu)*2+(assertScore(sudu)+assertScore(liliang)+assertScore(jingong))*0.8+\
            (assertScore(naili)+assertScore(fangshou))*0.2
        return score
    elif type=="守":
        score = assertScore(fangshou)*2+(assertScore(jishu)+assertScore(liliang)+assertScore(sudu))*0.8+\
                (assertScore(naili)+assertScore(jingong))*0.2
        return score
    else:
        return "type is error~"


def prDate(dataNum):
    date=""
    if len(dataNum) ==12:
        jingong = dataNum[1]
        fangshou = dataNum[3]
        jishu = dataNum[5]
        liliang = dataNum[7]
        naili = dataNum[9]
        sudu = dataNum[11]
        total = str(int(jingong)+int(fangshou)+int(jishu)+int(liliang)+int(naili)+int(sudu))
        keyValue_off = str(int(jingong)+int(jishu)+int(liliang)+int(sudu))
        keyValue_def = str(int(fangshou)+int(jishu)+int(liliang)+int(sudu))
        date="进攻:%s 速度：%s 技术：%s 力量：%s 防守：%s 耐力：%s 总值：%s"%(tp99(jingong),tp99(sudu),tp99(jishu),tp99(liliang),tp99(fangshou),tp99(naili),str(tp99(total)+495))
        # date[u'基础数据']={u'进攻:':jingong,u'速度':sudu,u'技术':jishu,u'力量':liliang,u'防守':fangshou,u'耐力':naili,u'总值':total}
        # date[u'终极数据']={u'进攻':tp99(jingong),u'速度':tp99(sudu),u'技术':tp99(jishu),u'力量':tp99(liliang),u'防守':tp99(fangshou),u'耐力':tp99(naili),u'总值':tp99(total)+495}
        # date[u'数据评估']={u'攻击属性':keyValue_off,u'防御属性':keyValue_def}
        return date
    else:
        date="传奇卡组存在变数,无法计算"
        return date

def prDateS(score,dataNum):
    date=""
    if len(dataNum) ==12:
        jingong = dataNum[1]
        fangshou = dataNum[3]
        jishu = dataNum[5]
        liliang = dataNum[7]
        naili = dataNum[9]
        sudu = dataNum[11]
        total = str(int(jingong)+int(fangshou)+int(jishu)+int(liliang)+int(naili)+int(sudu))
        valueScore = sumScore(score,int(jingong),int(fangshou),int(jishu),int(liliang),int(sudu),int(naili))
        endScore=sumScore(score,int(tp99(jingong)),int(tp99(fangshou)),int(tp99(jishu)),int(tp99(liliang)),int(tp99(sudu)),int(tp99(naili)))
        date="进攻:%s 速度：%s 技术：%s 力量：%s 防守：%s 耐力：%s 总值：%s 初级基础数据得分:%s 终极基础数据得分:%s"%(tp99(jingong),tp99(sudu),tp99(jishu),tp99(liliang),tp99(fangshou),tp99(naili),str(tp99(total)+495),str(valueScore),str(endScore))
        return date
    else:
        date="传奇卡组存在变数,无法计算"
        return date

def find_base(par):
    aa =""
    for i in par:
        if u"小精灵" in i or u"下方是" in i or u"点击了解" in i :
            par.remove(i)
        else:
            aa=aa+i+u'\n'
    return aa

def findData(name,type):
    par = getData(fixName(name), fixName(type))
    dataNum1 = find_data(par, ['进攻', '速度', '力量', '防守', '耐力'])
    data1 = find_base(par).replace('&nbsp;','')
    if dataNum1 != None and dataNum1 != []:
        dataNum = dataNum1
        data2 = prDate(dataNum).decode("utf-8")
        # data = data1.encode("utf-8")+data2
        return data1,data2
        # return data1,data2.decode("ascii").encode("utf-8")
        # print(data2)
    else:
        return u"可能是模糊力度不够,也可能是黄易未记载...\n",u"建议重试下更准确名称~"

def findDataS(type1,name,type):
    par = getData(fixName(name), fixName(type))
    dataNum1 = find_data(par, ['进攻', '速度', '力量', '防守', '耐力'])
    data1 = find_base(par)
    if dataNum1 != None and dataNum1 != []:
        dataNum = dataNum1
        data2 = prDateS(type1,dataNum).decode("utf-8")
        # data = data1.encode("utf-8")+data2
        return data1,data2
        # return data1,data2.decode("ascii").encode("utf-8")
        # print(data2)
    else:
        return u"可能是模糊力度不够,也可能是黄易未记载...\n",u"建议重试下更准确名称~"


# a = findData("欧冠4","内马尔")
# print(a[0])