# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 12:40:57 2023

@author: User
"""

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 3000
client_socket.connect((host, port))

while True:
    message = input("輸入訊息： ")
    client_socket.send(message.encode())
    data = client_socket.recv(1024)
    print(f"伺服器回應: {data.decode()}")

client_socket.close()
