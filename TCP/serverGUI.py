import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext
from server import Server
import socket
import threading
import time
import sys


class ServerGUI():
    def __init__(self, master):
        self.root = master
        self.root.title('Server')
        self.root.geometry('600x600')

        # MainPage(self.root)
        ConnectPage(self.root)


class MainPage():
    def __init__(self, master, con):
        self.master = master
        self.main_page = tk.Frame(self.master)
        self.main_page.grid()
        self.con = con

        self.message_frame = scrolledtext.ScrolledText(self.main_page)
        self.message_frame.grid(row=0, column=0, rowspan=1, columnspan=4)
        tk.Label(self.main_page, text='msg ').grid(row=1)
        self.msg_entry = tk.Entry(self.main_page)
        self.msg_entry.bind('<Return>', self.send_msg)
        self.msg_entry.grid(row=1, column=1)
        self.send_btn = tk.Button(self.main_page,
                                  text='send',
                                  command=self.send_msg).grid(row=1, column=2)
        self.exit_button = tk.Button(self.main_page,
                                     text='exit',
                                     command=self.exit).grid(row=2, column=0)

        t = threading.Thread(target=self.get_msg)
        t.start()

    def get_msg(self):
        while True:
            recv_time = 'Client: ' + time.strftime('%Y-%m-%d %H:%M:%S',
                                                   time.localtime()) + '\n'
            recv_msg = server.recv(self.con) + '\n'
            self.message_frame.config(state='normal')
            self.message_frame.insert(tk.END, recv_time + recv_msg)
            self.message_frame.see(tk.END)
            self.message_frame.config(state='disabled')

    def send_msg(self, event):
        msg = self.msg_entry.get()
        server.send(self.con, msg)
        send_time = 'Server' + time.strftime('%Y-%m-%d %H:%M:%S',
                                             time.localtime()) + '\n'
        blank = ' ' * 40
        self.message_frame.config(state='normal')
        self.message_frame.insert(tk.END,
                                  blank + send_time + blank + msg + '\n')
        self.message_frame.see(tk.END)
        self.message_frame.config(state='disabled')
        self.msg_entry.delete(0, 'end')

    def exit(self):
        server.close()
        sys.exit()


class ConnectPage():
    def __init__(self, master):
        self.master = master
        self.connect_page = tk.Frame(self.master)
        self.connect_page.grid()

        tk.Label(self.connect_page, text="ip ").grid(row=0)
        self.ip_entry = tk.Entry(self.connect_page)
        self.ip_entry.grid(row=0, column=1)
        tk.Label(self.connect_page, text="port ").grid(row=1)
        self.port_entry = tk.Entry(self.connect_page)
        self.port_entry.grid(row=1, column=1)
        self.connect_btn = tk.Button(self.connect_page,
                                     text='connect',
                                     command=self.connect).grid(row=3)

    def connect(self):
        ip = self.ip_entry.get() if self.ip_entry.get(
        ) else socket.gethostname()
        port = int(self.port_entry.get()) if self.port_entry.get() else 9000
        global server
        server = Server(ip, port)
        is_connected = server.connect()
        if is_connected == True:
            self.connect_page.destroy()
            WaitPage(self.master)
        else:
            messagebox.showerror("Error", "connection failed!")


class WaitPage():
    def __init__(self, master):
        self.master = master
        self.wait_page = tk.Frame(self.master)
        self.wait_page.grid()

        tk.Message(self.wait_page, text="Waiting for others to connect...").grid()

        t = threading.Thread(target=self.waiting)
        t.start()

    def waiting(self):
        while True:
            self.con = server.accept()
            flag = server.login_check(self.con)
            if flag == True:
                self.wait_page.destroy()
                MainPage(self.master, self.con)


if __name__ == '__main__':
    root = tk.Tk()
    ServerGUI(root)
    root.mainloop()
