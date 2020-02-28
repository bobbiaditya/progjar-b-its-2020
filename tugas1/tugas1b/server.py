import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('192.168.1.19', 10000)
print(f"starting up on {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
while True:
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")
    data = connection.recv(1024)
    print('receiving data...')
    file = open(data.decode(), 'rb')
    content = file.read(1024)
    # Receive the data in small chunks and retransmit it
    while content:
        connection.sendall(content)
        print("sending", repr(content))
        content = file.read(1024)
    print("File Terkirim")
    file.close()
    # Clean up the connection
    connection.close()
