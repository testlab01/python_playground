import socket

class ServerSocket:

	def __init__(self):
		self.serverSocket = 'none';

	def open_socket(self, host = 'localhost', port = 8080):
		self.host = host
		self.port = port
		if self.serverSocket == 'none':
			try:
				self.serverSocket = socket.socket()
			except socket.error as errorMsg:
				print(errorMsg)
		else:
			self.serverSocket


socketS = ServerSocket()
socketS.open_socket()
