# from source import Menu
import Menu
import server



if __name__ == "__main__":
    host = 'localhost'
    port = 50001
    data_size = 1024
    server = server.EchoServer(host, port, data_size)
    server.handle_connection()
