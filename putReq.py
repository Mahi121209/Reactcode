import socket
import os
HOST = ''
PORT = 8000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen(5)
sock.setblocking(0)

while True:
    try:
        conn, addr = sock.accept()
        pid = os.fork()
        if pid == 0:
            sock.close()
            while True:
                try:
                    data = conn.recv(300)
                    request = data.decode('ascii')
                    # print('req', request)
                    if not request:
                        break
                    method = request.split(' ')[0]
                    path = request.split(' ')[1]
                    # print('method', method)
                    # print('reqSplit', path)
                    if path == '/' or path == '/index.html':
                        filename = 'index.html'
                    else:
                        filename = path[1:]
                        if method == 'GET':
                            if os.path.exists(filename):
                                with open(filename, 'r') as f:
                                    response = f.read()
                                    header = 'HTTP/1.1 200 OK\r\nContent-Length: ' + \
                                        str(len(response)) + '\r\n\r\n'
                                    conn.sendall(
                                        (header + response).encode('ascii'))
                            else:
                                response = 'File not found'
                                header = 'HTTP/1.1 404 Not Found\r\nContent-Length: ' + \
                                    str(len(response)) + '\r\n\r\n'
                                conn.sendall(
                                    (header + response).encode('ascii'))

                        elif method == 'POST':
                            a = request.split('\r\n\r\n')
                            print('aa', a)
                            body = a[1]
                            b = a[0].split('\r\n')
                            c = b[1:len(b)]
                            len = 0
                            for i in c:
                                abcd = i.split(':')
                                if abcd[0] == 'Content-Length':
                                    len = int(abcd[1])
                                    break
                            print(len)
                            post_data = request.split('\r\n\r\n')[1]
                            f = open(filename, 'w')
                            with open(filename, 'w') as f:
                                f.write(post_data)
                                response = 'successful'
                                str(len(response)) + '\r\n\r\n'
                                conn.sendall(
                                    (header + response).encode('ascii'))
                except:
                    break  # conn.close() # os._exit(0)
                else:
                    conn.close()
    except:
        pass
