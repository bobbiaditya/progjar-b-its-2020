import sys
import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 10000)
print(f"starting up on {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
while True:
	print("waiting for a connection")
	connection, client_address = sock.accept()
	print(f"connection from {client_address}")
	# Receive the data in small chunks and retransmit it
	while True:
		data = connection.recv(1024)
		print('data received with "%d" length' % len(data))
		hasil = open("hasil" + ".jpg", 'a+b')
		if not data:
			hasil.close()
			break
		hasil.write(data)
	# Clean up the connection
	connection.close()
