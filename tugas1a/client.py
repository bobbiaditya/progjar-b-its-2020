import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print ('connecting')
sock.connect(server_address)
try:
    # Send data
    file_name="foto.jpg"
    file = open(file_name,'rb')
    content =file.read()
    # message = 'latian woi latian latian woi latian latian woi latian latian woi latian'
    print ('sending "%s"' % content)
    sock.sendall(content)
    # Look for the response
    amount_received = 0
    amount_expected = len(content)
    while amount_received < amount_expected:
        data = sock.recv(10^24)
        hasil = open("hasil"+file_name,'a+b')
        hasil.write(data)
        amount_received += len(data)
    contenth = file.read()
    print ('received "%s"' % contenth)
finally:
    print ('closing socket')
    sock.close()
