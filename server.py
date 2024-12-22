import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('127.0.0.1', 8000))
server_socket.listen(10)

print('Listening on port 8000!')

while True:
    client_socket, client_addr = server_socket.accept()
    print(f'Now communicating with {client_socket}, {client_addr}')
    client_request = client_socket.recv(1024).decode()
    print(f'The request sent was\n\n{client_request}')