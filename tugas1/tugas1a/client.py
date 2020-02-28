import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.1.7', 10000)
print ('connecting')
sock.connect(server_address)
try:
    # Send data
    file_name="259958.jpg"
    file = open(file_name,'rb')
    content =file.read()
    print ('sending data...')
    sock.sendall(content)
    # print ("done!")
finally:
    print ('closing socket')
    sock.close()
