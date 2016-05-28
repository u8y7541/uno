from socket import socket, gethostname
from threading import Thread

class UnoServer:
    def __init__(self, size):
        self.socket = socket(2, 1)
        self.socket.bind((gethostname(), 8000))
        self.size = size
        self.connections = {}
    def listen(self):
        self.socket.listen(self.size)
        while True:
            conn, addr = self.socket.accept()
            self.connections[conn] = conn.recv(1024)
            conn.send(b'Hello!')
            conn.close()
            self.socket.close()
            break
a = UnoServer(5)
a.listen()
