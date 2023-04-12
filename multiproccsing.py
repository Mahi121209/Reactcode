import socket
import os
sock_add = ('', 1235)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(sock_add)
sock.listen(5)

while True:
    client_sock, client_addr = sock.accept()
    # print('kkk', client_sock)
    pid = os.fork()
    if pid == 0:
        sock.close()
    while True:
        data = client_sock.recv(1024)
        fileData = (data).decode('utf-8').split(' ')[1].replace('/', '', 1)
        print('filedata', fileData)
        for subdir, dirs, files in os.walk('./'):
            for x in files:
                if x == fileData:
                        f = open(fileData, 'r')
                        size = os.stat(fileData)
                        response = ''
                        if data:
                            for x in range(0, size.st_size, 64):
                                response += f.read(x)
                            client_sock.sendall((response).encode('ascii'))
                            print((data).decode('utf-8'))
                        else:
                            client_sock.close()
                            break
    else:
        client_sock.close()