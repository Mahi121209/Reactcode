import socket
import os
sock_add = ('', 4000)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock1= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock1.connect(('192.168.29.206', 1236))
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(sock_add)
sock.listen(5)


while True:
    client_sock, client_addr = sock.accept()
    pid = os.fork()
    if pid == 0:
        sock.close()
    while True:
        data = client_sock.recv(1024)
        f = open('index.html', 'r')
        size = os.stat('index.html')
        response = ''
        relayServer = ''
        if data:
            for x in range(0, size.st_size, 64):
                response += f.read(x)
            sock1.sendall((response).encode('ascii'))
            relayServer = sock1.recv(10000)
            print('replay', relayServer)
            
            client_sock.sendall((relayServer))
            print((data).decode('utf-8'))
        else:
            client_sock.close()
            break
    else:
        client_sock.close()