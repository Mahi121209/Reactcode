import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.bind(('0.0.0.0', 3002))
sock.listen(3)
print('Server is listening ...')

def get_request(req, file_name, client):
    if req:
        try:
            data = open(file_name, 'r')
            size = os.stat(file_name)
            response = 'HTTP/1.1 200 OK\r\nContent-Length: ' + str(size.st_size) + '\r\nContent-Type: text/html\r\n\r\n'
            response += data.read()
            client.send(response.encode())

        except:
            response = 'HTTP/1.1 404 OK\r\nContent-Length: 123' + '\r\nContent-Type: text/html\r\n\r\n<html><head><title>page not found</title></head><body><h2>404 Not Found ...</h2><p>something went wrong !</p></body></html>'
            client.send(response.encode())
        pass
    else:
        client.close()

def post_request(content_length, has_read, req, client, file_name):
    if int(content_length) > has_read:
        how_much_more = int(content_length) - has_read
        req += client.recv(how_much_more).decode()
        content = req.split('\r\n\r\n')[1]
        print(f'&&&: {req}\n')
    if len(content) != int(content_length):
        client.send(b'HTTP/1.1 404 OK\r\nContent-Length: 15\r\n\r\nBad request ...')

    else:
        new_file = open(file_name, 'w')
        new_file.write(content)
        client.send(b'HTTP/1.1 200 OK\r\nContent-Length: 37\r\n\r\nfile created/updated successfully ...')
        new_file.close()

def delete_request(file_name, client):
    if os.path.exists(file_name):
        os.remove(file_name)
        client.send(b'HTTP/1.1 200 OK\r\nContent-Length: 29\r\n\r\nfile deleted successfully ...')
    else:
        client.send(b'HTTP/1.1 404 OK\r\nContent-Length: 14\r\n\r\nfile not found')

def main():
     while True:    
        client, addr = sock.accept()
        print('clinet')
        pid = os.fork()
        if pid == 0:
            sock.close()
            while True:
                req = client.recv(10)
                while '\r\n\r\n'.encode() not in req:
                    req += client.recv(10)
                    req = req.decode()
                    content_list = req.split('\r\n\r\n')
                    headers = content_list[0].split('\r\n')
                    headers = headers[1:]
                    print(f'headers: {headers}')
                    for i in headers:
                        parts = i.split(':')
                        key = parts[0].strip()
                        value = parts[1].strip()
                    if (key == 'Content-Length' or key == 'content-length'):
                        content_length = value
                        has_read = len(content_list[1])
                        method = req.split('\r\n')[0].split(' ')[0]
                        resource = req.split('\r\n')[0].split(' ')[1]
                        file_name = resource.split('/', 1)[1]
                        if (file_name == '' or file_name == 'favicon.ico.html'):
                            file_name = 'index.html'
                        if method == 'GET':
                            get_request(req, file_name, client)
                        elif (method == 'POST'):
                            post_request(content_length, has_read, req, client, file_name)

                        else:
                            delete_request(file_name, client)
                            os.exit()

                else:
                    client.close()

if __name__ == "__main__":
    main()
     
     