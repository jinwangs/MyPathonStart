import threading,time

def addNum():
    global num #在每个线程中都获取这个全局变量
    print('--get num:',num)
    time.sleep(1)
    lock.acquire()
    num -= 1  # 对此公共变量进行-1操作
    lock.release()

lock = threading.Lock()
num = 100 #设定一个共享变量
thread_list = []
for i in range(100):
    t = threading.Thread(target=addNum)
    print(t)
    s = t.start()
    print(s)
    thread_list.append(t)
for t in thread_list: #等待所有线程执行完
    t.join()
print('final num:',num)
