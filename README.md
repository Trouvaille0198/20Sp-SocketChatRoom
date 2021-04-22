# 20Sp-SocketChatRoom
2020-2021 学年春季学期《计算机网络》Socket 实验

## 目录结构

```shell
20SP-SOCKETCHATROOM
|
├───README.md
│
├───TCP	// 基于TCP实现
│       client.py		// 客户端类及命令行界面
│       clientGUI.py	// 客户端GUI界面（及其入口）
│       server.py		// 服务端类及命令行界面
│       serverGUI.py	// 服务端GUI界面（及其入口）
│       TCPThread.py  	// 线程类，命令行界面专用
│
└───UDP	// 基于UDP实现
       client.py  		// 客户端/服务端
       UDPThread.py  	// 线程类
```

## 使用

克隆项目

```bash
git clone https://github.com/Trouvaille0198/20Sp-SocketChatRoom
```

### 1）UDP 程序

在 UDP 目录的 `client.py` 中修改 ip 地址与端口

```python
# 本机的ip和端口
ip = 'your ip here'
host = socket.gethostname()
port = 9000
# 目标主机的ip和端口
target_host = socket.gethostname()
target_ip = 'target ip here'
target_port = 9000
```

在命令行中运行

```shell
py client.py
```

Tips：

- UDP 协议几乎不区分服务端与客户端，故同时运行两个 `client.py` ，它们即可互相进行通信

### 2）TCP 程序—命令行版

在 TCP 目录的 `cleint.py` 和`server.py` 中修改 ip 地址与端口	

在命令行中分别运行

```shell
py server.py
py client.py
```

3. 在客户端程序中输入用户名与密码以登录

![image-20210422210031677](http://image.trouvaille0198.top/image-20210422210031677.png)

若登陆成功，此时服务端应显示

![image-20210422210415325](http://image.trouvaille0198.top/image-20210422210415325.png)

通信场景如下

![image-20210422210641547](http://image.trouvaille0198.top/image-20210422210641547.png)

Tips：

- 允许连续发送或接收多条消息

- 任意一方发送 `over` 字段即可断开连接

### 3）TCP 程序—GUI 版

在命令行中分别运行

```shell
py serverGUI.py
py clientGUI.py
```

打开服务端与客户端的 GUI 界面