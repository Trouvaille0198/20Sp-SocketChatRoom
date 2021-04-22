from threading import Thread
import sys
import socket


class SendThread(Thread):
    def __init__(self, name, socket):
        Thread.__init__(self, name=name)
        self.socket = socket

    def run(self):
        while True:
            msg = input()
            self.socket.send(msg.encode('utf-8'))
            if msg.lower() == 'over':
                # sys.exit(0)
                self.socket.close()


class RecvThread(Thread):
    def __init__(self, name, socket):
        Thread.__init__(self, name=name)
        self.socket = socket

    def run(self):
        while True:
            recv_msg = self.socket.recv(1024)
            print('msg received: ', recv_msg.decode('utf-8'))
