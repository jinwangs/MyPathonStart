
import threading

import queue

 

def producer():

    for i in range(10):

        q.put("��ͷ %s" % i )

 

    print("��ʼ�ȴ����еĹ�ͷ��ȡ��...")

    q.join()

    print("���еĹ�ͷ��ȡ����...")

 

 

def consumer(n):

 

    while q.qsize() >0:

 

        print("%s ȡ��" %n  , q.get())

        q.task_done() #��֪�������ִ������

 

 

q = queue.Queue()

 

 

 

p = threading.Thread(target=producer,)

p.start()

 

c1 = consumer("�")