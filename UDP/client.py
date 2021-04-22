import socket
from UDPThread import SendThread, RecvThread


if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 本机的ip和端口
    ip = 'your ip here'
    host = socket.gethostname()
    port = 9000
    # 目标主机的ip和端口
    target_host = socket.gethostname()
    target_ip = 'target ip here'
    target_port = 9000
    # 绑定
    client.bind((host, port))
    st = SendThread('\nsend: ', client, target_host, target_port)
    rt = RecvThread('\nrecv: ', client)

    # 启动线程
    st.start()
    rt.setDaemon(True)  # 设置守护线程   后台线程
    rt.start()
