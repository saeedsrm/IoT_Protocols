import socket
from multiprocessing import Process
import threading


# SOCK_STREAM -> TCP
# SOCK_DGRAM -> UDP
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

# Connecting
s.connect(('localhost',1598)) #127.0.0.1


def recv():
    while True:
        data=s.recv(32)
        print("Server: ",data.decode())

# p=Process(target=recv)
# p.start()
t1 = threading.Thread(target=recv)
t1.start()


while True:
    msg=input()
    if msg=='~':
        s.send('!'.encode())
        break
    try:
        s.send(msg.encode())
    except:
        print('connection lost!')
        break
s.close()
p.terminate()
