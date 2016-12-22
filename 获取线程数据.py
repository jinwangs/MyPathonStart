#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time ,threading

data = []
def run(n):
    time.sleep(5)
    data.append(n**n)
    print('from child')
    #return  n**n

res_list = []
for i in range(10):
    t = threading.Thread(target=run,args=[i,])
    t.start()
    res_list.append(t)

for r in res_list:
    r.join(timeout=0.1)
    #break
print("-------",data)