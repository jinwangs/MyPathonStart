#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import threading
HOST = 'localhost'    # The remote host
PORT = 8001           # The same port as used by the server
def run(n):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((HOST, PORT))
    s.send("Hello World!")
    data = s.recv(1024)
    print("Thread [%s]:[%s]\n" % (n,data))

    s.close()

res_list = []
for i in range(2000):
    t = threading.Thread(target=run,args=[i,])
    t.start()
    res_list.append(t)

for r in res_list:
    r.join()