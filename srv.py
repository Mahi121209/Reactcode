
import sys
import socket
len(sys.argv)
# print(sys.argv[1], sys.argv[2])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.connect((sys.argv[1], int(sys.argv[2])))
# sock.listen()

while True:
    a = input()
    b = input()
    request = (str(a) + '\r\n' + str(b) + '\r\n\r\n').encode('ascii')
    sock.sendall(request)
    reply = sock.recv(10000000)
    print((reply).decode('utf-8'))
    sock.close()
    break
    