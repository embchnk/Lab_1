import socket
import sys
import Menu
import logging
import datetime

logging.basicConfig(filename = "logs.log", level = logging.INFO)


class GameServer:
    def __init__(self, address, port, data_size):
        self.data_size = data_size
        self._createTcpIpSocket()
        self._bindSocketToPort(address, port)
        self.menu = Menu.Menu(self)
        self.buffer = 0
        self.buffer_to_send = ""
        self.connection = 0

    def add_str_to_buffer(self, string):
        self.buffer_to_send += string

    def send_buffer(self):
        self.print_str_to_client(self.buffer_to_send)
        self.buffer_to_send = ""

    def return_received_data(self):
        self.buffer = self.connection.recv(self.data_size)
        logging.info("Received data: {}".format(self.buffer.decode()))
        return self.buffer.decode()

    def print_str_to_client(self, string):
        self.connection.send(string.encode())
        logging.info("Sending string to client: {}".format(string))

    def handle_connection(self):
        self.sock.listen(1)
        logging.info("\n\n{}".format(datetime.datetime.now()))
        logging.info("Server listening...")
        try:
            self.connection, client_address = self.sock.accept()
            logging.info("Connection established")
        except KeyboardInterrupt:
            return False
        while True:
            if not self.menu.start():
                self.connection.close()
                try:
                    self.connection, client_address = self.sock.accept()
                except KeyboardInterrupt:
                    break

    def _createTcpIpSocket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _bindSocketToPort(self, address, port):
        server_address = (address, port)
        print('bind to %s port %s' % server_address, file = sys.stderr)
        self.sock.bind(server_address)

if __name__ == "__main__":
    host = 'localhost'
    port = 50001
    data_size = 8192
    server = GameServer(host, port, data_size)
    server.handle_connection()
