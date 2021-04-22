import socket
from TCPThread import SendThread, RecvThread
import time


class Client():
    def __init__(self, ip, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ip
        self.port = port

    def connect(self):
        try:
            self.client.connect((self.ip, self.port))
            return True
        except:
            return False

    def start(self):
        # 用于命令行界面的多线程函数
        st = SendThread('\nsend: ', self.client)
        rt = RecvThread('\nrecv: ', self.client)
        # 启动线程
        st.start()
        rt.setDaemon(True)  # 设置守护线程/后台线程
        rt.start()

    def login(self, username, password):
        # username = input("Please input your username: ")
        # password = input("please input your password: ")
        self.client.send(username.encode('utf-8'))
        self.client.send(password.encode('utf-8'))
        res = self.client.recv(2048).decode('utf-8')
        return res

    def login_in_shell(self):
        username = input("Please input your username: ")
        password = input("please input your password: ")
        self.client.send(username.encode('utf-8'))
        self.client.send(password.encode('utf-8'))
        res = self.client.recv(2048).decode('utf-8')
        return res

    def recv(self):
        # 对recv的一个简单封装，用于GUI界面
        return self.client.recv(1024).decode('utf-8')

    def send(self, msg):
        self.client.send(msg.encode('utf-8'))

    def close(self):
        self.client.close()

    # def recv_to_file(self):


if __name__ == '__main__':
    # 本机的ip和端口
    target_ip = 'target ip here'
    target_host = socket.gethostname()
    target_port = 9000

    client = Client(target_host, target_port)
    client.connect()
    client.login_in_shell()
    client.start()
