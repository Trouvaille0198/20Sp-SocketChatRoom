from threading import Thread
import sys


class SendThread(Thread):
    def __init__(self, name, client, target_ip, target_port):
        Thread.__init__(self, name=name)
        self.client = client
        self.ip = target_ip
        self.port = target_port

    def run(self):
        while True:
            msg = input("client: ")
            self.client = sendto(msg.encode('utf-8'), (self.ip, self.port))
            if msg.lower() == 'over':
                sys.exit(0)


class RecvThread(Thread):
    def __init__(self, name, client):
        Thread.__init__(self, name=name)
        self.client = client

    def run(self):
        while True:
            recv_msg, from_addr = self.client.recvfrom(1024)
            print(from_addr, 'say: ', recv_msg.decode('utf-8'))
