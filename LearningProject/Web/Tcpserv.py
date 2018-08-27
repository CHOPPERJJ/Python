#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *
from time import ctime
from threading import Thread

# HOST = ''
# PORT = 21567
# BUFSIZ = 1024
# ADDR = (HOST, PORT)
#
# tcpSerSock = socket(AF_INET, SOCK_STREAM)
# tcpSerSock.bind(ADDR)
# tcpSerSock.listen(5)
#
# while True:
#     print('waitting for connection...')
#     tcpCliSock, addr = tcpSerSock.accept()
#     print('...connected from:', addr)
#
#     while True:
#         data = tcpCliSock.recv(BUFSIZ)
#         if not data:
#             break
#         tcpCliSock.send('[%s] %s' % (bytes(ctime(), 'utf-8'), data))
#
#     tcpCliSock.close()
# tcpSerSock.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind('127.0.0.1', 9999)
s.listen(5)
print('waiting for connection...')

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

def tctlink(sock, addr):
    print('Accept new connection from %s,:%s..' % addr)
    sock.send(b'Welcom!')
    while True:
        data = sock.recb(1024)
