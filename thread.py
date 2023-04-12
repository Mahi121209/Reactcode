import socket
import threading

HOST = ''
PORT = 8002
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen()
print(f'Server listening on port {PORT}')

def handle_connection(conn, addr):
    print(f'Connected by {addr}')
    
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f'Received: {data}')
        conn.sendall(data)
    conn.close()
while True:
    conn, addr = sock.accept()
    threading.Thread(target=handle_connection, args=(conn, addr)).start()
Collapse



# multiconn-server.py

# import sys
# import socket
# import selectors
# import types

# sel = selectors.DefaultSelector()

# # ...

# host, port = sys.argv[1], int(sys.argv[2])
# lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# lsock.bind((host, port))
# lsock.listen()
# print(f"Listening on {(host, port)}")
# lsock.setblocking(False)
# sel.register(lsock, selectors.EVENT_READ, data=None)
