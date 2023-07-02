import socket
from multiprocessing import Process
# SOCK_STREAM -> TCP
# SOCK_DGRAM -> UDP
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

s.bind(('localhost',8085)) #127.0.0.1
s.listen(1)
clients=[]


def listen(connection , client):
    while True:
        # wait for data per 32 byte
        data=connection.recv(32).decode()
        print("Received",data)
        if data=='!':
                break
        for client in clients:
            client['connection'].send(data.encode())
    connection.close()


# def join():
while True:
    #listen for a connection
    connection , client =s.accept()
    print (client,'Connected')
    clients.append({'connection':connection,'client':client})
    p_listen=Process(target=listen,args=(connection,client))
    p_listen.start()


# p_join=Process(target=join)
# p_join.start()


