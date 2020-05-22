import socket
import time
import sys
import asyncore
import logging
import subprocess 
flag = 0
portnum = 8000
# class Timer:
#       def __init__(self):
#     self._start_time = None


#   def start(self):
#     if self._start_time is not None:
#       print("Timer is running. Use .stop() to stop it")
#     self._start_time = time.perf_counter()


#   def stop(self):
#     test = time.perf_counter()
#     # print(test-self._start_time)
#     if test-self._start_time > 0.0001:
#       elapsed_time = time.perf_counter() - self._start_time
#       self._start_time = None
#       print(f"Elapsed time: {elapsed_time:0.4f} seconds")
class BackendList:
	def __init__(self):
		self.servers=[]
		self.servers.append(('127.0.0.1',8000))
		self.current=0

	def getserver(self):
		s = self.servers[self.current]
		self.current=self.current+1
		if (self.current>=len(self.servers)):
			self.current=0
		return s

	def addserver(self):		
		global portnum
		portnum += 1
		self.servers.append(('127.0.0.1',portnum))
class Backend(asyncore.dispatcher_with_send):
	def __init__(self,targetaddress):
		asyncore.dispatcher_with_send.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connect(targetaddress)
		self.connection = self

	def handle_read(self):
		try:
			self.client_socket.send(self.recv(8192))
		except:
			pass
	def handle_close(self):
		try:
			self.close()
			self.client_socket.close()
		except:
			pass


class ProcessTheClient(asyncore.dispatcher):
	def handle_read(self):
		data = self.recv(8192)
		if data:
			self.backend.client_socket = self
			self.backend.send(data)
	def handle_close(self):
		self.close()

class Server(asyncore.dispatcher):
	def __init__(self,portnumber):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.set_reuse_addr()
		self.bind(('',portnumber))
		self.listen(5)
		self.bservers = BackendList()
		logging.warning("load balancer running on port {}" . format(portnumber))

	def handle_accept(self):
		pair = self.accept()
		global flag
		if pair is not None:
			sock, addr = pair
			logging.warning("connection from {}" . format(repr(addr)))
			flag +=1
			if(len(self.bservers.servers)<=10):
				if(flag == 100):
					flag = 0
					self.bservers.addserver()
			#menentukan ke server mana request akan diteruskan
			bs = self.bservers.getserver()
			logging.warning("koneksi dari {} diteruskan ke {}" . format(addr, bs))
			print(portnum) 
			backend = Backend(bs)

			#mendapatkan handler dan socket dari client
			handler = ProcessTheClient(sock)
			handler.backend = backend

def main():
	portnumber=44444
	try:
		portnumber=int(sys.argv[1])
	except:
		pass
		svr = Server(portnumber)
		asyncore.loop()

if __name__=="__main__":
	main()


