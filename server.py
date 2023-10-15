# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 14:43:08 2023

@author: User
"""


import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 3000
server_socket.bind((host, port))

# 開始監聽連接
server_socket.listen(5)
print(f"伺服器正在監聽 {host}:{port}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"接收來自 {client_address} 的連接")
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        client_socket.send(data)
    client_socket.close()
