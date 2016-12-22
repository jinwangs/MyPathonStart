#!/usr/bin/env python
# -*- coding:utf-8 -*-
import queue
class Foo(object):
    def __init__(self,n):
        self.n = n

#q =  queue.Queue(maxsize=30)
#q =  queue.LifoQueue(maxsize=30)
q =  queue.PriorityQueue(maxsize=30)
q.put((2,[1,2,3]))
#q.put(Foo(1))
q.put((10,1))
q.put((3,1))
q.put((5,30))
q.task_done()
q.join()
print(q.get())
print(q.get())
print(q.get())
print(q.get())
