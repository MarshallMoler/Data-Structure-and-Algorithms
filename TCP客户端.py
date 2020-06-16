import socket


class ClientSocket(object):

    def __init__(self, ip_addr, port):

        self.__address = ip_addr
        self.__port = port

    def tcp_socket(self):

        while True:
            tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_sock.connect((self.__address, self.__port))
            info = input("请输入您要发送的信息：")
            tcp_sock.send(info.encode('utf-8'))
            buf = tcp_sock.recv(4096)
            if len(buf) != 0:
                try:
                    print(buf.decode('utf-8'))
                except Exception:
                    print(buf.decode('gbk'))
            else:
                break


if __name__ == "__main__":

    cs = ClientSocket("127.0.0.1", 8080)
    cs.tcp_socket()
