#!/usr/bin/env python
# -*- coding:utf-8 -*-

import MySQLdb
conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123',db='s12day9')
cur = conn.cursor()
#reCount = cur.execute('select * from students')
#reCount = cur.execute('insert into students(Name,Address) values(%s,%s)',('alex','usa'))
#reCount = cur.execute('insert into students(name,sex,age,tel,nal) values(%s,%s,%s,%s,%s)',('Jack','F',23,135343,"CN"))

#reCount = cur.execute('insert into students(name,sex,age,tel,nal) values(%s,%s,%s,%s,%s)',('Rachel','F',26,3663,"US"))
# reCount = cur.execute('insert into UserInfo(Name,Address) values(%(id)s, %(name)s)',{'id':12345,'name':'wupeiqi'})
#res = cur.fetchall()
#res = cur.fetchmany(3)
#res = cur.fetchone()
#print(res)
#conn.rollback()
li =[
     ('alex','F',11,111,'CN'),
     ('Tenglang','F',19,111,'JP'),
     ('Rain','F',11,111,'USA'),
     ('JACK','F',11,555,'UK'),
]
reCount = cur.executemany('insert into students(name,sex,age,tel,nal) values(%s,%s,%s,%s,%s)',li)

conn.commit()

cur.close()
conn.close()

print reCount