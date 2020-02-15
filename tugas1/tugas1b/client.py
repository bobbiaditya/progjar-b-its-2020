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
    file_name="259958.jpg"
    content =file_name
    print ('sending data...')
    sock.sendall(content.encode())
    while 1:
        data = sock.recv(1024)
        print('data received with "%d" length' % len(data))
        hasil = open("hasil"+file_name,'a+b')
        if not data:
            hasil.close()
            break
        hasil.write(data)
    print ('received "%s"' % file_name)

finally:
    print ('closing socket')

    sock.close()
