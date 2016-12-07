import socket
ip_address = ('127.0.0.1',3306)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ip_address)
while True:
    msg = input(">>:").strip()
    if len(msg) == 0:
        continue
    client.send(msg.encode("utf-8"))
    data  = client.recv(1024)
    print("来自服务器：",data.decode())
client.close()