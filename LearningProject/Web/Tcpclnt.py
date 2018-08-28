#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *

# HOST = 'localhost'
# PORT = 21567
# BUFSIZ = 1024
# ADDR = (HOST, PORT)
#
# tcpCliSock = socket(AF_INET, SOCK_STREAM)
# tcpCliSock.connect(ADDR)
#
# while True:
#     data = raw_input('> ')
#     if not data:
#         break
#     tcpCliSock.send(data)
#     data = tcpCliSock.recv(BUFSIZ)
#     if not data:
#         break
#     print(data.decode('utf-8'))
#
# tcpCliSock.close()



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('127.0.0.01', 9999))
# 接收欢迎消息
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarsh']:
    # 发送数据
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
