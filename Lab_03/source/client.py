import socket
import sys


class GameClient:
    def __init__(self, address, port, data_size):
        self.data_size = data_size
        self._createTcpIpSocket()
        self._connectToServer(address, port)

    def sendMsg(self, msg):
        try:
            self.sock.send(msg.encode())
        except BrokenPipeError:
            return False
        response = self.sock.recv(self.data_size).decode()
        print(response, file = sys.stderr)
        if response == "":
            return False
        else:
            return True

    def _createTcpIpSocket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _connectToServer(self, address, port):
        server_address = (address, port)
        print('connecting to %s port %s' % server_address, file = sys.stderr)
        self.sock.connect(server_address)

if __name__ == "__main__":
    host = 'localhost'
    port = 50001
    data_size = 8192
    client = GameClient(host, port, data_size)
    print(client.sock.recv(client.data_size).decode())
    while True:
        if not client.sendMsg(input()):
            break

