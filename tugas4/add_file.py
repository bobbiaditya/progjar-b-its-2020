import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port_num = 8888
server_address = ('127.0.0.1', port_num)
print("Connecting to Server: 127.0.0.1" , " Port:", port_num)
sock.connect(server_address)

try:
    filename="upload1.txt"
    temp = open(filename,"rb")
    file = temp.read(2048)
    temp.close()
    file = file.decode()
    msg = "add_file "+filename+" "+file
    # print(file)
    print ("Adding File")
    sock.send(msg.encode())

    data = sock.recv(2048).decode()
    print(data)
finally:
    print("Closing Connection")
    sock.close()