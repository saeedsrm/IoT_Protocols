import socket
# SOCK_STREAM -> TCP
# SOCK_DGRAM -> UDP
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

s.bind(('localhost',1598)) #127.0.0.1
s.listen(1)


#listen for a connection

connection , client =s.accept()

print (client,'Connected')

while True:
    # wait for data per 32 byte
    data=connection.recv(32).decode()
    print("Received",data)

    if data=='!':
        break

    connection.send('sent'.encode())
connection.close()