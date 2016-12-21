import time
import threading

def run(n):
    print('[%s]--------running-------\n' %n)
    time.sleep(2)
    print('----done------')
def main():
    for i in range(5):
        t = threading.Thread(target=run,args=[i,])
        t.start()
        # t.join(1)
        print('starting thread',t.getName())

m = threading.Thread(target=main,args=[])
m.setDaemon(True)

m.start()
m.join(timeout=3)
print("----------mian thread done----------")