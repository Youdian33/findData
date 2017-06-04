# -*- coding: utf-8 -*-

import sae.const
import _mysql
import MySQLdb

#
# dbName = sae.const.MYSQL_DB
# usere = sae.const.MYSQL_USER
# pw = sae.const.MYSQL_PASS
# wHost = sae.const.MYSQL_HOST
# port = sae.const.MYSQL_PORT
# rHost = sae.const.MYSQL_HOST_S


def queryData():
    conn = MySQLdb.connect(port=int(sae.const.MYSQL_PORT), host=sae.const.MYSQL_HOST, db=sae.const.MYSQL_DB, user=sae.const.MYSQL_USER, passwd=sae.const.MYSQL_PASS)
    cursor=conn.cursor()
    cursor.execute("SELECT TYPE,NAME,ATC,SPE,STC,POW,DEF,STA,TOT FROM COMPANY WHERE NAME = \'韦斯利·斯内德\' ORDER BY (ATC+SPE+STC+POW) DESC LIMIT 10")
    aa=cursor.fetchall()
    la=list(aa)
    str1= ','.join(la)
    # out =[]
    # for i in aa:
    #     out.append(u'%s-%s 进攻:%s ,速度:%s 技术:%s 力量:%s 防守:%s 耐力:%s 总值:%s  ;' % (i[0],i[1],str(i[2]),str(i[3]),str(i[4]),str(i[5]),str(i[6]),str(i[7]),str(i[8])))
    return str1
    # return u'%s-%s 进攻:%s ,速度:%s 技术:%s 力量:%s 防守:%s 耐力:%s 总值:%s  ;' % (aa[1][0],aa[1][1],str(aa[1][2]),str(aa[1][3]),str(aa[1][4]),str(aa[1][5]),str(aa[1][6]),str(aa[1][7]),str(aa[1][8]))