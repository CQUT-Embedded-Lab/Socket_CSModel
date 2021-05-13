from socket import *
from time import ctime
import threading


class Server:
    def __init__(self):
        self.BUFFSIZE = 1024
        self.tcp_server_socket = socket(AF_INET, SOCK_STREAM)
        self.tcp_client_socket_list = []  # 放每个客户端的socket

    def create_server(self, ipaddr, port):
        HOST = ipaddr
        PORT = port

        ADDR = (HOST, PORT)
        self.tcp_server_socket.bind(ADDR)
        self.tcp_server_socket.listen(5)

    def handle(self, tcp_client_socket_list, BUFFSIZE):
        while True:
            for tcp_client_socket in tcp_client_socket_list:
                try:
                    data = tcp_client_socket.recv(BUFFSIZE)
                except Exception as e:
                    continue
                if not data:
                    tcp_client_socket_list.remove(tcp_client_socket)
                    continue
                print('[{}][{}]: {}'.format(ctime(), tcp_client_socket.getpeername(), data))
                tcp_client_socket.send(bytes('[{}][{}]: {}'.format(ctime(), tcp_client_socket, data), encoding="utf-8"))

    def start(self):
        t = threading.Thread(target=self.handle, args=(self.tcp_client_socket_list, self.BUFFSIZE,))  # 子线程
        t.start()
        print(u'我在%s线程中 ' % threading.current_thread().name)  # 本身是主线程
        print('waiting for connecting...')
        while True:
            tcp_client_socket, addr = self.tcp_server_socket.accept()
            print('connected from:', addr)
            tcp_client_socket.setblocking(False)
            self.tcp_client_socket_list.append(tcp_client_socket)


def main():
    server = Server()
    server.create_server('127.0.0.1', 5057)
    server.start()


if __name__ == '__main__':
    main()
