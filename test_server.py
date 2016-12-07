import socket,time
ip_address = ('127.0.0.1',3306)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ip_address)
server.listen(5)
print("等待客户连接......")
client,addr = server.accept()
print("新连接：" ,addr)
time.sleep(2)
while True:
    data = client.recv(1024)
    if not data:
        print("客户应经断开。。。")
        break
    print("收到消息",data.decode())
    client.send(data)
server.close()
