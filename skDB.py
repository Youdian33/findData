# -*- coding: utf-8 -*-

import sqlite3


def main():
    # deleteData()
    queryData()
    # updateData()

# 进攻，技术，速度，力量，防守，耐力，合计
# 查询数据
def queryData():
    conn = sqlite3.connect('skDB.db')
    cursor = conn.execute("SELECT TYPE,NAME,ATC,SPE,STC,POW,DEF,STA,TOT FROM COMPANY WHERE NAME == '韦斯利·斯内德' ORDER BY (ATC+SPE+STC+POW) DESC LIMIT 100")
    aa=cursor.fetchall()
    for i in aa:
        # print("\033[1;32;40m%s" % (str(i)))
        # print(u'%s-%s' % (i[0],i[1]))
        print(u'%s-%s 进攻:%s ,速度:%s 技术:%s 力量:%s 防守:%s 耐力:%s 总值:%s' % (i[0],i[1],str(i[2]),str(i[3]),str(i[4]),str(i[5]),str(i[6]),str(i[7]),str(i[8])))
    conn.close()


# 删除数据
def deleteData():
    conn = sqlite3.connect('skDB.db')
    conn.execute("DELETE FROM COMPANY WHERE TYPE='五星一'")
    # conn.execute('delete from COMPANY where TYPE="欧星2";')
    conn.commit()
    conn.close()


# 修改数据
def updateData():
    conn = sqlite3.connect('skDB.db')
    conn.execute("UPDATE COMPANY SET TYPE='五星一' WHERE TYPE='旧五星'")
    # conn.execute('delete from COMPANY where TYPE="欧星2";')
    conn.commit()
    conn.close()



if __name__ == '__main__':
  main()