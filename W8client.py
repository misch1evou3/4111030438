# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import socket

def main():
    server_ip = 'localhost'
    server_port = 3000
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    
    n = int(input("Enter the length of the Fibonacci sequence: "))
    client_socket.send(str(n).encode())
    
    data = client_socket.recv(1024)
    fib_sequence = data.decode()
    
    print(f"Fibonacci sequence of length {n}: {fib_sequence}")
    
    client_socket.close()

if __name__ == '__main__':
    main()
