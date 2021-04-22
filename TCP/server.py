import socket
from TCPThread import SendThread, RecvThread
import time


class Server():
    def __init__(self, ip, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ip
        self.port = int(port)

    def connect(self):
        try:
            self.server.bind((self.ip, self.port))
            self.server.listen(5)
            return True
        except:
            return False

    def accept(self):
        con, addr = self.server.accept()
        return con

    def recv(self, con):
        return con.recv(1024).decode('utf-8')

    def send(self, con, msg):
        con.send(msg.encode('utf-8'))

    def start(self):
        self.server.bind((self.ip, self.port))
        self.server.listen(5)  # 等待客户端连接
        # self.server.settimeout(300)

        while True:
            # con就是客户端链接过来而在服务端为期生成的一个链接实例
            con, addr = self.server.accept()  # 建立客户端连接
            # con.settimeout(5.0)
            self.login_check(con)
            st = SendThread('\nsend: ', con)
            rt = RecvThread('\nrecv: ', con)
            # 启动线程
            st.start()
            rt.setDaemon(True)  # 设置守护线程/后台线程
            rt.start()
            print('start server')
        con.close()  # 关闭连接

    def login_check(self, con):
        while True:
            username = con.recv(2048).decode('utf-8')
            password = con.recv(2048).decode('utf-8')
            admin = {'sun': '123', 'jimmy': '456', 'admin': '233'}
            if username not in admin.keys() or password not in admin.values():
                print("Login failed!")
                con.send("Login failed!".encode('utf-8'))
            else:
                con.send("Login successfully!".encode('utf-8'))
                return True

    def close(self):
        self.server.close()


if __name__ == '__main__':
    # 本机的ip和端口
    ip = 'your ip here'
    host = socket.gethostname()
    port = 9000
    server = Server(host, port)
    server.start()
