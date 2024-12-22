import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('127.0.0.1', 8000))
server_socket.listen(10)

print('Listening on port 8000!')

while True:
    client_socket, client_addr = server_socket.accept()
    client_request = client_socket.recv(1024).decode()
    client_requests = client_request.split('\n')
    header = client_requests[0].split(' ') 
    method = header[0]
    requested_path = header[1]
    if method == 'GET':
        print(f'GET request from {client_addr} for {requested_path}')
        if requested_path == '/' or '/index.html':
            response_file = open('./index.html')
            page = response_file.read()
            response_file.close()
            response = 'HTTP/1.1 200 OK\n\n' + page

    else:
        print(f'Faulty request from {client_addr}')
        response = 'HTTP/1.1 405 Method Not Allowed\n\nAllowed methods: GET'
        
    client_socket.sendall(response.encode())
    client_socket.close()