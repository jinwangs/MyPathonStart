#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import socket
import time
import gevent
import socket

from gevent import socket,monkey
monkey.patch_all()

def server(port):
    s = socket.socket()
    s.bind(('0.0.0.0', port))
    s.listen(5000)
    while True:
        cli, addr = s.accept()
        gevent.spawn(handle_request, cli,addr)
def handle_request(s,addr):
    try:
        while True:
            data = s.recv(1024)
            print("recv from[%s]:%s"%(addr,data) )
            s.send(data)
            if not data:
                s.shutdown(socket.SHUT_WR)

    except Exception as  ex:
        pass #print(ex)
    finally:
        s.close()
if __name__ == '__main__':
    server(8001)