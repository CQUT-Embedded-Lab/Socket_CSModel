from socket import *


class Client:
    def __init__(self):
        self.tcp_client_socket = socket(AF_INET, SOCK_STREAM)

    def connect(self, ipaddr, port):
        HOST = ipaddr
        PORT = port
        ADDRESS = (HOST, PORT)
        self.tcp_client_socket.connect(ADDRESS)

    def send_msg(self, msg):
        data = msg
        self.tcp_client_socket.send(data.encode('utf-8'))

    def close(self):
        self.tcp_client_socket.close()


def main():
    client = Client()
    client.connect('127.0.0.1', 5057)
    while True:
        data = input('>')
        if data == '1':
            break
        if data == 'exit':
            client.close()
            break
        if not data:
            continue
        client.send_msg(data)


if __name__ == '__main__':
    main()
