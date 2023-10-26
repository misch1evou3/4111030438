# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 15:28:12 2023

@author: User
"""
import socket

def fibonacci(n):
    if n <= 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[-1] + fib[-2])
        return fib

def main():
    server_ip = 'localhost'
    server_port = 3000
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)
    
    print(f"Server listening on {server_ip}:{server_port}")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        
        data = client_socket.recv(1024)
        if not data:
            break
        
        n = int(data.decode())
        print(f"Received n={n}")
        
        fib_sequence = fibonacci(n)
        response = ",".join(map(str, fib_sequence))
        
        client_socket.send(response.encode())
        print(f"Sent Fibonacci sequence to {client_address}: {response}")
        
        client_socket.close()
        print(f"Connection with {client_address} closed")

if __name__ == '__main__':
    main()
