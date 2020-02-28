
import socket

TARGET_IP = "192.168.1.12"
TARGET_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes('Informatika'.encode()),(TARGET_IP,TARGET_PORT))