import time
import threading
def sayhi(num): #定义每个线程要运行的函数
    print("running on number:%s" %num)
    time.sleep(3)
if __name__ == '__main__':
    t_list = []
    for i in range(10):
        t = threading.Thread(target=sayhi,args=(i,))#生成一个线程实例
        t_list.append(t)
        t.start()#启动线程

    for i in t_list:
        i.join()
    print('-----main------')
    # print(t1.getName())#获取线程名
    # print(t2.getName())