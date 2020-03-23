import socket
import sys
from time import sleep
import base64

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
port_num = 8888
server_address = ('127.0.0.1', port_num)
print("Connecting to Server: 127.0.0.1" , " Port:", port_num)
sock.connect(server_address)

try:
    msg = "list_file"
    sock.send(msg.encode())
    print("\nRequest sent\n")
    data = sock.recv(2048)
    print(data.decode())
finally:
    sock.close()