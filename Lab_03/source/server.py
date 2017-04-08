import socket
import sys
import Menu


class EchoServer:
    def __init__(self, address, port, data_size):
        self.data_size = data_size
        self._createTcpIpSocket()
        self._bindSocketToPort(address, port)
        self.menu = Menu.Menu(self)
        self.buffer = 0
        self.connection = 0

    def return_received_data(self):
        self.buffer = self.connection.recv(self.data_size)
        return self.buffer.decode()

    def print_str_to_client(self, string):
        self.connection.send(string.encode())

    def handle_connection(self):
        self.sock.listen(1)
        self.connection, client_address = self.sock.accept()
        self.menu.start()
        self.connection.close()

    def _createTcpIpSocket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _bindSocketToPort(self, address, port):
        server_address = (address, port)
        print('bind to %s port %s' % server_address, file = sys.stderr)
        self.sock.bind(server_address)

if __name__ == "__main__":
    host = 'localhost'
    port = 50001
    data_size = 1024
    server = EchoServer(host, port, data_size)
    server.handle_connection()
